import os
import boto3
import pandas as pd
from sqlalchemy import create_engine, text
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# -------- MinIO Config --------
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "http://minio:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin123")
BUCKET = os.getenv("MINIO_BUCKET", "raw")
LOCAL_DIR = os.getenv("MINIO_LOCAL_DIR", "/tmp/minio_downloads")

# -------- PostgreSQL Destination Config --------
POSTGRES_DEST_USER = os.getenv("POSTGRES_DEST_USER", "marketinguser")
POSTGRES_DEST_PASSWORD = os.getenv("POSTGRES_DEST_PASSWORD", "marketingpass")
POSTGRES_DEST_DB = os.getenv("POSTGRES_DEST_DB", "marketingdb_destination")
POSTGRES_DEST_SCHEMA = os.getenv("POSTGRES_DEST_SCHEMA", "raw")
POSTGRES_DEST_HOST = "postgres-dest"
POSTGRES_DEST_PORT = 5432

TABLES = ["ecommerce_sales"]

# -------- Python Callables --------
def download_from_minio():
    os.makedirs(LOCAL_DIR, exist_ok=True)
    s3 = boto3.client(
        "s3",
        endpoint_url=MINIO_ENDPOINT,
        aws_access_key_id=MINIO_ACCESS_KEY,
        aws_secret_access_key=MINIO_SECRET_KEY
    )
    local_files = {}
    for table in TABLES:
        prefix = f"{table}/"
        resp = s3.list_objects_v2(Bucket=BUCKET, Prefix=prefix)
        objects = resp.get("Contents", [])
        local_files[table] = []
        for obj in objects:
            key = obj["Key"]
            local_file = os.path.join(LOCAL_DIR, os.path.basename(key))
            s3.download_file(BUCKET, key, local_file)
            print(f"Downloaded {key} -> {local_file}")
            local_files[table].append(local_file)
    return local_files

def load_to_postgres(ti):
    local_files = ti.xcom_pull(task_ids="download_minio")
    if not local_files:
        print("No files found in MinIO.")
        return

    engine = create_engine(
        f"postgresql+psycopg2://{POSTGRES_DEST_USER}:{POSTGRES_DEST_PASSWORD}"
        f"@{POSTGRES_DEST_HOST}:{POSTGRES_DEST_PORT}/{POSTGRES_DEST_DB}"
    )

    with engine.connect() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {POSTGRES_DEST_SCHEMA}"))
        conn.commit()

    for table, files in local_files.items():
        if not files:
            print(f"No files for {table}, skipping.")
            continue

        dfs = []
        for f in files:
            df = pd.read_parquet(f, engine="fastparquet")
            dfs.append(df)
            print(f"Read {len(df)} rows from {f}")

        if dfs:
            df_all = pd.concat(dfs, ignore_index=True)
            df_all.to_sql(
                name=table,
                con=engine,
                schema=POSTGRES_DEST_SCHEMA,
                if_exists="append",
                index=False
            )
            print(f"✅ Loaded {len(df_all)} rows into {POSTGRES_DEST_SCHEMA}.{table}")

    engine.dispose()

# -------- Airflow DAG --------
default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="minio_to_postgres_marketing",
    default_args=default_args,
    description="Load MinIO parquet into PostgreSQL destination RAW schema",
    schedule="*/5 * * * *",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["minio", "postgres", "marketing"],
) as dag:

    task1 = PythonOperator(
        task_id="download_minio",
        python_callable=download_from_minio,
    )

    task2 = PythonOperator(
        task_id="load_postgres",
        python_callable=load_to_postgres,
    )

    task1 >> task2

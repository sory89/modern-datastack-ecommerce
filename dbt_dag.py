"""
DAG dbt compatible Airflow 3.
Airflow 3 introduit le nouveau SDK de task — on utilise toujours
BashOperator qui reste supporté, mais avec la syntaxe @task décorateur
disponible si besoin.
"""
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

DBT_PROJECT_DIR = "/opt/airflow/marketing_dbt"
DBT_PROFILES_DIR = "/home/airflow/.dbt"
DBT_CMD = f"cd {DBT_PROJECT_DIR} && dbt"

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="dbt_marketing_pipeline",
    description="Pipeline dbt complet : deps → run → test",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",           # Airflow 3 : schedule= remplace schedule_interval=
    catchup=False,
    default_args=default_args,
    tags=["dbt", "marketing"],
) as dag:

    dbt_deps = BashOperator(
        task_id="dbt_deps",
        bash_command=f"{DBT_CMD} deps --profiles-dir {DBT_PROFILES_DIR}",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"{DBT_CMD} run --profiles-dir {DBT_PROFILES_DIR}",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"{DBT_CMD} test --profiles-dir {DBT_PROFILES_DIR}",
    )

    dbt_deps >> dbt_run >> dbt_test
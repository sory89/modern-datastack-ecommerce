from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import sys

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

DBT_DIR = "/opt/airflow/marketing_dbt"

def run_dbt(command: str):
    sys.path = [p for p in sys.path if p]
    original_getcwd = os.getcwd
    os.getcwd = lambda: DBT_DIR
    os.chdir(DBT_DIR)

    try:
        from dbt.cli.main import dbtRunner, dbtRunnerResult
        runner = dbtRunner()
        args = command.split() + ["--profiles-dir", DBT_DIR, "--project-dir", DBT_DIR]
        result: dbtRunnerResult = runner.invoke(args)
        if not result.success:
            raise Exception(f"dbt {command} failed: {result.exception}")
    finally:
        os.getcwd = original_getcwd

with DAG(
    dag_id="scd2_snapshots",
    default_args=default_args,
    description="Run dbt snapshots SCD2 + gold models",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["dbt", "snapshots", "marketing"],
) as dag:

    dbt_run_bronze = PythonOperator(
        task_id="dbt_run_bronze",
        python_callable=run_dbt,
        op_args=["run --select bronze"],
    )

    dbt_run_silver = PythonOperator(
        task_id="dbt_run_silver",
        python_callable=run_dbt,
        op_args=["run --select silver"],
    )

    dbt_snapshot = PythonOperator(
        task_id="dbt_snapshot",
        python_callable=run_dbt,
        op_args=["snapshot"],
    )

    dbt_run_gold = PythonOperator(
        task_id="dbt_run_gold",
        python_callable=run_dbt,
        op_args=["run --select gold"],
    )

    dbt_test = PythonOperator(
        task_id="dbt_test",
        python_callable=run_dbt,
        op_args=["test"],
    )

    dbt_run_bronze >> dbt_run_silver >> dbt_snapshot >> dbt_run_gold >> dbt_test
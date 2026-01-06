from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

SCRIPT_PATH = "/opt/airflow/scripts"

def run_meteo_script():
    sys.path.append(SCRIPT_PATH)
    from meteo_script import MeteoAPI

    meteo = MeteoAPI(latitude=48.8566, longitude=2.3522)
    meteo.fetch_and_save("/opt/airflow/data/raw")


default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="meteo_logs_collection",
    default_args=default_args,
    description="Récupération des logs météo via Open-Meteo API",
    schedule="0 * * * *",   # ✅ NOUVELLE SYNTAXE
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["meteo", "api"],
) as dag:

    fetch_meteo_logs = PythonOperator(
        task_id="fetch_meteo_logs",
        python_callable=run_meteo_script,
    )

from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
import sys 

sys.path.append("/opt/airflow/api_request")
from insert_data import main


default_args = {
    "description" : "orchestration for pipelines",
    "start_date" : datetime(2025 ,5 , 2),
    "catchup" : False
}

dags = DAG (
    dag_id = "weather-api-dbt-orchestration",
    default_args = default_args,
    schedule = timedelta(minutes=1)
)

with dags:
    task1 = PythonOperator(
        task_id = 'insert-record-task',
        python_callable = main
    )

    task2 = DockerOperator(
        task_id = 'transforming-data-dbt',
        image = 'ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command = 'run',
        working_dir = '/usr/app',
        mounts = [
            Mount(source = '/home/ayush/repos/weatherapi_project/dbt/dbt/my_project',
            target = '/usr/app',
            type = 'bind'),
            Mount(source = '/home/ayush/repos/weatherapi_project/dbt/dbt/profiles.yml',
            target = '/root/.dbt/profiles.yml',
            type = 'bind')
        ],
        network_mode = 'weatherapi_project_my-network',
        docker_url = 'unix://var/run/docker.sock',
        auto_remove = 'success'
    )


task1>>task2
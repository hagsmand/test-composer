from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG('example_dag', start_date=datetime(2025, 1, 1), schedule_interval=None) as dag:
    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')
    start >> end
    
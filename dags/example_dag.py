from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG('example_dag', start_date=datetime(2025, 1, 1), schedule=None) as dag:
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')
    start >> end

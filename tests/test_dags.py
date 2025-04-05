import pytest
from airflow.models import DagBag

def test_dag_integrity():
    dag_bag = DagBag(dag_folder='dags/', include_examples=False)
    assert len(dag_bag.import_errors) == 0, "DAG import errors found"
    dag = dag_bag.get_dag('example_dag')
    assert dag is not None, "DAG not found"
    assert len(dag.tasks) == 2, "Unexpected number of tasks"

    
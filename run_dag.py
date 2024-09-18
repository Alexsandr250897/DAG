import json

from dag_execution import DAGRunner
from models import DAG


with open('dag.json') as f:
    dag_data = json.load(f)
    dag = DAG(**dag_data)

dag_runner = DAGRunner(dag)

dag_runner.execute_tasks()

import datetime as dt

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.latest_only_operator import LatestOnlyOperator
from airflow.utils.dates import days_ago


dag = DAG(
    dag_id='second_dag_example',
    schedule_interval=dt.timedelta(days=2),
    start_date=days_ago(2)
)

latest_only = LatestOnlyOperator(task_id='latest_only', dag=dag)
task1 = DummyOperator(task_id='task1', dag=dag)

latest_only >> task1

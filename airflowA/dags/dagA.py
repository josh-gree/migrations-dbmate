from datetime import timedelta

import airflow
from airflow.models import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.bash_operator import BashOperator

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='redhshift_ops',
    default_args=args,
    schedule_interval=None,
    template_searchpath='/usr/local/airflow/dags'
)

pg_op = PostgresOperator(
    task_id = 'pg_op',
    sql='sample.sql',
    postgres_conn_id='pg_conn',
    dag=dag
)

pg_op
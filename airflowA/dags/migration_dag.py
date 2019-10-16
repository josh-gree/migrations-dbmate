import os
from datetime import timedelta

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='migration_op',
    default_args=args,
    schedule_interval=None,
    template_searchpath='/usr/local/airflow/dags'
)

migrate_op = BashOperator(
    task_id = 'migragte',
    bash_command= 'dbmate --migrations-dir /usr/local/airflow/dags/migrationrepo/db/migrations --no-dump-schema migrate',
    env={
        'DATABASE_URL':'postgres://redshift:redshift@redshift:5432/redshift?sslmode=disable',
        **os.environ
    },
    dag=dag
)

migrate_op
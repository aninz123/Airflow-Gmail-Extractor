from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


def get_email_report():
    pass


default_args = {
    'owner' : 'admin',
    'depends_on_past':False,
    'start_date' : datetime(2023,9,1),
    'retries':1,
    'retry_delay':timedelta(minutes=2)
}

dag = DAG('gmail_report_dag',default_args=default_args,schedule_interval=timedelta(days=1))

task = PythonOperator(
    task_id= 'get_gmail_reports',
    python_callable= get_email_report,
    dag=dag
)
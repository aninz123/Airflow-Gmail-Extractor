from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

def print_hello():
    return 'Hello from Airflow!'

def create_text_file():
    with open('/tmp/sample.txt', 'w') as f:
        f.write('This is a sample text file created by Airflow')
    return 'File created successfully'

default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'simple_example',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
)

task1 = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

task2 = PythonOperator(
    task_id='create_file',
    python_callable=create_text_file,
    dag=dag,
)

task1 >> task2
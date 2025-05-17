
import sys
sys.path.append('/opt/airflow/scripts')
from extract import run_queries
from transform import transform
from load import load

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='tripadvisor_etl',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    def extract_task(**context):
        data = run_queries()  # เรียก extract
        return data  # คืนค่าให้ XCom

    def transform_task(**context):
        ti = context['ti']
        extracted_data = ti.xcom_pull(task_ids='extract1')
        transformed_data = transform(extracted_data)  # เรียก transform
        return transformed_data

    def load_task(**context):
        ti = context['ti']
        transformed_data = ti.xcom_pull(task_ids='transform1')
        load(transformed_data)  # เรียก load (ไม่มี return)

    extracted = PythonOperator(
        task_id='extract1',
        python_callable=extract_task,
        provide_context=True,
    )

    transformed = PythonOperator(
        task_id='transform1',
        python_callable=transform_task,
        provide_context=True,
    )

    loaded = PythonOperator(
        task_id='load1',
        python_callable=load_task,
        provide_context=True,
    )

    extracted >> transformed >> loaded

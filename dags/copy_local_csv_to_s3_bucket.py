from datetime  import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator



# define default args
default_args = {
    'owner': 'airflow',
    'retries' : 2,
    'relay_delay' : timedelta(minutes=5)
}

with DAG(
    dag_id='copy_local_csv_to_s3_bucket',
    default_args=default_args,
    start_date=datetime(2023, 2, 22),
    schedule_interval='0 0 * * *',
    tags=["local_to_s3"]
) as dag:
    copy_csv_file_to_s3_bucket_task = LocalFilesystemToS3Operator(
    task_id="copy_csv_file_to_s3_bucket",
    filename='data/invoices.csv',
    dest_key='invoices.csv',
    dest_bucket='de-proj01-bucket',
    aws_conn_id='aws_default',
    replace=True
    )
    copy_csv_file_to_s3_bucket_task
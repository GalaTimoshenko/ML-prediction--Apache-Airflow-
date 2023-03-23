import datetime as dt
import os
import sys

from airflow.models import DAG
from airflow.operators.python import PythonOperator

from modules.pipeline import pipeline
from modules.predict import predict


path = os.path.expanduser('~/PycharmProjects/33homework')
# Добавим путь к коду проекта в переменную окружения, чтобы он был доступен python-процессу
os.environ['PROJECT_PATH'] = path
# Добавим путь к коду проекта в $PATH, чтобы импортировать функции
sys.path.insert(0, path)
path = os.environ.get('PROJECT_PATH', '.')

args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2022, 6, 10),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'depends_on_past': False,
}

with DAG(
        dag_id='car_price_prediction',
        schedule_interval="00 15 * * *",
        default_args=args,

# После того, как подготовили каркас Базовые параметры - Функции - Даг вводим питон операции

) as dag:

    # первое задание в даг
    pipeline = PythonOperator(
        task_id='model_creation',
        python_callable=pipeline,
        dag=dag,
    )

    # второе задание в даг
    predict = PythonOperator(
        task_id='price_prediction',
        python_callable=predict,
        dag=dag,
    )
 # Порядок выполнения тасок
    pipeline >> predict
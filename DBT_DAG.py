from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# DBT PATH
DBT_PROJECT_DIR = "/usr/local/airflow/include/dbt_SF"  

# DAG Definition 
with DAG(
    dag_id="dbt_dag",
    start_date=datetime(2025, 6, 28),
    schedule_interval="@daily",  # fixed typo
    catchup=False,
    tags=["snowflake", "daily", "dbt"],
) as dag:

    # first task
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command=f'cd {DBT_PROJECT_DIR} && dbt run',
    )

    # second task
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command=f'cd {DBT_PROJECT_DIR} && dbt test',
    )

    # Define task dependencies
    dbt_run >> dbt_test


#DAG with decorator


from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from datetime import datetime

DBT_PROJECT_DIR = "/usr/local/airflow/include/dbt_SF"


@dag(
    dag_id="dbt_daggll",
    start_date=datetime(2025, 6, 28),
    schedule="@daily",
    catchup=False,
    tags=["dbt", "snowflake"],
)
def dbt_workflow():

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command=f'cd {DBT_PROJECT_DIR} && dbt run 

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command=f'cd {DBT_PROJECT_DIR} && dbt test 
    )

    dbt_run >> dbt_test


dbt_workflow()

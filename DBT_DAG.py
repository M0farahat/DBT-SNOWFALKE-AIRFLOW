from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


# DBT PATH
DBT_PROJECT_DIR = "C:\Users\mofar\dbt-project" 

# DAG Definition 

with DAG( dag_id= "dbt_dag",
         start_date= datetime(2025,6,28),
         scedule_interval= "@daily",
         catchup=False,
         tags= ["snowflake","daily","dbt"],
) as dag :
  
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


  



  

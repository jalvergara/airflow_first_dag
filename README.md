# Steps to run airflow using docker:

Note: You need docker installed to run this repo

1. Create a folder 
2. clone this repository
3. Go to the root of the repository
4. Run `docker-compose up airflow-init`
5. Run `docker-compose up`
6. Go to: http://localhost:8080/
7. Log in with the credentials: airflow airflow
8. Run the dag: api_dag
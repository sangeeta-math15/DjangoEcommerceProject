# DjangoEcommerceProject
Steps to be followed to setup the project 

Clone the repository

```git clone git@github.com:sangeeta-math15/DjangoEcommerceProject.git```

```cd DjangoEcommerceProject```

```mv /path/to/sample.json .```

Setup Project locally

Assuming postgresql is installed on your machine, run the following commands to setup the postgres for project

```sudo -u postgres psql```

```CREATE USER postgres WITH PASSWORD Sang@123;```

```CREATE DATABASE ecommerce_db OWNER postgres;```

Quit the psql terminal using ```\q```

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py loaddata sample.json```

```python manage.py runserver```

APIs collection

To add data to RegularFit and RelaxedFit table use the following command(Note: Only once per setup)

```http://127.0.0.1:8000/update_records_db```

To fetch records 

```http://127.0.0.1:8000/get_fit_results?type_of_fit=relaxed```

```http://127.0.0.1:8000/get_fit_results?type_of_fit=regular```

How to setup the project using a Dockerfile:

Building a docker image

```docker build -t flip kart .```

If a Postgres service is running the stop it by the following command

```sudo systemctl stop postgresql```

Create a docker network which helps in communication between docker containers

```docker network create my-project-postgres-network```

Build and run a Postgres official image

```docker run --name my-postgres -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=Sang@123 --network my-project-postgres-network -d postgres```

Open an interactive shell and add users as follows  - docker exec -it my-postgres bash

```psql -U postgres```

CREATE DATABASE ecommerce_db OWNER postgres
```\q```
Create a .env file and add the following line in it

```DATABASE_HOST=my-postgres```

Running Django project application

```docker run --env-file .env --name django-flipkart-app -p 8000:8000 --network my-project-postgres-network -d flip kart```

To apply migrations please use the following command 

```docker run django-flipkart-app sh -c "python manage.py migrate && python manage.py loaddata sample.json```

To add data to RegularFit and RelaxedFit table use the following command(Note: Only once per setup)

```http://127.0.0.1:8000/update_records_db```

To fetch records 

```http://127.0.0.1:8000/get_fit_results?type_of_fit=relaxed```

```http://127.0.0.1:8000/get_fit_results?type_of_fit=regular```



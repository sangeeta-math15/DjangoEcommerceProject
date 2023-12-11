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



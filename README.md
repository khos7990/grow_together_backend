# Backend

# Getting Started

## Python Virtual Environments

Whenever you're working on a Python project that uses external dependencies, creating a virtual environment is best. [Link](https://realpython.com/python-virtual-environments-a-primer/)

### Create a Python Virtual Environment
```
python3 -m venv venv
```
### Activating the environment (mac/unix)
```
source venv/bin/activate
```

### Deactivating the environment
```
deactivate
```
## Python Virtual Envronments Linux:

## Install venv tool
sudo apt install python3-venv

### Create a Python Virtual Environment
python3 -m venv venv
```
### Activating the environment (Linux)
```
source env/bin/activate
```

### Deactivating the environment
```
deactivate


### Installing dependencies

- See requirements.txt file to look at the dependencies
- To install all dependencies:

```
pip install -r requirements.txt
```
- To install dependencies individually:
```
python -m pip install <package-name>
```
- After installing dependencies
```
pip3 freeze > requirements.txt
```

<hr>

#### General Info on Dependencies
- CORS allows interaction of ressources between domains [django-cors-headers](https://pypi.org/project/django-cors-headers/)
(i.e. localhost:3000 and localhost:8000)
- Psycopg2 is a library to connect Django to PostgreSQL [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
- Simple JWT provides a JSON Web Token authentication backend for the django rest framework [simple-jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

<hr>

## Create a dotenv file in backend folder
```
DJANGO_SECRET_KEY='<secret-key>'
```

# Small application that provides API for tickets booking

## Installation with PIP
Create virtual environment for python ^3.8, according to this:  
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/.  
Install with pip:
```$ pip install -r requirements.txt```

## Installation with Pyenv & Poetry
Or I strongly recommend using pyenv for python version management:
https://github.com/pyenv/pyenv

and poetry for package management:
https://python-poetry.org/docs/

find poetry.lock file in project directory and run:
```
poetry install
```

get docker from:
https://www.docker.com/get-started

after installing docker run:
```docker run -d -p 5672:5672 rabbitmq```

next run:
```
poetry run python manage.py migrate
```
```
poetry run python manage.py runserver
```
```
poetry run celery -A ticket_selling worker -B -E -l info
```

The application runs on port 8000.
It is available at http://localhost:8000/.

You can find API docs at http://localhost:8000/api/v1/swagger/

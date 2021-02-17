# v27-bears-team-04-backend

## Features
Django Python 3.9 Postgres13 Pytest for backend tests


## development:
- Install postgreSQL:
    - Mac: brew install postgres: https://medium.com/@viviennediegoencarnacion/getting-started-with-postgresql-on-mac-e6a5f48ee399
    - Linux/Ubuntu: http://doc.ubuntu-fr.org/postgresql
    - Windows: https://www.postgresqltutorial.com/install-postgresql/

- Install python3.9:
    - Mac/Windows: https://www.python.org/downloads/
    - Ubuntu: https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/

- Install python environment:
    - ubuntu:
        - sudo apt-get install python3-pip
        - sudo pip3 install virtualenv

When cloning, do for the first time:

- Enter your directory:
    - cd v27-bears-team-04-backend/

- Create a secret key, tape in your terminal:
    - openssl rand -hex 32

- Create your local database:
    - Connect to postgres:
        - Mac: psql postgres
        - Ubuntu: sudo -i psql -u postgres
    - Create database:
        - CREATE DATABASE morseapp;
    - Create new user:
        - CREATE USER username WITH PASSWORD 'yourpassword';
    - Grant privilege to database to your user:
        - GRANT ALL PRIVILEGES ON DATABASE morseapp TO username;

- Create python virtual environment:
    - python3 -m venv .venv
    - source venv/bin/activate

- install requirements.txt:
    - pip install -r requirements.txt

- Create a .env file with that syntax:
    - DEBUG=True
    - SECRET_KEY=secret_key (copy/paste your terminal's code)
    - POSTGRES_USER=username
    - POSTGRES_PASSWORD=password
    - POSTGRES_HOST=localhost
    - POSTGRES_PORT=5432
    - POSTGRES_DB=morseapp

- Create first tables:
    - python manage.py migrate

- load django server:
    - python manage.py runserver
    
- url for create new users:
    - http://127.0.0.1:8000/api/user/create

Add-project-description-here | Voyage-27 | https://chingu.io/ | Twitter: https://twitter.com/ChinguCollabs

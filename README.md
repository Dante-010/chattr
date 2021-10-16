# Chattr: A simple live chat website

## Running the app

First, you should create a file named: 'secret_key.txt' (or anything you want really, you can change this in the [settings.py](chattr/settings.py) file) and add a Django secret key.
You can generate one using this code:
```python
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```
This is just a placeholder, the real key is kept secret on my machine ;).

Then, simply run `docker-compose up` in order to run the app.
## docker-compose layout

This app is composed of four services: **nginx**, **daphne**, **redis** and **postgres**:

- **nginx** works as a reverse proxy which serves static files and routes websocket traffic to daphne.
Static files are located in 'nginx/collected_static'.

- The app runs inside **daphne**, which handles websocket requests and communicates with the database.
Websocket connections are set on port 8000.

- **redis** is an in-memory data structure used as a database, cache, and message broker.
  
- **postgres** is a database in which all of our user data is stored.

Most of the settings of these containers are defined as environment variables, which
can be found inside the '.env' file.

Services who do not need to know about each other are isolated through the use of two networks:
- *frontend* (nginx - daphne)
- *backend* (daphne - redis - postgres).

## Requirements

This app runs on docker-compose, which you can install from [here](https://docs.docker.com/compose/install/).

pip requirements can be found in the `requirements.txt` file in the root folder.

You can install them using `pip install -r requirements.txt`.

You don't need to install these in order to run the app, since docker-compose does this for you,
but if you want to contribute to the project this will allow you to run the `manage.py` file for
a better developing, testing and debugging experience.

----------

#### Notes

This app is not prepared to run in real environments (yet). CI/CD is missing, test support is missing, user authentication is missing... you get the point. My only intention was to try out tools such as Django, GitHub, Docker, Nginx, etc. I wanted to see how well I could get the hang of them and how much would it take me to build a functioning app.
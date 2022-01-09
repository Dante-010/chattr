# **Chattr**: A simple live chat website
----------
## Running the app

This app runs on docker-compose, which you can install from [here](https://docs.docker.com/compose/install/).

You can then simply run `docker-compose up` in order to start the app.

### Setting up a superuser and creating a new room

Once all the containers have started, log in to `daphne_production` with the following command:

`docker exec -ti daphne_production /bin/bash`.

You then need to run `python manage.py createsuperuser`.

Finally, go the the `/admin` page, (eg: `localhost/admin`) and create a new room.

## Developing

In order to set up a development environment, you should, first of all, install pip requirements,
found in the `requirements.txt` file in the root folder.

You can do so using `pip install -r requirements.txt`
(I would recommend using a virtual environment).

You should then export the environment variables in the `development.env` and `.env` files. (This allows you to run `manage.py` without starting the docker container.)

There are many ways to do this, but the one I found the most simple and easy was using this 
command:

 `export $(egrep -vh '^#' development.env .env | xargs -d '\n')` ([source](https://stackoverflow.com/questions/19331497/set-environment-variables-from-file-of-key-value-pairs)).

 If you'd like to unset these variables, you can use this command:

 `unset $(egrep -oh '^.+=' development.env .env | xargs -d '=')`

I'd recommend setting up a virtual environment so that these variables are automatically set and unset each time you activate/deactivate it, but there plenty other ways to do this.

### docker-compose layout

This app is composed of four services: **nginx**, **daphne**, **redis** and **postgres**:

- **nginx** works as a reverse proxy which serves static files and routes websocket traffic to daphne.
Static files are located in 'nginx/collected_static'.

- The app runs inside **daphne**, which handles websocket requests and communicates with the database.
Websocket connections are set on port 8000.

- **redis** is an in-memory data structure used as a database, cache, and message broker.
  
- **postgres** is a database in which all data (eg: admin accounts) is stored.

Most of the settings of these containers are defined as environment variables, which
can be found inside the '.env' file.

Services who do not need to know about each other are isolated through the use of two networks:
- *frontend* (nginx - daphne)
- *backend* (daphne - redis - postgres).

----------

#### Notes

This is not meant to be a real and working web application. It's just a simple personal project
with the goal of trying out new technologies and having an insight into the challenges developers
face when carrying out this sort of tasks on a daily basis.

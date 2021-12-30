# **Chattr**: A simple live chat website
----------
## Running the app

This app runs on docker-compose, which you can install from [here](https://docs.docker.com/compose/install/).

You can then simply run `docker-compose up` in order to start the app.

## Developing

In order to set up a development environment, you should install pip requirements,
found in the `requirements.txt` file in the root folder.

You can do so using `pip install -r requirements.txt`
(I would recommend using a virtual environment).

You should then export the environment variables in the `development.env` file.

There are many ways to do this, but the one I found the most simple and easy was this 
command:

 `export $(grep -v '^#' development.env | xargs -d '\n')` ([source](https://stackoverflow.com/questions/19331497/set-environment-variables-from-file-of-key-value-pairs)).

### docker-compose layout

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

----------

#### Notes

This is not meant to be a real and working web application. It's just a simple personal project
with the goal of trying out new technologies and having an insight into the challenges developers
face when carrying out this sort of tasks on a daily basis.

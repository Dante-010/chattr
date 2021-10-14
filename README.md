# Chattr: A simple live chat website

## Requirements

Requirements can be found in the `requirements.txt` file in the root folder.

You can install them using `pip install -r requirements.txt`.

### Running the app

Simply use `docker-compose up` in order to run the app.

### docker-compose layout

This app is composed of four services: nginx, daphne, redis and postgres:

nginx works as a reverse proxy which serves static files and routes websocket traffic to daphne.
Static files are located in 'nginx/collected_static'.

The app runs inside daphne, which handles websocket requests and communicates with the database.
Websocket connections are set on port 8000.

redis is an in-memory data structure used as a database, cache, and message broker.

Environment variables such as the static file location
(STATIC_FILES) should be defined inside the '.env' file.
The database volume is automatically created inside '/var/lib/docker/volumes'.

Services who do not need to know about each other are isolated through the use of two networks,
'frontend' (nginx - daphne), and 'backend' (daphne - redis - postgres).

#### Notes

This app is not prepared to run in real environments. CI/CD is missing, test support is missing, user authentication is missing... you get the point. My only intention was to try out tools such as Django, GitHub, Docker, etc. I wanted to see how well I could get the hang of them and how much would it take me to build a functioning app.
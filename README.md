# Chattr: A simple live chat website

## Requirements

Requirements can be found in the `requirements.txt` file in the root folder.

You can install them using `pip install -r requirements.txt`.

### Running the app

#### Production
If running in production, you can simply use `docker-compose up` and the app will start by itself.

#### Debugging/Developing

Use `python manage.py runserver` in order to start the debugging server.

Remember to run redis with `docker run -p 6379:6379 -d redis:5`.

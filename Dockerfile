FROM python:3.8.7
ENV PYTHONBUFFERED 1

WORKDIR $HOME/code/chattr

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["daphne", "chattr.asgi:application", "-p 8080", "-b 0.0.0.0"]
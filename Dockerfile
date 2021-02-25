FROM python:3.8.7
ENV PYTHONBUFFERED 1
ENV DJANGO_SETTINGS_MODULE chattr.settings

WORKDIR /code/chattr
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
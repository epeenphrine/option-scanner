FROM python:3.6
WORKDIR /app
COPY . /app

RUN pip install Flask gunicorn flask-cors
CMD gunicorn -b 0.0.0.0:5000 -w 8 wsgi:app

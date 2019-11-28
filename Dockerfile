FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# COPY CODE and FipFiles
COPY Pipfile Pipfile.lock /code/
ADD . /app

# RUN apt-get clean && apt-get update
# RUN pip install django
# Install dependencies 
# RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system

FROM python:3.7-alpine
MAINTAINER Agnes Kis

RUN mkdir /app
COPY ./requirements.txt /app/
WORKDIR /app
COPY . /app

RUN apt-get update
RUN apt-get build-dep python-pygame
RUN apt-get install python-dev

RUN pip install -r requirements.txt

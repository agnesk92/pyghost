FROM python:3.7-alpine
MAINTAINER Agnes Kis

RUN mkdir /app
COPY ./requirements.txt /app/
WORKDIR /app
COPY . /app

RUN apk update
RUN apk upgrade
RUN apk build-dep python-pygame
RUN apk install python-dev

RUN pip install -r requirements.txt

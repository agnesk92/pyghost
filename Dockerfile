FROM python:3.7-alpine
MAINTAINER Agnes Kis

RUN mkdir /app
COPY ./requirements.txt /app/
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

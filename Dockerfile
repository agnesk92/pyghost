FROM python:3.7-alpine
MAINTAINER Agnes Kis

RUN mkdir /app
COPY ./requirements.txt /app/
WORKDIR /app
COPY . /app

RUN apk add --update \
    python \
    python-dev \
    build-base \
    build-dep

RUN pip install -r requirements.txt

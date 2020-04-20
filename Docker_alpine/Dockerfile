FROM python:3.7-alpine
MAINTAINER Agnes Kis

RUN mkdir /app
COPY ./requirements.txt /app/
WORKDIR /app
COPY . /app

#RUN sudo apt-get build-dep python-pygame
#RUN sudo apt-get install python-dev

RUN apk add --update \
    python \
    python-dev \
    build-base
RUN python -V
RUN pip install --upgrade pip
# RUN apk add --virtual python-pygame

# RUN apk add python-pygame

RUN pip install -r requirements.txt

FROM ubuntu:18.04
MAINTAINER Agnes Kis

# Set up Bionic
RUN apt-get update && apt-get upgrade -y
RUN apt-get install vim -y

# For x11
RUN apt-get install -qqy x11-apps

# Dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install tzdata libssl-dev openssl zlib1g-dev
RUN apt-get -y install build-essential checkinstall wget screenfetch
RUN apt-get -y install libffi-dev curl libsqlite3-dev

# Get Python 3.7.5
WORKDIR /usr/src
RUN wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
RUN tar xzf Python-3.7.5.tgz
WORKDIR /usr/src/Python-3.7.5
RUN ./configure
RUN make altinstall

# Upgrade pip
RUN pip3.7 install --upgrade pip

# Test Python install
RUN python3.7 -V
RUN pip3.7 -V

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip3.7 install -r requirements.txt

# Change from root user for security reasons
#RUN useradd -m -U -s /bin/bash pygame
#USER pygame

FROM ubuntu:18.04
MAINTAINER Agnes Kis

# Set up Bionic
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    tzdata \
    libssl-dev \
    openssl \
    zlib1g-dev \
    build-essential \
    checkinstall \
    libffi-dev \
    libsqlite3-dev \
    screenfetch \
    vim \
    curl

# For x11
RUN apt-get install -qqy x11-apps

# Get Python 3.7
RUN apt-get install python3.7 && python3.7 -V

# Upgrade pip
RUN pip3.7 install --upgrade pip && pip3.7 -V

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip3.7 install -r requirements.txt

# Change from root user for security reasons
RUN useradd -r -U -s /bin/bash pygameuser
RUN mkdir /shared && chown -R pygameuser:pygameuser /shared /app
USER pygameuser

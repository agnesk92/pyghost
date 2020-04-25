FROM ubuntu:18.04
MAINTAINER Agnes Kis

# todo: build more images for subtasks
# todo: cis: cisecurity.org/benchmark/docker/

# Set up Bionic
# todo: alpine linux instead?
RUN apt-get update && apt-get upgrade -y
RUN apt-get install vim -y

# For x11
RUN apt-get install -qqy x11-apps

# Get Python 3.7.5
# ref: https://askubuntu.com/questions/682869/how-do-i-install-a-different-python-version-using-apt-get
#RUN apt-get install -y build-essential checkinstall
#RUN apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev
#RUN apt-get install -y tk-dev libsqlite3-dev libgdbm-dev libc6-dev libbz2-dev

# Dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install tzdata
#8 (europe), 11 (bp)
RUN apt-get install -y libssl-dev openssl zlib1g-dev
RUN apt-get install -y build-essential checkinstall
RUN apt-get install -y wget
RUN apt-get install -y screenfetch

# Get the spec. Python version
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
RUN useradd -m -U -s /bin/bash pygame
USER pygame

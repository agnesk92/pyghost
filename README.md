[![Python 3](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/release/python-3/)
[![Python 3.7.5](https://img.shields.io/badge/python-3.7.5-blue.svg)](https://www.python.org/downloads/release/python-375/)

[![Build Status](https://travis-ci.org/agnesk92/pyGhost.svg?branch=master)](https://travis-ci.org/agnesk92/pyGhost)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1caa85475416eb3c7840/test_coverage)](https://codeclimate.com/github/agnesk92/pyGhost/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/1caa85475416eb3c7840/maintainability)](https://codeclimate.com/github/agnesk92/pyGhost/maintainability)
[![codecov](https://codecov.io/gh/agnesk92/pyGhost/branch/master/graph/badge.svg)](https://codecov.io/gh/agnesk92/pyGhost)

# PyGhost :ghost:

## About.. 

A simple :video_game: to experiment with pygame & :whale2: & codecov and other tools.

## Contribution

### Environment

Set up the env for docker.
```bash 
# Run the Docker daemon
sudo systemctl start docker

# Create the docker group and add yourself - you'll need to re-login for this to take effect
sudo groupadd docker
sudo usermod -aG docker $USER 
```

#### Ubuntu

```bash 
# Build dockerfile
docker build . -t pyghost-ubuntu:v1.0
# Clean build
docker build --no-cache . -t pyghost-ubuntu:v1.0

# Depending on the OS you are using sh or bash ..
docker run -it pyghost-ubuntu:v1.0 sh
docker run -it pyghost-ubuntu:v1.0 bash

# Linux setups - might need for host display access
# If needed for display env var: ip route list | grep default
xhost +local:docker

# For GUI apps, use the host's X11 server and DISPLAY
# https://stackoverflow.com/questions/28392949/running-chromium-inside-docker-gtk-cannot-open-display-0
docker run --env DISPLAY=unix$DISPLAY --volume $XAUTH:/root/.Xauthority --volume /tmp/.X11-unix:/tmp/.X11-unix --rm -it pyghost-ubuntu:v1.0 bash
docker run --env DISPLAY=unix$DISPLAY --volume $XAUTH:/root/.Xauthority --volume /tmp/.X11-unix:/tmp/.X11-unix --volume `pwd`:/app --rm -it pyghost-ubuntu:v1.0 bash


docker exec -it pyghost-ubuntu:v1.0 bash
```

## Code Metrics

[![codecov](https://codecov.io/gh/agnesk92/pyGhost/commit/ea156d5005ac12181f981516b4fbaee7c5be5842/graphs/sunburst.svg)](https://codecov.io/gh/agnesk92/pyGhost)

## License

The code is available under the [Apache License](LICENSE).

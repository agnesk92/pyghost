FROM agnesk92/pygame-base:v2.1
MAINTAINER Agnes Kis

RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

# Change from root user for security reasons
RUN useradd -r -U -s /bin/bash pygameuser && usermod -u 1000 pygameuser
RUN mkdir /shared && chown -R pygameuser:pygameuser /app /shared
USER pygameuser

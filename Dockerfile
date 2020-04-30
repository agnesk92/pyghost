FROM agnesk92/pygame-base:v2.1
MAINTAINER Agnes Kis

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# Change from root user for security reasons
RUN useradd -r -U -s /bin/bash pygameuser
RUN mkdir /shared && chown -R pygameuser:pygameuser /shared /app
USER pygameuser

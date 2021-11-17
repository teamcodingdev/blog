FROM python:3.7.5-slim-buster
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV prod
ENV DOCKER_CONTAINER 1

# WORKDIR /opt/oracle
# RUN apt-get update && apt-get install -y libaio1 wget unzip \
#     && wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip \
#     && unzip instantclient-basiclite-linuxx64.zip \
#     && rm -f instantclient-basiclite-linuxx64.zip \
#     && cd /opt/oracle/instantclient* \
#     && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
#     && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
#     && ldconfig

RUN mkdir /src
RUN mkdir /env_root
RUN mkdir /env_root/static_root
RUN mkdir /env_root/media_root

WORKDIR /src
COPY . /src/

# install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev \
#     && apk add libaio-dev libnsl-dev gcompat \
#     && rm -rf /var/cache/apk/*

RUN pip install -U pip && pip install -r requirements.txt

FROM ubuntu:16.04

MAINTAINER Jarrekk me@jarrekk.com

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    git \
    python \
    python-dev \
    python-setuptools \
    python-pip \
    uwsgi-plugin-python && \
    pip install -U pip setuptools && \
    rm -rf /var/lib/apt/lists/*

ADD ./ztool-backhend-mongo/jalpc-docker.ini /tmp/jalpc-docker.ini
ADD ./ztool-backhend-mongo/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
CMD uwsgi /tmp/jalpc-docker.ini

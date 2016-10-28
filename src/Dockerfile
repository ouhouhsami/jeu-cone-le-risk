FROM python:2.7

MAINTAINER Samuel Goldszmidt

ENV PYTHONUNBUFFERED 1

RUN apt-get update

# gettext
RUN apt-get install -y gettext

# pip
RUN pip install pip

# source code dependancies
WORKDIR /
RUN mkdir python-dep
ADD ./requirements.txt /python-dep/
WORKDIR /python-dep
RUN pip install -r requirements.txt
RUN rm requirements.txt
WORKDIR /

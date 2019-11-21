FROM python:3.7
ENV PYTHONUNBUFFERED 1

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools

RUN mkdir /webapps
WORKDIR /webapps
COPY requirements.txt /webapps/
RUN pip install -r /webapps/requirements.txt
#ADD . /webapps/

# Django service
EXPOSE 8000

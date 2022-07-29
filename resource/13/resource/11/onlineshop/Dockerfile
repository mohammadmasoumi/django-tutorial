FROM dockerhub.ir/python:3.8

COPY / /onlineshop/

WORKDIR onlineshop

RUN apt-get -y update \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt

EXPOSE 8000
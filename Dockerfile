# FROM ubuntu:20.04
# RUN apt-get update -y
# RUN apt-get install python -y
# RUN apt-get install software-properties-common -y
# RUN apt-add-repository universe -y
# RUN apt-get update -y
# RUN apt-get install python3-pip -y
# RUN pip3 install flask
# ENV FLASK_APP /home/lucas/Documentos/weather/src/app.py
# COPY app.py /home/lucas/Documentos/weather/src/app.py
# ENTRYPOINT flask run

FROM python:3-alpine

RUN apk add --virtual .build-dependencies \ 
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev

RUN apk add --no-cache pcre

WORKDIR /src
COPY /src /src
COPY ./requirements.txt /src

RUN pip install -r /src/requirements.txt

RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

EXPOSE 5000
CMD ["uwsgi", "--ini", "/src/wsgi.ini"]
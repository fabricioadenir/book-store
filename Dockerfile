FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /book-store
WORKDIR /book-store
ADD requirements.txt /book-store/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /book-store/

# # pull official base image
# FROM python:3.8.0-alpine

# # set work directory
# WORKDIR /usr/src/book-store

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # install psycopg2 dependencies
# RUN apk fix
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev

# # install dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt /usr/src/book-store/requirements.txt
# RUN pip install -r requirements.txt

# # copy project
# COPY . /usr/src/book-store/
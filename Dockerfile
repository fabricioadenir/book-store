FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /book-store
WORKDIR /book-store
ADD requirements.txt /book-store/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /book-store/

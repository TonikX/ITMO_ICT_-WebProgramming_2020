FROM python:3.7-alpine
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

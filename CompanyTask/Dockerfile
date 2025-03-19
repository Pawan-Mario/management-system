FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
RUN addgroup --gid 1000 celeryuser && \
    adduser --uid 1000 --gid 1000 --disabled-password celeryuser
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

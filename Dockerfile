# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -y install g++
RUN pip3 install -r requirements.txt
COPY . .
CMD ["sh", "-c","/ComEnergyForecast;","python", "flask_api_forecast.py","--host=0.0.0.0"]
FROM python:3.8-slim

WORKDIR /opt/chatbot

RUN apt update && apt install -y -q python3-dev python3-pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

FROM python:3.11-slim


RUN apt-get update -y && apt install python3-bs4 -y

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /src
COPY ./src /src
#ENV PYTHONPATH=/src

WORKDIR /src/

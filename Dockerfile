FROM python:3.11-slim

WORKDIR /src/

RUN apt-get update -y && apt install python3-bs4 -y

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./src /src
ENV PYTHONPATH=/src


CMD ["uvicorn main:app --reload --host 0.0.0.0 --port 7777"]

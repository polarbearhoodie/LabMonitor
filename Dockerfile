FROM ubuntu:jammy
WORKDIR /usr/src/app

RUN apt update
RUN apt install graphicsmagick -y
RUN apt install python3 python3-pip -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn main:app --bind=0.0.0.0:8000
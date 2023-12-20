FROM ubuntu:jammy
WORKDIR /usr/src/app

RUN apt update

COPY . .
RUN apt install python3 python3-pip -y
RUN pip install -r requirements.txt

RUN apt install graphicsmagick -y

CMD python3 web.py &
CMD gunicorn main:app
FROM python:3.12
LABEL authors="David Smith <david@xterm.me>"

ENV SLACK_BOT_TOKEN = ""

RUN mkdir /opt/app


COPY requirements.txt /opt/app
RUN cd /opt/app && pip3 install -r requirements.txt

COPY src /opt/app

WORKDIR /opt/app

ENTRYPOINT ["python3", "main.py"]
FROM python:3.8-slim

MAINTAINER chaos:life0531@foxmail.com

RUN mkdir /root/chatAuthBot

RUN mkdir /root/chatAuthBot/log

ADD . /root/chatAuthBot

WORKDIR /root/chatAuthBot

RUN pip3 install -r requirements.txt -i https://pypi.douban.com/simple/

CMD ["python3", "run.py"]

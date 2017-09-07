FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python python-pip python-dev build-essential
RUN pip install --upgrade pip
#WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY server.py /run/server.py
CMD [ "python", "/run/server.py" ]

EXPOSE 12345

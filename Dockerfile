FROM ubuntu:22.04

ENV TZ='Asia/Taipei'
ENV DEBIAN_FRONTEND=noninteractive

# 更新 apt
RUN apt update -y
RUN apt upgrade -y

# 安裝及更新pip
RUN apt install -y python3-pip
RUN pip install --upgrade pip

WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN pip install -U -r requirements.txt
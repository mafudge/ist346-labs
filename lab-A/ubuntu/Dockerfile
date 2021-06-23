FROM ubuntu:18.04

LABEL  image ist346/ubuntu

# Base Setup
RUN apt-get update

RUN apt-get install -y \
        build-essential \
        dialog \
        apt-utils 

RUN apt-get install -y \
        curl \
        libfreetype6-dev \
        libzmq3-dev \
        pkg-config \
        net-tools \
        iputils-ping \ 
        inetutils-traceroute\
        dnsutils \ 
        iproute2 \
        nano \
        lynx \
        openssh-client \
        telnet \
        sudo \
        nmap \
        ftp \
        wget \
        rsync \
        software-properties-common \
        unzip

RUN apt-get install -y git 

RUN apt-get install -y wget

RUN apt-get install -y \
        python3 \
        python3-dev \
        python3-pip \
        python3-setuptools

RUN apt-get upgrade -y
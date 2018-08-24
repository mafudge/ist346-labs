FROM ubuntu:16.04

 
MAINTAINER  Michael Fudge <mafudge@syr.edu>

# Base Setup
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        apt-utils

# Every image needs these!
RUN apt-get install -y --no-install-recommends \
        curl \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        net-tools \
        iputils-ping \ 
        inetutils-traceroute\
        dnsutils \ 
        nano \
        lynx \
        openssh-client \
        telnet \
        sudo \
        nmap \
        git \
        ftp \
        wget \
        rsync \
        software-properties-common \
        unzip \
        && \
    apt-get clean 

#RUN useradd -md /home/tommy -p IST346!
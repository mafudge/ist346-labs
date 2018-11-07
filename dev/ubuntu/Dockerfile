FROM ubuntu:16.04

# Let's give credit! Most of this script comes from:
# https://github.com/dash00/tensorflow-python3-jupyter
# Jeremy Coatelen <dash0@protonmail.com>
 
MAINTAINER  Michael Fudge <mafudge@syr.edu>

# Pick up some TF dependencies
RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y --no-install-recommends \
        build-essential \
        apt-utils

RUN apt-get install -y --no-install-recommends \
        apt-utils \ 
        man \
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
        rsync \
        software-properties-common \
        unzip \
        && \
    apt-get clean 

#        python3 \
#        python3-dev \
#        python3-pip \
#        python3-setuptools \


# RUN git clone git://github.com/scottsimpson/commandlinebasics
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

# Upgrade Pip
#RUN pip3 --no-cache-dir install  --upgrade pip

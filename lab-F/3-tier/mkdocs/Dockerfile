FROM ist346/ubuntu

RUN apt-get update && apt-get upgrade -y python3 python3-pip gcc
#RUN pip3 install --upgrade pip
RUN pip3 install wheel 
RUN pip3 install mkdocs==1.0.4 mkdocs-material 
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /docs

VOLUME /docs
EXPOSE 8000

FROM ist346/ubuntu

RUN apt-get update && apt-get install -y python3 python3-pip gcc
RUN pip3 install --upgrade pip
RUN pip3 install wheel
RUN pip3 install --upgrade mkdocs mkdocs-material tornado==5.0
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /docs

VOLUME /docs
EXPOSE 8000

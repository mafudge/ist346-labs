FROM ubuntu:16.04
RUN apt-get update &&  apt-get install -y python3 python3-dev python3-pip 
RUN pip3 install flask 
WORKDIR /app
COPY app.py /app
EXPOSE 8080
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
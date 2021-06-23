FROM ist346/ubuntu:latest
LABEL image ist346/flaskapp
#RUN apt-get update &&  apt-get install -y python3 python3-dev python3-pip 
RUN pip3 install flask 
WORKDIR /app
COPY . /app
EXPOSE 8080
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
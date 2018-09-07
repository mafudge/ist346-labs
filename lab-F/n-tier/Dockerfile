FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get install default-libmysqlclient-dev
#RUN apt-get install libmysqlclient-dev # nao sei pq mudou :D
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
# ADD . /code/# ADD . /code/

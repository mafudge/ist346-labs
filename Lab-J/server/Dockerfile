# Lab01 - Server Runs sshd & nginx

FROM ubuntu:latest 
 
MAINTAINER  Michael Fudge <mafudge@syr.edu>

# Install Stuff
RUN apt-get update && apt-get install -y openssh-server nano 
RUN mkdir -p /var/run/sshd 

# SSH Confing of root password
RUN echo 'root:IST346' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# Build Script, expose ports, run!
#RUN echo '#!/bin/bash \n/usr/sbin/sshd \n/usr/sbin/nginx \nwhile sleep 60; do \n   echo "test"\ndone' > /start.sh
COPY start.sh /
EXPOSE 22
CMD ["/bin/bash", "/start.sh"]
# Server Runs sshd & nginx
FROM ist346/ubuntu:latest 
 
LABEL image ist346/server

# Install Stuff
RUN apt-get install -y openssh-server nginx 
RUN mkdir -p /var/run/sshd && mkdir -p /var/run/nginx

# SSH Confing of root password
RUN echo 'root:IST346' | chpasswd
#RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# NGINX
COPY index.html /var/www/html/

# Build Script, expose ports, run!
#RUN echo '#!/bin/bash \n/usr/sbin/sshd \n/usr/sbin/nginx \nwhile sleep 60; do \n   echo "test"\ndone' > /start.sh
COPY start.sh /
EXPOSE 80 22
CMD ["/bin/bash", "/start.sh"]
# Lab02 - Linux Commands

FROM ist346/ubuntu:latest 
 
LABEL image ist346/workstation:latest

# Install Stuff
#RUN apt-get update && apt-get install -y openssh-server nginx 
#RUN mkdir -p /var/run/sshd && mkdir -p /var/run/nginx

# Set Root Password
RUN echo 'root:IST346' | chpasswd
RUN useradd scott -md /home/scott -s /bin/bash
RUN echo 'scott:IST346' | chpasswd 
RUN cp /root/.bashrc /home/scott/.bashrc && chown scott:scott /home/scott/.bashrc
RUN mkdir /home/scott/Documents
RUN git clone git://github.com/scottsimpson/commandlinebasics /home/scott/Documents
RUN chown -R scott:scott /home/scott 

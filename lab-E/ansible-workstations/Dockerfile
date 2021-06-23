# ansible workstation 
FROM ist346/ubuntu:latest 
 
LABEL image ist346/ansible-workstation:latest

# Install Stuff
RUN apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd 

# SSH Confing of root password
RUN echo 'root:IST346' | chpasswd
#RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile


# Build Script, expose ports, run!
COPY start.sh /
EXPOSE 22
CMD ["/bin/bash", "/start.sh"]
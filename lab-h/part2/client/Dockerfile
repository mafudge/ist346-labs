FROM ist346/ubuntu-16.04-base:latest 

RUN apt-get -y update

# Install requirements, cifs utils allows us to mount the folder
RUN apt-get install -y smbclient nano cifs-utils openssh-server

# RUN dpkg-reconfigure ldap-auth-config

RUN echo 'root:IST346' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22

RUN mkdir -p /var/run/sshd

# Build Script, expose ports, run!
COPY start.sh /

CMD ["/bin/bash", "/start.sh"]

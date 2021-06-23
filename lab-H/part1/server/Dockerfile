FROM ist346/ubuntu:latest

RUN apt-get install -y samba 

# Comments
# RUN useradd ist-t-user --shell /bin/false

# RUN (echo "password"; sleep 1; echo "password" ) | smbpasswd -a ist-t-user

# RUN mkdir -p /home/ist-t-user/share
# RUN chown :ist-t-user /home/ist-t-user
# RUN chown ist-t-user:ist-t-user /home/ist-t-user/share

# RUN echo $' \n\
# [myshare] \n\
# path = /home/ist-t-user/share \n\
# valid users = ist-t-user \n\
# available = yes \n\
# browsable = yes \n\
# public = yes \n\
# writable = yes \n\
# read only = no \n\
# ' >> /etc/samba/smb.conf

EXPOSE 137/udp 138/udp 139 445

# keep the container running
ENTRYPOINT tail -f /dev/null

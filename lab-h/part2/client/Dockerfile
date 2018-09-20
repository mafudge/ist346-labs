FROM ubuntu:16.04

RUN apt-get -y update

# Install requirements, cifs utils allows us to mount the folder
RUN apt-get install -y smbclient nano cifs-utils

#mount -t cifs -o user=ist-t-user //server/myshare /mnt/myshare

ENTRYPOINT tail -f /dev/null

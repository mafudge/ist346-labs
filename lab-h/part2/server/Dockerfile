FROM ubuntu:16.04

RUN apt-get -y update
RUN apt-get install -y samba nano libnss-ldap

RUN smbpasswd -w JonSn0w

COPY .start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 137/udp 138/udp 139 445

# keep the container running
ENTRYPOINT start.sh

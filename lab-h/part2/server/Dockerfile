FROM ubuntu:16.04

RUN apt-get -y update
RUN apt-get install -y samba nano


EXPOSE 137/udp 138/udp 139 445

# keep the container running
ENTRYPOINT tail -f /dev/null

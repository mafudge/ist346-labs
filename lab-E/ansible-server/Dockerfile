# ansible server

FROM ist346/server:latest 
 
LABEL image ist346/ansible-server:latest

# Install Stuff
RUN apt-add-repository -y ppa:ansible/ansible
RUN apt-get update && apt-get install -y ansible 


EXPOSE 22
CMD ["/bin/bash", "/start.sh"]
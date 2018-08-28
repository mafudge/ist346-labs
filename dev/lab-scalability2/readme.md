Based on 
https://medium.com/@ruanbekker/setup-your-first-python-flask-web-application-on-docker-swarm-aecf7c5f4cc3


first without scalability

`docker-compose up -d`


With swarm

`docker swarm init`

Deploy the stack

`docker stack deploy --compose-file .\flask-swarm.yml flaskapps --with-registry-auth`


Is it running?

`docker stack ps flaskapps`

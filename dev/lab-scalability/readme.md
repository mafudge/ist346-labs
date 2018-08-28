Based on 
https://medium.com/@nirgn/load-balancing-applications-with-haproxy-and-docker-d719b7c5b231


`docker-compose `


setup to ensure compose can access the docker engine


`$Env:COMPOSE_CONVERT_WINDOWS_PATHS=1`

Checking on the status of haproxy

http://localhost:1936

user: stats
pass: stats

witness the round-robin effect in all its gory-glory!


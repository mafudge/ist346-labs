#!/bin/bash

while true; do 
    curl -d -m 3 admin:password http://webserver/admin
    sleep 1
    curl -d -m 3 john:P@ssword123 http://webserver/user/login
    sleep 1
    curl -d -m 3 john@gmail.com:Password http://webserver/user/login
    sleep 1
    curl -d -m 3 administrator:password123 http://webserver/admin
    sleep 1
done
#!/bin/bash

while true; do 
    curl -d -m 3 admin:password http://172.44.1.102/admin
    sleep 1
    curl -d -m 3 john:P@ssword123 http://172.44.1.102/user/login
    sleep 1
    curl -d -m 3 john@gmail.com:Password http://172.44.1.102/user/login
    sleep 1
    curl -d -m 3 administrator:password123 http://172.44.1.102/admin
    sleep 1
done
#! /bin/bash

sudo docker login
sudo docker rmi $(sudo docker images -aq)
sudo docker-compose build --parallel
sudo docker-compose push


#! /bin/bash
  
cd /home/jenkins/.jenkins/workspace/rap-name-generator/

sudo docker-compose build --parallel

sudo docker-compose push

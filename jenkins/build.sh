#! /bin/bash

. /home/jenkins/.jenkins/workspace/rap-name-generator/venv/bin/activate

export MY_SECRET_KEY=$MY_SECRET_KEY
export DB_USERNAME=$DB_USERNAME
export DB_PASSWORD=$DB_PASSWORD

cd /home/jenkins/.jenkins/workspace/rap-name-generator/

sudo docker-compose build --parallel

sudo docker-compose push

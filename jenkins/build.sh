#! /bin/bash
  
. /home/jenkins/.jenkins/workspace/rap-name-generator/venv/bin/activate
export MY_SECRET_KEY='aeiou'
export DB_USERNAME='callumgoodley'
export DB_PASSWORD='root'
cd /home/jenkins/.jenkins/workspace/rap-name-generator/
sudo docker-compose build --parallel

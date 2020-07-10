#! /bin/bash

. /home/jenkins/.jenkins/workspace/rap-name-generator/venv/bin/activate

export MY_SECRET_KEY=$MY_SECRET_KEY
export DB_USERNAME=$DB_USERNAME
export DB_PASSWORD=$DB_PASSWORD

cd /home/jenkins/.jenkins/workspace/rap-name-generator/

sudo docker-compose build --parallel
sudo docker rmi $(sudo docker images -aq)
#sudo docker login -u $DH_USERNAME -p $DH_PASSWORD docker.io
#sudo docker-compose build callumgoodley/service1 + ":$BUILD_NUMBER"
#sudo docker-compose build callumgoodley/service2 + ":$BUILD_NUMBER"
#sudo docker-compose build callumgoodley/service3 + ":$BUILD_NUMBER"
#sudo docker-compose build callumgoodley/service4 + ":$BUILD_NUMBER"
#sudo docker-compose build callumgoodley/rapper_name_mysql + ":$BUILD_NUMBER"

#sudo docker-compose push

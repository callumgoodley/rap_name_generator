#! /bin/bash

. /home/jenkins/.jenkins/workspace/rap-name-generator/venv/bin/activate

export MY_SECRET_KEY=$MY_SECRET_KEY
export DB_USERNAME=$DB_USERNAME
export DB_PASSWORD=$DB_PASSWORD

sudo docker login
sudo docker rmi $(sudo docker images -aq)
sudo docker-compose build --parallel
sudo docker-compose push


#sudo docker push "callumgoodley/service1:$BUILD_NUMBER"
#sudo docker push "callumgoodley/service2:$BUILD_NUMBER"
#sudo docker push "callumgoodley/service3:$BUILD_NUMBER"
#sudo docker push "callumgoodley/service4:$BUILD_NUMBER"
#sudo docker push "callumgoodley/rapper_name_mysql:$BUILD_NUMBER"

#! /bin/bash

sudo docker login
sudo docker rmi $(sudo docker images -aq)
sudo docker-compose build --parallel
#sudo docker-compose push


sudo docker push "callumgoodley/service1:$BUILD_NUMBER"
#sudo docker push "callumgoodley/service2:$BUILD_NUMBER"
#sudo docker push "callumgoodley/service3:$BUILD_NUMBER"
#sudo docker push "callumgoodley/service4:$BUILD_NUMBER"
#sudo docker push "callumgoodley/rapper_name_mysql:$BUILD_NUMBER"

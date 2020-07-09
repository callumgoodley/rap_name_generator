#! /bin/bash
export MY_SECRET_KEY='aeiou'
export DB_USERNAME='root'
export DB_PASSWORD='root'

cd /home/jenkins/.jenkins/workspace/rap-name-generator/

sudo docker stop mysql-test
sudo docker rm mysql-test
sudo docker run -d -p 3306:3306 --name mysql-test mysql -e MYSQL_USER='callumgoodley' MYSQL_PASSWORD='root' -e MYSQL_ROOT_PASSWORD='root' -e MYSQL_DATABASE=test
cd /home/jenkins/.jenkins/workspace/rap-name-generator/service1/testing
python -m pytest
sudo docker stop mysql-test
sudo docker rm mysql-test

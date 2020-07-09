#! /bin/bash

. /home/jenkins/.jenkins/workspace/rap-name-generator/venv/bin/activate

export MY_SECRET_KEY='aeiou'
export DB_USERNAME='callumgoodley'
export DB_PASSWORD='root'

cd /home/jenkins/.jenkins/workspace/rap-name-generator/

cd /home/jenkins/.jenkins/workspace/rap-name-generator/service1/testing
python -m pytest --cov application

cd /home/jenkins/.jenkins/workspace/rap-name-generator/service2/testing
python -m pytest --cov application

cd /home/jenkins/.jenkins/workspace/rap-name-generator/service3/testing
python -m pytest --cov application

cd /home/jenkins/.jenkins/workspace/rap-name-generator/service4/testing
python -m pytest --cov application

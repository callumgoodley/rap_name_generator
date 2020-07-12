#! /bin/bash


cd /home/jenkins/.jenkins/workspace/rap-name-generator/service1/testing
python -m pytest --cov application

cd /home/jenkins/.jenkins/workspace/rap-name-generator/service2/testing
python -m pytest --cov application

cd /home/jenkins/.jenkins/workspace/rap-name-generator/service3/testing
python -m pytest --cov application

cd /home/jenkins/.jenkins/workspace/rap-name-generator/service4/testing
python -m pytest --cov application

#! /bin/bash

cd ~/.jenkins/workspace/rap_name_generator_final/service1/testing
python -m pytest --cov application

cd ~/.jenkins/workspace/rap_name_generator_final/service2/testing
python -m pytest --cov application

cd ~/.jenkins/workspace/rap_name_generator_final/service3/testing
python -m pytest --cov application

cd ~/.jenkins/workspace/rap_name_generator_final/service4/testing
python -m pytest --cov application

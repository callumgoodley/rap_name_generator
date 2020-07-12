#! /bin/bash

cd ./service1/testing
python -m pytest --cov application

cd ./service2/testing
python -m pytest --cov application

cd ./service3/testing
python -m pytest --cov application

cd ./service4/testing
python -m pytest --cov application

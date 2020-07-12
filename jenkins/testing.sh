#! /bin/bash

python -m pytest --cov ./service1/application

python -m pytest --cov ./service2/application

python -m pytest --cov ./service3/application

python -m pytest --cov ./service4/application

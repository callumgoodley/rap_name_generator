#! /bin/bash

cd /home/callumgoodley/rap_name_generator/service1/testing
python -m pytest --cov application
cd /home/callumgoodley/rap_name_generator/service2/testing
python -m pytest --cov application
cd /home/callumgoodley/rap_name_generator/service3/testing
python -m pytest --cov application
cd /home/callumgoodley/rap_name_generator/service4/testing
python -m pytest --cov application

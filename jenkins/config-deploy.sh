#! /bin/bash

cd /home/jenkins/.jenkins/workspace/rap-name-generator/configure

/home/jenkins/.local/bin/ansible-playbook -v -i 34.105.252.67, --inventory=inventory playbook.yaml

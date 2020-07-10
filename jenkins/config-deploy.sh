#! /bin/bash


cp /home/jenkins/.local/bin/ansible-playbook /home/jenkins/usr/bin/ansible-playbook
whoami
#/home/callumgoodley/.local/bin/ansible-playbook -v -i 34.105.252.67, --inventory=inventory playbook.yaml
/home/jenkins/.local/bin/ansible-playbook -v -i 34.105.252.67, --inventory=inventory playbook.yaml

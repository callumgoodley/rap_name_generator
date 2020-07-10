#! /bin/bash


ln -s /home/jenkins/.local/bin/ansible-playbook /usr/bin/ansible-playbook
#/home/callumgoodley/.local/bin/ansible-playbook -v -i 34.105.252.67, --inventory=inventory playbook.yaml
/home/jenkins/.local/bin/ansible-playbook -v -i 34.105.252.67, --inventory=inventory playbook.yaml

#! /bin/bash
ssh callumgoodley@rap-manager3 << EOF
sudo docker container stop $(docker container ls –aq)
sudo docker container rm $(docker container ls –aq)
docker system prune
EOF
/home/jenkins/.local/bin/ansible-playbook -i /home/callumgoodley/rap_name_generator/configure/inventory /home/callumgoodley/rap_name_generator/configure/playbook.yaml


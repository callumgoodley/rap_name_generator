#! /bin/bash
/home/jenkins/.local/bin/ansible-playbook -i /home/callumgoodley/rap_name_generator/configure/inventory /home/callumgoodley/rap_name_generator/configure/playbook.yaml
ssh callumgoodley@rap-manager << EOF
sudo docker service update rapstack_mysql=3 rapstack_service1=3 rapstack_service2=3 rapstack_service3=3 rapstack_service4=3
EOF


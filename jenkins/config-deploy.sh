#! /bin/bash
/home/jenkins/.local/bin/ansible-playbook -i /home/callumgoodley/rap_name_generator/configure/inventory /home/callumgoodley/rap_name_generator/configure/playbook.yaml
ssh callumgoodley@rap-manager << EOF
sudo docker service scale rapstack_mysql=5 rapstack_service1=5 rapstack_service2=5 rapstack_service3=5 rapstack_service4=5
EOF


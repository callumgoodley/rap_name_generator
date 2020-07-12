#! /bin/bash
/home/jenkins/.local/bin/ansible-playbook -i /home/callumgoodley/rap_name_generator/configure/inventory /home/callumgoodley/rap_name_generator/configure/playbook.yaml
ssh callumgoodley@rap-manager << EOF
sudo docker service update --replicas 3 rapstack_mysql
EOF

ssh callumgoodley@rap-manager << EOF
sudo docker service update -–replicas 3 rapstack_service1
EOF
ssh callumgoodley@rap-manager << EOF
sudo docker service update -–replicas 3 rapstack_service2
EOF
ssh callumgoodley@rap-manager << EOF
sudo docker service update -–replicas 3 rapstack_service3
EOF
ssh callumgoodley@rap-manager << EOF
sudo docker service update -–replicas 3 rapstack_service4
EOF

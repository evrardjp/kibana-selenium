#! /bin/bash

password="$(grep -R "kibana_password" /etc/openstack_deploy/user_extras_secrets.yml)"
external_lb_vip_address="$(grep -R "external_lb_vip_address" /opt/rpc-openstack/jenkins-oa/inventory/group_vars/qe-iad3-lab03.yml)"

echo "kibana:" >> ryan.configuration
echo "  ${password}" >> ryan.configuration
echo "${external_lb_vip_address}" >> ryan.configuration
echo "  username: kibana" >> ryan.configuration
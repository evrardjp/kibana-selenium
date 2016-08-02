from subprocess import call

host = call(["hostname"])

if "qe-iad3-3" in host:
    h = "qe-iad3-lab03"
elif "qe-iad3-2" in host:
    h = "qe-iad3-lab02"
else:
    raise Exception("conf-gen.py is only used to configure for iad3-2 and iad3-3 at this time.")

inv = "/opt/rpc-openstack/jenkins-oa/inventory/group_vars/{0}.yml".format(h)
elva = call(["grep", "-R", "external_lb_vip_address", inv])
print elva
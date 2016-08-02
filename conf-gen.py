import subprocess


def get_external_lb_vip():
    host = subprocess.check_output(["hostname"])
    if "qe-iad3-3" in host:
        h = "qe-iad3-lab03"
    elif "qe-iad3-2" in host:
        h = "qe-iad3-lab02"
    else:
        raise Exception("conf-gen.py is used to configure for iad3-2 and iad3-3.")

    inv = "/opt/rpc-openstack/jenkins-oa/inventory/group_vars/{0}.yml".format(h)
    elva = subprocess.check_output(["grep", "-R", "external_lb_vip_address", inv])
    return elva


def get_password():
    password = subprocess.check_output([
        "grep", "-R", "kibana_password",
        "/etc/openstack_deploy/user_extras_secrets.yml"])
    return password

vip = get_external_lb_vip()
pas = get_password()

f = open('/opt/kibana-selenium/config/app.yaml', 'w')
f.write("kibana:\n")
f.close()
append = open('/opt/kibana-selenium/config/app.yaml', 'a')
append.write("  username: kibana\n")
append.write("  "+pas)
append.write(vip)
append.close()
print "Config file generated into config/app.yaml"

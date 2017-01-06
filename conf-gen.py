import argparse
import subprocess


def get_external_lb_vip(file_location=None):
    host = subprocess.check_output(["hostname"])
    if file_location:
        fi = file_location
    elif "qe-iad3-3" in host:
        h = "qe-iad3-lab03"
        fi = "/opt/rpc-openstack/jenkins-oa/inventory/group_vars/" \
             "{0}.yml".format(h)
    elif "qe-iad3-2" in host:
        fi = "/etc/openstack_deploy/openstack_user_config.yml"
    else:
        raise Exception("conf-gen.py is for iad3-2 and iad3-3.")

    elva_line = subprocess.check_output([
        "grep", "-R", "external_lb_vip_address", fi])
    elva = elva_line.split(":", 1)[1].strip()
    return elva


def get_password(file_location=None):
    file_location = (file_location
                     or "/etc/openstack_deploy/user_extras_secrets.yml")
    password_line = subprocess.check_output([
        "grep", "-R", "kibana_password", file_location])
    password = password_line.split(":", 1)[1].strip()
    return password

if __name__ == '__main__':
    description = "Script to generate config file"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--password-file")
    parser.add_argument("--vip-file")
    parser.add_argument("--password")
    parser.add_argument("--vip")
    args = parser.parse_args()

    vip = args.vip or get_external_lb_vip(args.vip_file)
    pas = args.password or get_password(args.password_file)

    f = open('config/app.yaml', 'w+')
    f.write("kibana:\n")
    f.close()
    append = open('config/app.yaml', 'a')
    append.write("  username: kibana\n")
    append.write("  kibana_password: {0}\n".format(pas))
    append.write("  external_lb_vip_address: {0}".format(vip))
    append.close()
    print "Config file generated into config/app.yaml"

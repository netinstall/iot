import paramiko

def get_ssh_connect(ssh_host, ssh_user, ssh_password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, username=ssh_user, password=ssh_password, allow_agent=False, look_for_keys=False)
    return ssh


import paramiko

def login():
    certificado_privado = paramiko.RSAKey.from_private_key_file("domotoy-key.pem")
    server_ssh = paramiko.SSHClient()
    server_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    server_ssh.connect( hostname = "ec2-15-237-27-210.eu-west-3.compute.amazonaws.com", username = "ubuntu", pkey = certificado_privado )
    print(server_ssh.exec_command('ls'))
    stdin, stdout, stderr = server_ssh.exec_command("docker ps | sed -n '2,$p' |awk '{print $1}'")
    print(stdout.readlines())
    server_ssh.close()

login()
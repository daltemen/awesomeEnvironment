import paramiko

from confs import conf


class SshCommandsRepo:

    def install_dependencies(self, server_model, public_ip):
        key = paramiko.RSAKey.from_private_key_file(f"{conf.SERVER_KEY_PATH}{server_model.name}.pem")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            print("*-------------------------------------------------------*")
            print("*-------------------------------------------------------*")
            print("*-----------------Installing Dependencies---------------*")
            command = f"sudo apt-get update && sudo apt-get install -y {' '.join(server_model.deps)}"
            print(command)
            client.connect(hostname=public_ip, username="ubuntu", pkey=key)
            stdin, stdout, stderr = client.exec_command(command)
            print(stdout.read())
            client.close()
        except Exception as e:
            print(e)

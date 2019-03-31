import time
import paramiko

from confs import conf


class SshCommandsRepo:

    def install_dependencies(self, server_model, public_ip):
        retry_sleep_sec = 7
        time.sleep(retry_sleep_sec)
        key = paramiko.RSAKey.from_private_key_file(f"{conf.SERVER_KEY_PATH}{server_model.name}.pem")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("*-------------------------------------------------------*")
        print("*-------------------------------------------------------*")
        print("*-----------------Installing Dependencies---------------*")
        print("Please wait, this process may take several minutes...")
        command = f"sudo apt-get update && sudo apt-get install -y {' '.join(server_model.deps)}"
        print(command)
        time.sleep(retry_sleep_sec)

        retry_times = 20
        for _ in range(retry_times):
            try:
                client.connect(hostname=public_ip, username="ubuntu", pkey=key)
                stdin, stdout, stderr = client.exec_command(command)
                print(stdout.read())
                client.close()
                return
            except Exception as e:
                time.sleep(retry_sleep_sec)
                print("Please wait, this process may take several minutes...")

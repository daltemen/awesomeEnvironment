import os
import boto3
from confs import conf


class KeyPairsRepo:

    def __init__(self, ec2_resouce):
        self.ec2 = boto3.resource('ec2')

    def create(self, server_model):
        print(f"creating key pair ... {server_model.name}")
        key_pair = self.ec2.create_key_pair(KeyName=server_model.name)
        path = f"{conf.SERVER_KEY_PATH}{server_model.name}.pem"

        with open(path, "w") as pem_file:
            pem_file.write(str(key_pair.key_material))

        os.chmod(path, 0o400)

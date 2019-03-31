import boto3
from confs import conf


class KeyPairsRepo:

    def __init__(self):
        self.ec2 = boto3.resource('ec2')

    def create(self, server_model):
        key_pair = self.ec2.create_key_pair(KeyName=server_model.name)
        path = f"{conf.SERVER_KEY_PATH}{server_model.name}.pem"

        with open(path, "w") as pem_file:
            pem_file.write(str(key_pair.key_material))

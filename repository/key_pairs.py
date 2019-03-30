import boto3



class KeyPairsRepo():

    def __init__(self):
        self.ec2 = boto3.resource('ec2')

    def create(self, model):
        key_pair = self.ec2.create_key_pair(KeyName='ec2-keypair')
        with open('ec2-keypair.pem', "w") as pem_file:
            pem_file.write(str(key_pair.key_material))

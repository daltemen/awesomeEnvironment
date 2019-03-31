import boto3

from models.models import Ami


class Ec2InstancesRepo:

    def __init__(self):
        self.ec2 = boto3.resource('ec2')

    def create(self):
        self.ec2.create_instances(
            ImageId=Ami.UBUNTU,
            MinCount=1,
            MaxCount=2,
            InstanceType='t2.nano',
            KeyName='ec2-keypair'
        )
        pass

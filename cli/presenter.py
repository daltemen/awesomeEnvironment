import argparse
import json
import boto3

from models.models import EnvironmentModel
from repository.ec2_instances_repo import Ec2InstancesRepo
from repository.key_pairs_repo import KeyPairsRepo
from repository.ssh_commands_repo import SshCommandsRepo
from usecases.instance_creation_usecase import CreateInstancesUseCase


class CliPresenter:

    def __init__(self):
        self.args = self._parse_args()

    def _parse_args(self):
        parser = argparse.ArgumentParser(description="Its a awesome environment script builder")
        parser.add_argument("-env", action="store", help="json env file", dest="env")
        parser.add_argument(
            "-key", action="store", help="key amazon ex: <access_key:secret_key>", dest="key"
        )
        return parser.parse_args()

    def execute(self):
        ec2 = boto3.resource(service_name='ec2')
        if self.args.key:
            key = self.args.key.strip(":")
            ec2 = boto3.resource(
                service_name='ec2',
                aws_access_key_id=key[0],
                aws_secret_access_key=key[1]
            )
        with open(self.args.env) as env_file:
            env_dict = json.load(env_file)
            use_case = CreateInstancesUseCase(
                ec2_repo=Ec2InstancesRepo(ec2),
                key_pairs_repo=KeyPairsRepo(ec2),
                ssh_repo=SshCommandsRepo()
            )
            result = use_case.process(
                EnvironmentModel(**env_dict)
            )

        print(result)

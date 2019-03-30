import argparse
import json

from models.EnvironmentModel import EnvironmentModel
from repository.ec2_instances import Ec2InstancesRepo
from repository.key_pairs import KeyPairsRepo
from usecases.instances import CreateInstancesUseCase


class CliPresenter:

    def __init__(self):
        self.args = self._parse_args()

    def _parse_args(self):
        parser = argparse.ArgumentParser(description="Its a awesome environment script builder")
        parser.add_argument("-env", action="store", help="json env file", dest="env")
        parser.add_argument(
            "-key", action="store", help="key amazon ex: <access_key:secret:key>", dest="key"
        )
        return parser.parse_args()

    def execute(self):
        if self.args.key:
            # TODO: Login or credentials with aws
            pass

        with open(self.args.env) as env_file:
            env_dict = json.load(env_file)
            use_case = CreateInstancesUseCase(
                ec2_repo=Ec2InstancesRepo(),
                key_pairs_repo=KeyPairsRepo()
            )
            use_case.process(
                EnvironmentModel(**env_dict)
            )

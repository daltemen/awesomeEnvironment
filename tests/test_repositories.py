from unittest.mock import MagicMock

from models.models import EnvironmentModel
from repository.ec2_instances_repo import Ec2InstancesRepo


def test_create_ec2_repo():
    env_model = {
        "name": "test-env-1",
        "region": "us-west-1",
        "servers": [
            {
                "name": "controller ",
                "deps": [
                    "nginx"
                ]
            },
            {
                "hostname": "endpoint ",
                "deps": [
                    "wget"
                ]
            }
        ]
    }
    env_model = EnvironmentModel(**env_model)
    ec2 = MagicMock()
    ec2_repo = Ec2InstancesRepo(ec2)
    ec2_repo.create(env_model.servers[0])
    assert ec2.create_vpc.called
    assert ec2.create_subnet.called
    assert ec2.create_security_group.called
    assert ec2.create_internet_gateway.called

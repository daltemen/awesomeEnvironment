from unittest.mock import MagicMock

from models.models import EnvironmentModel
from usecases.instance_creation_usecase import CreateInstancesUseCase


def test_create_instance_use_case():
    ec2_repo = MagicMock()
    key_pairs_repo = MagicMock()
    ssh_repo = MagicMock()
    use_case = CreateInstancesUseCase(ec2_repo, key_pairs_repo, ssh_repo)
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
    result = use_case.process(EnvironmentModel(**env_model))
    assert result[0].name_server == "controller"
    assert result[1].name_server == "endpoint"

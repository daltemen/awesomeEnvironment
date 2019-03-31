from models.models import Result

class CreateInstancesUseCase:

    def __init__(self, ec2_repo, key_pairs_repo, ssh_repo):
        self.ec2_repo = ec2_repo
        self.key_pairs_repo = key_pairs_repo
        self.ssh_repo = ssh_repo

    def process(self, env_model):
        servers_result = []
        ec2_repo = self.ec2_repo
        for server in env_model.servers:
            self.key_pairs_repo.create(server)
            ec2_instance = ec2_repo.create(server)
            self.ssh_repo.install_dependencies(
                server_model=server,
                public_ip=ec2_instance.public_ip_address
            )
            result = {
                "name_server": server.name,
                "private_ip": ec2_instance.private_ip_address,
                "public_ip": ec2_instance.public_ip_address
            }

            servers_result.append(Result(**result))
        return servers_result


class CreateInstancesUseCase:

    def __init__(self, ec2_repo, key_pairs_repo):
        self.ec2_repo = ec2_repo
        self.key_pairs_repo = key_pairs_repo

    def process(self, env_model):
        for server in env_model.servers:
            print(f"creating key pair ... {server.name}")
            self.key_pairs_repo.create(server)

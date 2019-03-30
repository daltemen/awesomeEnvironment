
class CreateInstancesUseCase:

    def __init__(self, ec2_repo, key_pairs_repo):
        self.ec2_repo = ec2_repo
        self.key_pairs_repo = key_pairs_repo

    def process(self, model):
        print(model)

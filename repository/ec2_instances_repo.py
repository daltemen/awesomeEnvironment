from models.models import Ami


class Ec2InstancesRepo:
    def __init__(self, ec2_resource):
        self.ec2 = ec2_resource
        self.subnet_id = None
        self.group_id = None

    def create(self, server_model):
        print(self.subnet_id)
        if not self.subnet_id or self.group_id:
            vpc = self._create_vpc()
            sec_group, subnet = self._create_security_group_and_subnet(vpc)
            self.subnet_id = subnet.id
            self.group_id = sec_group.id

        instances = self.ec2.create_instances(
            ImageId=Ami.UBUNTU.value,
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName=server_model.name,
            NetworkInterfaces=[
                {
                    "SubnetId": self.subnet_id,
                    "DeviceIndex": 0,
                    "AssociatePublicIpAddress": True,
                    "Groups": [self.group_id],
                }
            ],
        )
        print("creating ec2 instance...")
        instances[0].wait_until_running()
        print(f"instance ec2 created: {instances[0].id}")
        instances[0].reload()
        return instances[0]

    def _create_vpc(self):
        cidr = "192.168.0.0/16"
        print(f"Creation vpc cidr Block {cidr}")
        vpc = self.ec2.create_vpc(CidrBlock=cidr)
        vpc.create_tags(Tags=[{"Key": "Name", "Value": "daniel_default_vpc"}])
        vpc.wait_until_available()
        print(f"vpc created: {vpc.id}")
        return vpc

    def _create_security_group_and_subnet(self, vpc):
        route_table = self._create_route_table(vpc)

        subnet = self.ec2.create_subnet(CidrBlock="192.168.1.0/24", VpcId=vpc.id)
        print(f"subnet created: {subnet.id}")

        route_table.associate_with_subnet(SubnetId=subnet.id)

        print("creating security group...")
        sec_group = self.ec2.create_security_group(
            GroupName="daniel_slice_0", Description="slice_0 sec group", VpcId=vpc.id
        )
        sec_group.authorize_ingress(
            CidrIp="0.0.0.0/0", IpProtocol="tcp", FromPort=22, ToPort=22
        )
        print(f"security group created: {sec_group.id}")
        return sec_group, subnet

    def _create_route_table(self, vpc):
        ig = self.ec2.create_internet_gateway()
        vpc.attach_internet_gateway(InternetGatewayId=ig.id)
        print(f"internet gateway created: {ig.id}")

        route_table = vpc.create_route_table()
        route_table.create_route(DestinationCidrBlock="0.0.0.0/0", GatewayId=ig.id)
        print(f"Route table id created: {route_table.id}")
        return route_table

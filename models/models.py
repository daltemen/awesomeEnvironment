from enum import Enum


class Ami(Enum):
    UBUNTU = "ami-06397100adf427136"


class EnvironmentModel:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.region = kwargs.get("region")
        self.servers = [ServerModel(**server) for server in kwargs.get("servers")]

    def __str__(self):
        return f"name: {self.name} region: {self.region}"


class ServerModel:

    def __init__(self, **kwargs):
        raw_name = kwargs.get("name") if kwargs.get("name") else kwargs.get("hostname")
        self.name = raw_name.strip()
        self.deps = kwargs.get("deps")


    def __str__(self):
        return f"name: {self.name} deps: {self.deps}"


class Result:

    def __init__(self, **kwargs):
        self.name_server = kwargs.get("name_server")
        self.private_ip = kwargs.get("private_ip")
        self.public_ip = kwargs.get("public_ip")

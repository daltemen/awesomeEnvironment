from enum import Enum


class Ami(Enum):
    UBUNTU = "ami-00b6a8a2bd28daf19"


class EnvironmentModel:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.region = kwargs.get("region")
        self.servers = [ServerModel(**server) for server in kwargs.get("servers")]

    def __str__(self):
        return f"name: {self.name} region: {self.region} servers: {self.servers}"


class ServerModel:

    def __init__(self, **kwargs):
        self.host_name = kwargs.get("hostname")
        self.name = kwargs.get("name")
        self.deps = kwargs.get("deps")

    def __str__(self):
        return f"host_name: {self.host_name} name: {self.name} deps: {self.deps}"

from typing import Optional
from .models import Device


class CommandHandler:
    def __init__(self, device):
        self.device = device
        self.client = device.client
        self.COMMANDS = {
            "spot": self.spot,
            "service_create": self.service_create,
            "bruteforce": self.bruteforce
        }

    def execute(self, command: str, args: Optional[list[str]] = None):
        if command not in self.COMMANDS:
            raise Exception('Command not found')
        return self.COMMANDS[command](args)

    def spot(self, args):
        spotted_device = Device(self.client.ms('device', ['device', 'spot'], {}), self.client)
        return spotted_device

    def service_create(self, args: list[str]):
        service_name = args[0]
        return self.client.ms('service', ['create'], {
            "device_uuid": self.device.uuid,
            "name": service_name
        })

    def bruteforce(self, args: list[str]):
        device_uuid = self.device.uuid
        service_uuid = args[0]
        target_device = args[1]
        target_service = args[2]




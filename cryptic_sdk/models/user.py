from .device import Device
from .wallet import Wallet
from typing import List

Devices = List[Device]

class User(object):
    def __init__(self, client) -> None:
        self.client = client
        json = self.client.request({"action": "info"})
        self.name = json['name']
        self.uuid = json['uuid']
        self.created = json['created']
        self.dict = json

    def getDevices(self) -> Devices:
        raw_devices = self.client.ms('device', ['device', 'all'], {})['devices']
        devices = []
        for device in raw_devices:
            devices.append(Device(device, self.client))
        return devices

    def getDevice(self, uuid: str):
        raw_devices = self.client.ms('device', ['device', 'all'], {})['devices']
        for device in raw_devices:
            if device['uuid'] == uuid:
                return Device(device, self.client)
        return None

    def getWallet(self, wallet_id: str, wallet_key: str) -> list:
        return Wallet(self.client, wallet_id, wallet_key)

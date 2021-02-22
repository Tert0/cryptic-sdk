from .device import Device


class User(object):
    def __init__(self, client, json: dict) -> None:
        self.client = client
        self.name = json['name']
        self.uuid = json['uuid']
        self.created = json['created']
        self.dict = json

    def getDevices(self) -> list[Device]:
        raw_devices = self.client.ms('device', ['device', 'all'], {})['devices']
        devices = []
        for device in raw_devices:
            devices.append(Device(device, self.client))
        return devices

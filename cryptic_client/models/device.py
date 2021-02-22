class Device(object):
    def __init__(self, json: dict, client) -> None:
        self.client = client
        self.owner = json['owner']
        self.name = json['name']
        self.started_device = bool(json['starter_device'])
        self.uuid = json['uuid']
        self.on = bool(json['powered_on'])
        self.dict = json

    def togglePower(self) -> bool:
        self.client.ms('device', ['device', 'power'], {'device_uuid': self.uuid})
        self.on = not self.on
        return self.on

    def setName(self, name: str) -> None:
        self.client.ms('device', ['device', 'change_name'], {"device_uuid": self.uuid, "name": name})
        self.name = name

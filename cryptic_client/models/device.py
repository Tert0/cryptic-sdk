class Device(object):
    def __init__(self, json: dict) -> None:
        self.owner = json['owner']
        self.name = json['name']
        self.started_device = bool(json['starter_device'])
        self.uuid = json['uuid']
        self.on = bool(json['powered_on'])
        self.dict = json


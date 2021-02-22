class User(object):
    def __init__(self, json: dict) -> None:
        self.name = json['name']
        self.uuid = json['uuid']
        self.created = json['created']
        self.dict = json

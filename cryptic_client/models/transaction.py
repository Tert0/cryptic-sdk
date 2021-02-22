class Transaction(object):
    def __init__(self, client, json: dict):
        self.client = client
        self.send_amount = json['send_amount']
        self.time_stamp = json['time_stamp']
        self.destination_uuid = json['destination_uuid']
        self.usage = json['usage']
        self.source_uuid = json['source_uuid']
        self.id = json['id']
        self.dict = json
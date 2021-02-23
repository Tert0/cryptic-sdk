class Device(object):
    """
    Device Object
    """
    def __init__(self, json: dict, client) -> None:
        """
        Parameters
        ----------
        json : dict
            Json Data of the Device
        client : :py:class:`cryptic_sdk.Client`
            Client
        """
        self.client = client
        self.owner = json['owner']
        self.name = json['name']
        self.started_device = bool(json['starter_device'])
        self.uuid = json['uuid']
        self.on = bool(json['powered_on'])
        self.dict = json

    def togglePower(self) -> bool:
        """
        Toggels the Power of the Device
        
        Returns
        -------
        power : bool
            Power Status of the Device
        """
        self.client.ms('device', ['device', 'power'], {'device_uuid': self.uuid})
        self.on = not self.on
        return self.on

    def setName(self, name: str) -> None:
        """
        Setter of the Device Name
        
        Parameters
        ----------
        name : str
            New Name of the Device
        """
        self.client.ms('device', ['device', 'change_name'], {"device_uuid": self.uuid, "name": name})
        self.name = name

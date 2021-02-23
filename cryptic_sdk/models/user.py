from .device import Device
from .wallet import Wallet
from typing import List

Devices = List[Device]

class User(object):
    """
    Representation of an Cryptic User Account
    """
    def __init__(self, client) -> None:
        """
        Parameters
        ----------
        client : cryptic_sdk.Client
            Cryptic Client
        """
        self.client = client
        json = self.client.request({"action": "info"})
        self.name = json['name']
        self.uuid = json['uuid']
        self.created = json['created']
        self.dict = json

    def getDevices(self) -> Devices:
        """
        Getter for :py:class:`cryptic_sdk.Device`
        
        Returns
        -------
        Devices : list of :py:class:`cryptic_sdk.Devices`
            List of all Devices
        """
        raw_devices = self.client.ms('device', ['device', 'all'], {})['devices']
        devices = []
        for device in raw_devices:
            devices.append(Device(device, self.client))
        return devices

    def getDevice(self, uuid: str):
        """
        Getter for :py:class:`cryptic_sdk.Device` by Device UUID
        
        Parameters
        ----------
        uuid : str
            Device UUID

        Returns
        -------
        device : Device
        """
        raw_devices = self.client.ms('device', ['device', 'all'], {})['devices']
        for device in raw_devices:
            if device['uuid'] == uuid:
                return Device(device, self.client)
        return None

    def getWallet(self, wallet_id: str, wallet_key: str) -> list:
        """
        Getter for Wallet
        
        Parameters
        ----------
        wallet_id : str
            Wallet UUID of the Wallet
        wallet_key : str

        """
        return Wallet(self.client, wallet_id, wallet_key)

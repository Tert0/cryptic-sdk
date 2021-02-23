import websocket
import time
import json
from uuid import uuid4
from . import expeptions
from .models.user import User
from typing import List

def uuid():
    return str(uuid4())


class Client:
    """
    Cryptic Client

    Parameters
    ----------
    uri : str
        Websocket URI of the Cryptic Backend
    """
    def __init__(self, uri: str):
        self.uri = uri
        self.websocket = websocket.create_connection(self.uri)
        self.waiting_for_response = False
        self.notifications: list = []
        self.logged_in = False

    def request(self, data: dict) -> dict:
        """
        Make a Request to the Backend

        Parameters
        ----------
        data : dict
            Data for the Backend

        Raises
        ------
        cryptic_client.Timeout
            Raises :py:class:cryptic_client.Timeout if the connection Timeouts
        cryptic_client.MissingParameters
            Raises :py:class:`cryptic_client.MissingParameters` if not all Parameters are passed to the Backend
        cryptic_client.PermissionsDenied
            Raises :py:class:`cryptic_client.PermissionsDenied` if you dont have the Permissions to do that
        cryptic_client.InvalidToken
            Raises :py:class:`cryptic_client.InvalidToken` if the Session Token is Invalid
        cryptic_client.InvalidPassword
            Raises :py:class:`cryptic_client.InvalidPassword` if the Password Token is Invalid
        cryptic_client.UsernameAlreadyExists
            Raises :py:class:`cryptic_client.UsernameAlreadyExists` if the Username Alredy exists

        Returns
        -------
        response : dict
            Repsonse from the Backend
        """
        while self.waiting_for_response:
            time.sleep(0.01)
        self.waiting_for_response = True
        self.websocket.send(json.dumps(data))
        while True:
            response: dict = json.loads(self.websocket.recv())
            if 'notify-id' in response:
                self.notifications.append(response)
            else:
                break
        self.waiting_for_response = False
        if 'error' in response:
            error = response['error']
            if error == 'timeout':
                raise expeptions.Timeout
            elif error == 'missing parameters':
                raise expeptions.MissingParameters
            elif error == 'permissions denied':
                raise expeptions.PermissionsDenied
            elif error == 'invalid token':
                raise expeptions.InvalidToken
            elif error == 'invalid password':
                raise expeptions.InvalidPassword
            elif error == 'username already exists':
                raise expeptions.UsernameAlreadyExists
        return response

    def login(self, username: str, password: str) -> str:
        """
        Logins into a User account

        Parameters
        ----------
        username : str
            Username of the User account
        password : str
            Password of the User account

        Returns
        -------
        token : str
            Session Token
        """
        token = self.request({
            'action': 'login',
            'name': username,
            'password': password
        })['token']
        self.logged_in = True
        return token

    def logout(self) -> bool:
        """
        Logouts the User
    
        Returns
        -------
        status : bool
            Status
        """
        if self.logged_in:
            self.request({"action": "logout"})
            self.logged_in = False
            return True
        return False

    def ms(self, ms: str, endpoint: List[str], data: dict) -> dict:
        """
        Sends Microservice Requests
    
        Parameters
        ----------
        ms : str
            Name of the Microservice
        endpoint : List[str]
            Path to the Endpoint as list
        data : dict
        Data for the request

        Returns
        -------
        data : dict
            Data of the response

        Raises
        ------
        expeptions.InvalidInputData
            Raises :py:class:`expeptions.InvalidInputData` when the MS throws an Invalid Input Data error
        expeptions.MicroServiceExpeption
            Raises :py:class:`expeptions.MicroServiceExpeption` when the MS throws an Error
        """
        if not self.logged_in:
            raise expeptions.PermissionsDenied
        response = self.request({
            "tag": uuid(),
            "ms": ms,
            "endpoint": endpoint,
            "data": data
        })
        if 'error' in response:
            raise expeptions.MicroServiceExpeption(str(response['error']))
        if 'data' not in response:
            raise expeptions.InvalidServerResponse
        data = response['data']

        if 'error' in data:
            error = data['error']
            if error == 'invalid_input_data':
                raise expeptions.InvalidInputData
            else:
                raise expeptions.MicroServiceExpeption(str(data['error']))
        return data

    def register(self, username: str, password: str) -> str:
        """
        Registers an new User account
    
        Parameters
        ----------
        username : str
            Username of the new User account
        password : str
            Password of the new User account
    
        Returns
        -------
        token : str
            Session Token
        """
        resp = self.request({
            "action": "register",
            "name": username,
            "password": password
        })
        return resp['token']

    def getUser(self) -> User:
        """
        Getter of User object

        Returns
        -------
        user : discord_sdk.user
            User Object
        """
        return User(self)

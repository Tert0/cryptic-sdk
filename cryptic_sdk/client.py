import websocket
import time
import json
from uuid import uuid4
from . import expeptions
from .models.user import User


def uuid():
    return str(uuid4())


class Client:
    def __init__(self, uri: str):
        self.uri = uri
        self.websocket = websocket.create_connection(self.uri)
        self.waiting_for_response = False
        self.notifications: list = []
        self.logged_in = False

    def request(self, data: dict) -> dict:
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

    def login(self, username: str, password: str):
        token = self.request({
            'action': 'login',
            'name': username,
            'password': password
        })['token']
        self.logged_in = True
        return token

    def logout(self) -> bool:
        if self.logged_in:
            self.request({"action": "logout"})
            self.logged_in = False
        return True

    def ms(self, ms: str, endpoint: list[str], data: dict) -> dict:
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
            error = data['data']
            if error == 'invalid_input_data':
                raise expeptions.InvalidInputData
            else:
                raise expeptions.MicroServiceExpeption(str(data['error']))
        return data

    def register(self, username: str, password: str) -> str:
        resp = self.request({
            "action": "register",
            "name": username,
            "password": password
        })
        return resp['token']

    def getUser(self) -> User:
        return User(self)

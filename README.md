# Cryptic Client
A [Cryptic Game](https://github.com/cryptic-game/cryptic) Client Library for Python
## Installation
```pip install cryptic-client```
## Example
```python
from cryptic_client import *


USERNAME = 'Username'
PASSWORD = 'Password'

myclient = Client('wss://ws.cryptic-game.net:443/')

print(myclient.request({"action": "status"}))
print(myclient.login(USERNAME, PASSWORD))

devices = myclient.ms('device', ['device', 'all'], {})
print(devices)
print(myclient.ms('device', ['device', 'info'], {'device_uuid': devices['devices'][0]['uuid']}))

print(myclient.logout())


```
## Docs
Coming Soon
from cryptic_sdk import *

USERNAME = 'TestMik'
PASSWORD = 'XzeauC9vgccbepUT3x9HiKqU282rMNp2pFwsFvnMLouKc6WTBS'

client = Client('wss://ws.cryptic-game.net:443/')

print(client.request({"action": "status"}))
print(client.login(USERNAME, PASSWORD))


#client.getUser().getWallet("b48bd270-e2a3-43a1-9ae9-a3dbb14257de", "d142bee435").pay("8c9718e5-eceb-4d0d-a8dd-971e520e80b9", 900000, 'mik1234 Kundenkarte ;)')

d = client.getUser().getDevices()[0]
cmd = client.getUser().getCommandHandler(d)
spotted = cmd.execute("spot")
print(spotted.dict)


print(client.logout())

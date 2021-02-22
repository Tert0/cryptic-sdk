from .transaction import Transaction


class Wallet(object):

    def __init__(self, client, wallet_id: str, wallet_key: str):
        json = client.ms('currency', ['get'], {'source_uuid': wallet_id, 'key': wallet_key})
        self.client = client
        self.time_stamp = json['time_stamp']
        self.source_uuid = json['source_uuid']
        self.key = json['key']
        self.amount: float = json['amount'] / 1000
        self.user_uuid = json['user_uuid']
        self.transactions_count: int = json['transactions']
        self.transactions = client.ms('currency', ['transactions'], {
            'source_uuid': wallet_id,
            'key': wallet_key,
            'count': self.transactions_count,
            'offset': 0
        })['transactions']
        self.transactions = [Transaction(self.client, transaction) for transaction in self.transactions]
        self.dict = json
        self.dict['transactions'] = [transaction.dict for transaction in self.transactions]

    def pay(self, destination_uuid: str, amount: float, usage=''):
        self.client.ms('currency', ['send'], {
            'source_uuid': self.source_uuid,
            'key': self.key,
            'send_amount': amount,
            'destination_uuid': destination_uuid,
            'usage': usage
        })

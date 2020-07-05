#coinbase classes
from coinbase.wallet.client import Client

class CoinBaseClient:
    def __init__(self,details_dict):
        # create a client
        self.client = Client(details_dict['api_key'], details_dict['api_secret'])
        # get all accounts
    
    def get_client_accounts(self):
        return self.client.get_accounts()

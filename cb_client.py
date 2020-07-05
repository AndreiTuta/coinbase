#coinbase classes
from coinbase.wallet.client import Client
# custom classes
import wallet

class CoinBaseClient:
    def __init__(self,details_dict):
        # create a client
        self.client = Client(details_dict['api_key'], details_dict['api_secret'])
        # get all accounts
    
    def get_client_accounts(self):
        return self.client.get_accounts()
    
    def get_client_wallets(self):
        accounts = self.client.get_accounts()['data']
        return accounts
# coinbase classes
from coinbase.wallet.client import Client
# custom classes
from wallet import Wallet


class CoinBaseClient:
    def __init__(self, details_dict):
        # create a client
        self.client = Client(
            details_dict['api_key'], details_dict['api_secret'])
        self.fetch_accounts()
        
    # internal use
    def get_client_accounts(self):
        return self.client.get_accounts()

    def fetch_accounts(self):
        self.wallets = list()
        accounts = self.get_client_accounts()['data']
        for account in accounts:
            account_wallet = Wallet(account).toStr()
            self.wallets.append(account_wallet)
            
    # external use
    def get_client_wallets(self, refresh):
        if(refresh):
            self.fetch_accounts()
        return self.wallets

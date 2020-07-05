# coinbase classes
from coinbase.wallet.client import Client
# custom classes
from cb_wallet import Wallet


class CoinBaseClient:
    # internal use
    def get_client_accounts(self):
        return self.client.get_accounts()

    def fetch_accounts(self):
        self.wallets = list()
        accounts = self.get_client_accounts()['data']
        for account in accounts:
            account_wallet = Wallet(account).to_str()
            self.wallets.append(account_wallet)

    def fetch_account(self, coin):
        currency_wallets = list()
        accounts = self.get_client_accounts()['data']
        for account in accounts:
            account_wallet = Wallet(account)
            if(account_wallet.get_currency(coin) is not None):
                # TODO: Move all vars into functions
                coinbase_buy_price = str(self.client.get_buy_price(
                    currency_pair=coin+'-'+'GBP')['amount'])
                coinbase_sell_price = str(self.client.get_sell_price(
                    currency_pair=coin+'-'+'GBP')['amount'])
                account_wallet.add_prices(
                    coinbase_buy_price, coinbase_sell_price)
                exachange_rates = self.client.get_exchange_rates(currency=coin)['rates']
                account_wallet.add_rates(exachange_rates)
                currency_wallets.append(account_wallet.to_str())
        return currency_wallets

    # constructor
    def __init__(self, details_dict):
        # create a client
        self.client = Client(
            details_dict['api_key'], details_dict['api_secret'])
        self.fetch_accounts()

    # external use
    def get_client_wallets(self, refresh):
        if(refresh):
            self.fetch_accounts()
        return self.wallets

    def get_client_wallet(self, currency):
        return self.fetch_account(currency)

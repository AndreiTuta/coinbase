# coinbase classes
from coinbase.wallet.client import Client
# custom classes
from cb_wallet import Wallet
import datetime

class CoinBaseClient:
    # internal use
    def get_client_accounts(self):
        return self.client.get_accounts()['data']

        """
        params order: coin
        """

    def get_wallets(self, *args, **kwargs):
        # todo: change all functions to have an arg type and a return type
        currency_wallet = list()
        for account in self.accounts:
            if(len(args) != 0):
                coin = args[0]
            else:
                coin = account['currency']
            account_wallet = Wallet(account,datetime.datetime.now(datetime.timezone.utc))
            if (account_wallet.has_currency(coin)):
                # TODO: Move all vars into functions
                coinbase_buy_price = str(self.client.get_buy_price(
                    currency_pair=coin+'-'+'GBP')['amount'])
                coinbase_sell_price = str(self.client.get_sell_price(
                    currency_pair=coin+'-'+'GBP')['amount'])
                account_wallet.add_prices(
                    coinbase_buy_price, coinbase_sell_price)
                #account_wallet.get_dates_utc()
                exachange_rates = self.client.get_exchange_rates(currency=coin)[
                    'rates']
                account_wallet.add_rates(exachange_rates, self.rates_included)
                currency_wallet.append(account_wallet.to_dict())
        return currency_wallet

    # constructor
    def __init__(self, details_dict):
        # create a client
        self.client = Client(
            details_dict['api_key'], details_dict['api_secret'])
        self.accounts = self.get_client_accounts()
        self.rates_included = ['ETH', 'BTC', 'GBP', 'DAI', 'ALGO']

    # external use
    def get_client_wallets(self):
        print(self.get_wallets())
        return self.get_wallets()

    def get_client_wallet(self, coin):
        return self.get_wallets(coin)

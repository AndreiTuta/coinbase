# coinbase classes
from coinbase.wallet.client import Client
# custom classes
from cb_wallet import Wallet


class CoinBaseClient:
    # internal use
    def get_client_accounts(self):
        return self.client.get_accounts()

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
            account_wallet = Wallet(account)
            if (account_wallet.has_currency(coin)):
                # TODO: Move all vars into functions
                coinbase_buy_price = str(self.client.get_buy_price(
                    currency_pair=coin+'-'+'GBP')['amount'])
                coinbase_sell_price = str(self.client.get_sell_price(
                    currency_pair=coin+'-'+'GBP')['amount'])
                account_wallet.add_prices(
                    coinbase_buy_price, coinbase_sell_price)
                exachange_rates = self.client.get_exchange_rates(currency=coin)[
                    'rates']
                account_wallet.add_rates(exachange_rates)
                currency_wallet.append(account_wallet.to_str())
        return currency_wallet

    # constructor
    def __init__(self, details_dict):
        # create a client
        self.client = Client(
            details_dict['api_key'], details_dict['api_secret'])
        self.accounts = self.get_client_accounts()['data']
        self.wallets = self.get_client_wallets()

    # external use
    def get_client_wallets(self):
        return self.get_wallets()

    def get_client_wallet(self, coin):
        return self.get_wallets(coin)

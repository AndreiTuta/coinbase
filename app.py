# imports
import json
import urllib
import configparser
import time

#coinbase classes
from coinbase.wallet.client import Client
# custom classes
from wallet import Wallet

def coinbase_call():
    # load config from file
    config = configparser.RawConfigParser()
    config.read('config.ini')
    details_dict = dict(config.items('coinbase'))
    # get api_key and secret
    api_key = details_dict['api_key']
    api_secret = details_dict['api_secret']
    # create a client
    client = Client(api_key, api_secret)
    # get all accounts
    return client.get_accounts()

accounts = coinbase_call()
for cb_wallet in accounts.data:
    print(cb_wallet.items())
    # for detail in cb_wallet.items():
        # print(detail)
     # wallet = Wallet(cb_wallet)
     # current = time.time
     # wallet.print_wallet(current)

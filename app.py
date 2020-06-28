# imports
import json
import urllib
import configparser
import time
#coinbase classes
from coinbase.wallet.client import Client
# pretty pprint
from pprint import pprint
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
     wallet = Wallet(cb_wallet)
     # TODO: add current time
     # csv print
     print(wallet.print_to_csv())
     # pretty print
     #pprint(wallet.print())

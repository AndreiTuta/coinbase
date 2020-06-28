from coinbase.wallet.client import Client
import json
import urllib
import configparser

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
accounts = client.get_accounts()
print(accounts)

#
# for wallet in accounts.data:
#     if(wallet["currency"] == "ETH"):
        # print(wallet)

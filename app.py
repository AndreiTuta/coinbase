# imports
import json
import urllib
import configparser
import datetime
import time
#coinbase classes
from coinbase.wallet.client import Client
# pretty pprint
from pprint import pprint
# custom classes
from wallet import Wallet

# load config from file
config = configparser.RawConfigParser()
config.read('config.ini')
details_dict = dict(config.items('coinbase'))

def init_client():
    # get api_key and secret
    api_key = details_dict['api_key']
    api_secret = details_dict['api_secret']
    # create a client
    client = Client(api_key, api_secret)
    # get all accounts
    return client

def coinbase_call(client):
    return client.get_account(details_dict['account_id'])

def coinbase_buy_price(client, crypto, currency):
    return client.get_buy_price(currency_pair = crypto+'-'+currency)["amount"]

def coinbase_sell_price(client, crypto, currency):
    return client.get_sell_price(currency_pair = crypto+'-'+currency)["amount"]

def check_balance(client):
    cb_wallet = coinbase_call(client)
    wallet = Wallet(cb_wallet)
    return wallet.get_sequence()

def display_stats(current):
    client = init_client()
    seq = check_balance(client)
    # add time
    seq.insert(0, str(current.hour) + ":" + str(current.minute))
    # add buy price
    seq.insert(len(seq) + 1, str(coinbase_buy_price(client, seq[3], seq[5])))
    # add sell price
    seq.insert(len(seq) + 1, str(coinbase_sell_price(client, seq[3], seq[5])))
    print(', '.join(seq))

def main():
    while True:
        current = datetime.datetime.now()
        display_stats(current)
        time.sleep(1 *60)

if __name__ == '__main__':
    main()

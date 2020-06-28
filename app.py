# imports
import sys

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
# custom functions
from utils import parse_string_to_int, get_current_hour_minutes_seconds

# TODO: move to separate file
# GLOBAL config
# load config from file
config = configparser.RawConfigParser()
config.read('config.ini')
details_dict = dict(config.items('coinbase'))

modes = ['dev', 'active', 'info']
timer_options = ['1', '10', '60']

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
    return client.get_buy_price(currency_pair = crypto+'-'+currency)['amount']

def coinbase_sell_price(client, crypto, currency):
    return client.get_sell_price(currency_pair = crypto+'-'+currency)['amount']

def check_balance(client):
    cb_wallet = coinbase_call(client)
    wallet = Wallet(cb_wallet)
    return wallet.get_sequence()

def display_stats(client, current):
    seq = check_balance(client)
    # add time
    seq.insert(0, get_current_hour_minutes_seconds(current))
    # add buy price
    seq.insert(len(seq) + 1, str(coinbase_buy_price(client, seq[3], seq[5])))
    # add sell price
    seq.insert(len(seq) + 1, str(coinbase_sell_price(client, seq[3], seq[5])))
    print(', '.join(seq))

def handle_arg(x):
    timer = timer_options[0]
    mode = modes[0]
    if (isinstance(x, str)):
        if(x in modes):
            print('Mode set to ' + x)
            mode = x
        else:
             if (isinstance(parse_string_to_int(x), int)):
                 print('Time set to ' + x)
                 timer = x
             else:
                print('Undefined ' + x)
    return [timer, mode]

def main(argv):
    argv_processed = list(filter(lambda x : handle_arg(x) , argv))
    print(argv_processed)
    timer = parse_string_to_int(argv_processed[0])
    mode = argv_processed[1]
    hits = 0
    while True:
        current = datetime.datetime.now()
        if(mode=='dev'):
            print('deving...')
        else:
            client = init_client()
            hits += 1
            print('Strike ' + str(hits))
            display_stats(client, current)
        print('Sleeping from ' + get_current_hour_minutes_seconds(current) +' for '+ str(timer * 60) + ' seconds')
        time.sleep(timer * 60)
        print('Sleept until ' + get_current_hour_minutes_seconds(current))

if __name__ == '__main__':
    main(sys.argv[1:])

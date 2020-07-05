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
from utils import parse_string_to_int, get_current_hour_minutes_seconds, get_current_hour_minutes, write_results

# TODO: move to separate file
# GLOBAL config
# load config from file
config = configparser.RawConfigParser()
config.read('config.ini')
details_dict = dict(config.items('coinbase'))

modes = ['dev', 'active', 'info']
timer_options = ['1', '10', '60']

PATH = './results/'
CSV_COLS = ('Time','Name', 'Amount', 'Currency', 'Won amount', 'Won Currency', 'Buy price', 'Sell price')


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

def generate_stats(client, current):
    if client is None:
      client = init_client() 
    seq = check_balance(client)
    # add time
    seq.insert(0, get_current_hour_minutes(current))
    # add buy price
    seq.insert(len(seq) + 1, str(coinbase_buy_price(client, seq[2], seq[4])))
    # add sell price
    seq.insert(len(seq) + 1, str(coinbase_sell_price(client, seq[2], seq[4])))
    print(seq)
    # then remove the currencies
    seq.pop(2)
    # TODO: LOOOOL
    seq.pop(3)
    line = ','.join(seq)
    print(line)
    return line + '\n'

    """
    [ 
    
    Writes down as csv the result of 
    (time (minutes) x api calls (one, then sleep for time )) 
    in chuncks of write_groups
    
    ]
    """
def generate_csv(timer, mode, write_hits, write_groups):
    for i in range(write_groups):
        response_list =[]
        hits = 0
        current = datetime.datetime.now()
        while hits <= write_hits:
            client = init_client()            
            in_current = datetime.datetime.now()
            hits += 1
            response_list.append(generate_stats(client, in_current))
            print('Sleeping from ' + get_current_hour_minutes_seconds(in_current) +' for '+ str(timer * 60) + ' seconds')
            if(mode=='dev'):
                print('deving...')
            else:
                time.sleep(timer * 60)
        print('Writing results ' + str(i + 1))
        write_results(PATH, response_list, current)

# write_groups x (time x api_calls)
if __name__ =="__main__":
    generate_csv(2,'active',15, 10)

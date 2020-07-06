from flask import Flask, Response, request

import configparser
import json

from cb_client import CoinBaseClient

app = Flask(__name__)


# load config from file
config = configparser.RawConfigParser()
config.read('config.ini')
details_dict = dict(config.items('coinbase'))

client = CoinBaseClient(details_dict)

@app.route('/wallets')
def wallets_endpoint():
    wallet_data = client.get_client_wallets()
    return Response(json.dumps(wallet_data),  mimetype='application/json')


@app.route('/wallet/<currency>')
def wallet_endpoint(currency):
    wallet_data = client.get_client_wallet(currency)
    return Response(json.dumps(wallet_data),  mimetype='application/json')


@app.route('/accounts')
def accounts_endpoint():
    accounts_data = client.get_client_accounts()
    return Response(json.dumps(accounts_data),  mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True, port=8080)

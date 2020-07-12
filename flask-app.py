from flask import Flask, Response, request, render_template, abort

import configparser
import json

from cb_client import CoinBaseClient

app = Flask(__name__)


# load config from file
config = configparser.RawConfigParser()
config.read('config.ini')
details_dict = dict(config.items('coinbase'))

# Backend endpoints


@app.route('/wallets')
def wallets_endpoint():
    client = CoinBaseClient(details_dict)
    wallet_data = client.get_client_wallets()
    return render_template('wallet.html', wallets=wallet_data)


@app.route('/wallet/<currency>/<wallet_id>')
def wallet_endpoint(currency,wallet_id):
    client = CoinBaseClient(details_dict)
    wallet_data = client.get_client_wallet(currency)
    return wallet_data[0]


if __name__ == "__main__":
    app.run(debug=True, port=8080)

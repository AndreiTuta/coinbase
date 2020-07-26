from flask import Flask, Response, request, render_template, abort

import configparser
import json
import html

from cb_client import CoinBaseClient
from cb_chart_module import ChartModule
from cb_news import NewsClient

app = Flask(__name__)


# load config from file
config = configparser.RawConfigParser()
config.read('config.ini')
coinbase_dict = dict(config.items('coinbase'))
news_dict = dict(config.items('news'))

client = CoinBaseClient(coinbase_dict)
news_client = NewsClient(news_dict['news_api_key'])
# Backend endpoints
@app.route('/wallets')
def wallets_endpoint():
    wallet_data = client.get_client_wallets()
    wallets_json = html.unescape(wallet_data)
    wallet_news = html.unescape(news_client.get_news(client.rates_included))
    
    return render_template('wallet.html', wallets=wallet_data, wallet_data_json = wallets_json, wallet_news = wallet_news)


@app.route('/wallet/<currency>/<wallet_id>')
def wallet_endpoint(currency,wallet_id):
    wallet_data = client.get_client_wallet(currency)
    
    return wallet_data[0]

# Frontend endpoints
@app.route('/chart')
def chart():    
    module = ChartModule()
    return render_template('chartjs.html', labels = [1900, 1950, 1999, 2050, 2100], chart_module = module)


if __name__ == "__main__":
    app.run(debug=True, port=8080)

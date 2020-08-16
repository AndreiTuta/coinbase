from flask import Flask, render_template

import configparser
import html

from cb_client import CoinBaseClient
from cb_chart_module import ChartModule
from cb_news import NewsClient, get_covid_news, get_news

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
    wallet_news = html.unescape(get_news(client.rates_included))

    return render_template('wallet.html', wallets=wallet_data, wallet_data_json=wallets_json, wallet_news=wallet_news)


@app.route('/wallet/<currency>')
def wallet_endpoint(currency):
    wallet_data = client.get_client_wallet(currency)

    return wallet_data[0]


# Frontend endpoints
@app.route('/chart/<date>')
def chart(date):
    news_data = get_covid_news(date)
    module = ChartModule(news_data)
    return render_template("chartjs.html", chart_module=module, news_data_json=news_data)


if __name__ == "__main__":
    app.run(debug=True, port=8080)

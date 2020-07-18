from crypto_news_api import CryptoControlAPI
from file_util import write_as_csv

sswitcher = {
        "ETH": 'ethereum',
        "BTC": 'bitcoin',
        "DAI": 'dai',
        "GBP": 'gbp',
        "ALGO" : 'algorand'
    }

class NewsClient:
    def __init__(self, api_key):
        # Connect to the CryptoControl API
        self.client = CryptoControlAPI(api_key)

    def get_coin_news(self, coin_code):
        return self.client.getTopNewsByCoin(coin_code)

    def get_news(self, currencies):
        news = {}
        for coin in currencies:           
            if(coin !="GBP"):
                coin_code = sswitcher[coin]
                news_array = self.get_coin_news(coin_code)
                news[coin] =  news_array
        
        write_as_csv(news)
        
        return news
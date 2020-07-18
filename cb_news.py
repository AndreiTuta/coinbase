from crypto_news_api import CryptoControlAPI

sswitcher = {
        "ETH": 'ethereum',
        "BTC": 'bitcoin',
        "DAI": 'dai',
        "GBP": 'gbp'
    }

class NewsClient:
    def __init__(self, api_key):
        # Connect to the CryptoControl API
        self.client = CryptoControlAPI(api_key)

    def get_news(self, currencies):
        news = {}
        for coin in currencies:           
            if(coin !="GBP"):
                coin_code = sswitcher[coin]
                news[coin_code] =  self.client.getTopNewsByCoin(coin_code)
        
        print(news.keys())
        return news
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
        aDict = {'_id': '5f0c8fdb0b40f100190d2ec9', 'title': 'This Overhead Liquidity Region Could Propel Bitcoin Past $12,000', 'publishedAt': '2020-07-13T16:00:43.000Z', 'sourceDomain': 'newsbtc.com', 'url': 'https://cryptocontrol.io/r/api/article/5f0c8fdb0b40f100190d2ec9?ref=5f12c93922ee0f0018aae1b9', 'thumbnail': 'https://cloudfront.cryptocontrol.io/thumbnails/5f0c8fdb0b40f100190d2ec9-1594658779565.jpg'}
        news = {"ETH" : aDict , "ALGO" : aDict, "BTC" : aDict, "DAI" : aDict}
        print(news)
        return news
        # TODO: Expand new debug mode as api takes long to load sometimes
        # news = {}
        # for coin in currencies:           
        #     if(coin !="GBP"):
        #         coin_code = sswitcher[coin]
        #         news_array = self.get_coin_news(coin_code)
        #         news[coin] =  news_array
        
        # write_as_csv(news)
        
        # return news
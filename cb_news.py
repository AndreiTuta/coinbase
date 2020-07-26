from crypto_news_api import CryptoControlAPI
from file_util import write_as_csv
from datetime import timedelta, date

import datetime
import requests
import json



payload = {}
headers= {}

sswitcher = {
        "ETH": 'ethereum',
        "BTC": 'bitcoin',
        "DAI": 'dai',
        "GBP": 'gbp',
        "ALGO" : 'algorand'
    }

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

# aList = list of JSON object with details about individual provinces
def convert_covid_news(aList):
    complete_news = []
    provinces = []
    confirmed_data = []
    recovered_data = []
    deaths_data = []
    # province > day> data     
    for element in aList:
        #print(element)
        for index in range(len(element)):
            province_data = element[index]
            print(province_data['date'])             
            if province_data['region']['province'] != '':
                provinces.append(province_data['region']['province']) 
                confirmed_data.append(province_data['confirmed'])
                recovered_data.append(province_data['recovered'])
                deaths_data.append(province_data['deaths'])
    
    confirmed = {
        "label": 'Confirmed',
        "type": "bar",
        # "backgroundColor": "#fce700",
        "data": confirmed_data,
        "fill" :"false"
    }
    recovered = {
        "label": 'Recovered',
        "type": "bar",
        # "backgroundColor": "#2cdd76",
        "data": recovered_data,
        "fill" :"false"
    }
    death = {
        "label": 'Deaths',
        "type": "bar",
        # "backgroundColor": "#ff0000",
        "data": deaths_data,
        "fill" :"false"
    }
     
    complete_news.append(confirmed) 
    complete_news.append(recovered)
    complete_news.append(death)
    complete_news.append(provinces)
    print(complete_news)
    return complete_news

class NewsClient:
    def __init__(self, api_key):
        # Connect to the CryptoControl API
        self.client = CryptoControlAPI(api_key)

    def get_coin_news(self, coin_code):
        return self.client.getTopNewsByCoin(coin_code)

    
    def get_news(self, currencies):          
        aDict = {'_id': '5f0c8fdb0b40f100190d2ec9', 'title': 'This Overhead Liquidity Region Could Propel Bitcoin Past $12,000', 'publishedAt': '2020-07-13T16:00:43.000Z', 'sourceDomain': 'newsbtc.com', 'url': 'https://cryptocontrol.io/r/api/article/5f0c8fdb0b40f100190d2ec9?ref=5f12c93922ee0f0018aae1b9', 'thumbnail': 'https://cloudfront.cryptocontrol.io/thumbnails/5f0c8fdb0b40f100190d2ec9-1594658779565.jpg'}
        news = {"ETH" : aDict , "ALGO" : aDict, "BTC" : aDict, "DAI" : aDict}
        # print(news)
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
        
   
    
    def get_covid_news(self, start_date:str):
        date_time_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        news = []
        single_date = date_time_obj.date()
        # print(single_date.strftime("%Y-%m-%d"))        
        response = requests.request("GET", url = "https://covid-api.com/api/reports?date={}&iso=GBR".format(single_date.strftime("%Y-%m-%d")), headers=headers, data = payload)
        result = json.loads(response.text).get('data') 
        news.append(result)
        #return response.text.encode('utf8')
        news = convert_covid_news(news)
        print(news) 
        return news
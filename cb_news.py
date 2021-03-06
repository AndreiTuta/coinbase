from crypto_news_api import CryptoControlAPI
from datetime import timedelta

import datetime
import requests
import json

payload = {}
headers = {}

currencies_switcher = {
    "ETH": 'ethereum',
    "BTC": 'bitcoin',
    "DAI": 'dai',
    "GBP": 'gbp',
    "ALGO": 'algorand'
}


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


# aList = list of JSON object (from API response) with details about individual provinces
# chartType = type of chart from chart.js to be generated
def convert_covid_news(aList, chartType):
    complete_news = []
    provinces = []
    confirmed_data = []
    recovered_data = []
    deaths_data = []
    # province > day> data     
    for element in aList:
        # print(element)
        for index in range(len(element)):
            province_data = element[index]
            if province_data['region']['province'] != '' :
                provinces.append(province_data['region']['province'])
                confirmed_data.append(province_data['confirmed'])
                recovered_data.append(province_data['recovered'])
                deaths_data.append(province_data['deaths'])

    confirmed = {
        "label": 'Confirmed',
        "type": chartType,
        "borderColor": "#fce700",
        # "backgroundColor" : "red",
        "data": confirmed_data,"fill":"true"
    }
    recovered = {
        "label": 'Recovered',
        "type": chartType,
        "borderColor": "#2cdd76",
        # "backgroundColor" : "red",
        "data": recovered_data,"fill":"false"
    }
    death = {
        "label": 'Deaths',
        "type": chartType,
        "borderColor": "#ff0000",
        # "backgroundColor" : "red",
        "data": deaths_data, "fill":"false"
    }

    complete_news.append(confirmed)
    complete_news.append(recovered)
    complete_news.append(death)
    complete_news.append(provinces)
    return complete_news


def get_news(currencies):
    a_dict = {'_id': '5f0c8fdb0b40f100190d2ec9',
              'title': 'This Overhead Liquidity Region Could Propel Bitcoin Past $12,000',
              'publishedAt': '2020-07-13T16:00:43.000Z', 'sourceDomain': 'newsbtc.com',
              'url': 'https://cryptocontrol.io/r/api/article/5f0c8fdb0b40f100190d2ec9?ref=5f12c93922ee0f0018aae1b9',
              'thumbnail': 'https://cloudfront.cryptocontrol.io/thumbnails/5f0c8fdb0b40f100190d2ec9-1594658779565.jpg'}
    news = {"ETH": a_dict, "ALGO": a_dict, "BTC": a_dict, "DAI": a_dict}
    # print(news)
    return news
    # TODO: Expand new debug mode as api takes long to load sometimes
    # news = {}
    # for coin in currencies:
    #     if(coin !="GBP"):
    #         coin_code = currencies_switcher[coin]
    #         news_array = self.get_coin_news(coin_code)
    #         news[coin] =  news_array

    # write_as_csv(news)

    # return news


def get_covid_news(start_date: str, iso: str, region: str):
    date_time_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    isos = "&iso={}".format(iso) if iso > '' else ''
    regions = "&region_province={}".format(region) if region > '' else ''
    news = []
    single_date = date_time_obj.date()
    response = requests.request("GET", url="https://covid-api.com/api/reports?date={}{}{}".format(
        single_date.strftime("%Y-%m-%d"), isos, regions), headers=headers, data=payload)
    result = json.loads(response.text).get('data')
    news.append(result)
    # return response.text.encode('utf8')
    news = convert_covid_news(news, "bar")
    print(news)
    return news


class NewsClient:
    def __init__(self, api_key):
        # Connect to the CryptoControl API
        self.client = CryptoControlAPI(api_key)

    def get_coin_news(self, coin_code):
        return self.client.getTopNewsByCoin(coin_code)

import datetime
import json


def write_as_csv(aDict):
    aDict['timestamp'] = str(datetime.datetime.now(datetime.timezone.utc))
    f = open('results/entry-news.csv', 'w')
    print(json.dumps(aDict))
    f.write(json.dumps(aDict) + ', ')
    f.close()

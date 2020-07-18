
import datetime
import json

def map_as_csv(aTuple):
    eg_tuple = ''

def write_as_csv(aTuple):
    aTuple['timestamp'] = str(datetime.datetime.now(datetime.timezone.utc))
    f = open('results/entry.csv', 'a')
    print(json.dumps(aTuple))
    f.write(json.dumps(aTuple) + ', ')
    f.close()

import datetime
import json


def write_as_csv(aTuple):
    aTuple['timestamp'] = str(datetime.datetime.now(datetime.timezone.utc))
    f = open('results/entry.csv', 'a')
    print(json.dumps(aTuple))
    f.write(json.dumps(aTuple) + '\n')
    f.close()
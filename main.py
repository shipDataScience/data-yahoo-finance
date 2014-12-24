import ystockquote
import datetime
import csv
import json
import collections
import os

today_string = datetime.date.today().strftime( "%Y-%m-%d")
config_string = os.environ["SDS_PLUGIN_CONFIG_JSON"]
config = json.loads(config_string)
outfile = config['reserved']['outFilePath']

tickers = ["GOOG", "AAPL", "MSFT"]
data = collections.defaultdict(dict)

for ticker in tickers:
  resp = ystockquote.get_historical_prices(ticker, '2014-04-01', today_string ) 
  for day, info in resp.items():
    data[day][ticker] = info['Close']

with open(outfile, 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter='\t')
  writer.writerow(["Date"] + [ ticker for ticker in tickers ] )
  for day in sorted(data.keys()):
    writer.writerow( [day] + [data[day].get(ticker) for ticker in tickers ] )



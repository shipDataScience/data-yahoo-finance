import ystockquote
import datetime
import csv
import json
import collections
import os
import pandas
import time

config_string = os.environ["SDS_PLUGIN_CONFIG_JSON"]
config = json.loads(config_string)
outfile = os.environ["SDS_OUTPUT_PATH"]

if config.get('tickers'):
  tickers = config['tickers']
else:
  tickers = ['GOOG', 'QQQ', 'DBC']

if config.get('lags'):
  lags = config['lags']
else:
  lags = [1,3,5]

if config.get("startDate"):
  start_date = config["startDate"]
else:
  start_date = '2014-04-01'

if config.get("endDate"):
  end_date = config["endDate"]
else:
  end_date = datetime.date.today().strftime( "%Y-%m-%d")

data = pandas.DataFrame()

# Raw Data
for ticker in tickers:
  time.sleep(3)
  resp = ystockquote.get_historical_prices(ticker, start_date, end_date ) 
  series = pandas.Series()
  for day, info in resp.items():
    series = series.set_value(day, info['Close'])
  data[ticker] = series

data.index.names = ['Date']
data.sort_index(inplace=True)

# Lagged data
for ticker in tickers:
  for lag in lags:
    data[ticker + "_LAG_" + str(lag)] = data[ticker].shift(lag)

data.to_csv(outfile, sep="\t")



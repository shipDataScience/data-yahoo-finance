import ystockquote
import datetime
import csv
import json

today_string = datetime.date.today().strftime( "%Y-%m-%d")
outfile = os.environ["SDS_PLUGIN_CONFIG_JSON"]["reserved"]["outFilePath"]

resp = ystockquote.get_historical_prices('GOOG', '2010-01-01', today_string ) 

out = []
for day, data in resp.items()
  out.append( [day, data["close"] ] )

with open(outfile, 'wb') as csvfile:
  writer = csv.writer(csvfile, delimiter='\t')
  for row in out:
    writer.writerow(row)



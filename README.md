YAHOO Finance Connect Module
==============

An example data plugin for Ship Data Science.
This plugin grabs the daily closing stock quote for an arbitrary list of stocks 
using the Yahoo Finance API. 

Check out the demo model we've set up using this data source: [Tech Stocks Demo Model](https://github.com/shipDataScience/model-tech-stocks)

To use, simply add config like the following code to your model's .shipit.json.
You can automatically fill out the config at the [Ship Data Science Cofigurator](http://configurator.shipdatascience.com).

All settings inside the 'config' namespace are optional with sensible defaults.
If endDate is left unset, the data will be pulled until the present day.

```
"data" : {
  "module": {
    "repositoryOwner": "shipDataScience",
    "repositoryName": "data-yahoo-finance",
    "repositoryBranch": "master"
  },
  "config" : {
    "tickers" : ["AAPL", "GOOG", "MSFT"], 
    "lags" : [1,3,5],
    "startDate" : "2014-04-01",
    "endDate" : "2014-04-02"
  }
}
```

FAQ
--------

Be aware this plugin runs unauthenticated requests against Yahoo's Finance API and
is subject to rate limits and continuing support of the API by Yahoo.
  
Security Note
----------

Be aware that this configuration information will appear in the .shipit.json file if you use this module. 
You should ensure that your project repository on Github is set to private access only. 


License
-----------
Copyright (c) 2015 Ship Data Science LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




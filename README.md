YAHOO Finance Data Grabber
==============

An example data plugin for Ship Data Science.
This plugin grabs the daily closing stock quote for an arbitrary list of stocks 
using the Yahoo Finance API. 

Check out the demo model we've set up using this data source: [Tech Stocks Demo Model](https://github.com/shipDataScience/model-tech-stocks)

To use, simply add config like the following code to your model's .shipit.json.
All settings inside the 'config' namespace are optional with sensible defaults.
If endDate is left unset, the data will be pulled until the present day.

```
"data" : {
  "cloneUrl" : "git@github.com:shipDataScience/data-yahoo-finance.git",
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
Here is what happens to your data when you run a build:

 - A fresh virtual machine is spun up on AWS. This VM is only used for this build and deleted on termination.
 - Your model is cloned to the box using your Github oauth token.
 - This data plugin's environment is built using the Dockerfile.
 - This data plugin's docker container is started and the script writes your data to a mounted volume (a segregated file directory on your VM).
 - The docker container image is deleted and the data plugin is done.
 - Each monitoring plugin container you have selected is run sequentially and given access to the data directory.
 - The plugin results are sent to our server and the VM is terminated.
  



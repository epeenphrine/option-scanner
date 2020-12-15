#!/bin/env python3
#%%
#run callie_scripts with run.py
from scrapers.ipoScrape import start_scrape
from callie_scripts.make_options_req import MakeRequest 

start_scrape()
make_request = MakeRequest
#%%
#from callie_scripts import get_earnings_date



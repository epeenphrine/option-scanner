#!/bin/env python3
#%%
#run callie_scripts with run.py
from callie_scripts.make_options_req import MakeRequest 

make_request = MakeRequest
#%%
from scrapers.ipoScrape import start_scrape
start_scrape()
#from callie_scripts import get_earnings_date



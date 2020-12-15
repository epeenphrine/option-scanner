#!/bin/env python3
#%%
#run callie_scripts with run.py
from scrapers.ipoScrape import start_scrape
from option_scripts.get_options_from_tda import MakeRequest 

start_scrape()
make_request = MakeRequest
#%%
#from callie_scripts import get_earnings_date
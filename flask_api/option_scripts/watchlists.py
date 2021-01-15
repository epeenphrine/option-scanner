#%%
import re
import csv
import json 
import pandas as pd 

def get_nasdaq_list():
    """
    use nasdaq listings from nasdaq api and then use cboe options listings to filter companies with option chains
    """
    df = pd.read_csv('/tmp/data/cboe_all_options.csv')
    df_dict = df.to_dict('records')
    options_list = [company[' Stock Symbol'] for company in df_dict]
    with open('/tmp/json/nasdaq_listings_sorted_volume.json', 'r') as f:
        nasdaq_listings =  json.load(f)
    tickers = [company['symbol'] for company in nasdaq_listings]
    tickers_filter = [ticker for ticker in tickers if ticker in options_list]
    return tickers_filter
def get_short_list():
    '''returns a shorter list because it checks for weeklies'''
    df = pd.read_csv('/tmp/data/cboe_weeklies.csv')
    df_dict = df.to_dict('records')
    options_list = [company[' Stock Symbol'] for company in df_dict]
    watchlist_filename = "/tmp/json/nasdaq_listings_sorted_volume.json"
    with open("/tmp/json/nasdaq_listings_sorted_volume_short.json", 'r') as f:
        nasdaq_listings = json.load(f)
    tickers = [company['symbol'] for company in nasdaq_listings]
    tickers_filter = [ticker for ticker in tickers if ticker in options_list]
    return tickers_filter
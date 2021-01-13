#%%
import re
import csv
import json 

with open('./error_list.json', 'r') as f:
    error_list = json.load(f)

def get_nasdaq_list():
    '''use big watchlist which has 3k ish companies'''
    with open('/tmp/data/nasdaqlisted.txt', 'r') as f:
        company_list = f.read().splitlines()
    tickers = []
    for item in company_list:
        ticker = item.split('|')[0]
        if ticker not in error_list:
            tickers.append(ticker)
    return tickers

def get_short_list():
    '''use short watchlist which has < 300 ish companies'''
    watchlist_filename = "./2020-11-04-watchlist.csv"
    tickers = []
    with open(watchlist_filename, newline="") as watchlist_file:
        fr = csv.reader(watchlist_file, delimiter=',', quotechar='|')
        for row in fr:
            if len(row) > 1 and row[0] != "Symbol" and row[0] not in error_list:
                tickers.append(row[0])
    return tickers  
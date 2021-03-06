#%%
#from td.client import TDClient
import datetime
from pytz import timezone
import time
# from yahoo_earnings_calendar import YahooEarningsCalendar
import csv
from datetime import date
from config import client_id, redirect_uri, date_delta

import json
import os
import re
import requests 
from tqdm import tqdm
#custom module import
from watchlists import get_short_list, get_nasdaq_list

'''make request to tda and then save as json'''
date_delta = 60 
def get_front_date(date_delta):
    '''get nearest friday from date delta'''
    dates_list = []
    for i in range(0, date_delta):
        d = datetime.date.today()
        d += datetime.timedelta(i)
        if d.weekday() == 4:
            dates_list.append(str(d))
    #print(dates_list[-2])
    return dates_list[0]

def get_back_date(date_delta):
    '''get the next friday after front date'''
    dates_list = []
    for i in range(0, date_delta):
        d = datetime.date.today()
        d += datetime.timedelta(i)
        if d.weekday() == 4:
            dates_list.append(str(d))
    #print(dates_list[-1])
    return dates_list[-1]

# Create a new session, credentials path is optional.

date_delta = 60
front_date = get_front_date(date_delta)
back_date = get_back_date(date_delta)
# ========= check earnings calendar ==========
date_from = datetime.datetime.strptime(date.today().strftime('%Y-%m-%d') + " 05:00:00",  '%Y-%m-%d %X')
date_to = datetime.datetime.strptime(front_date + " " + "18:00:00", '%Y-%m-%d %X')

symbols = get_short_list()
symbols2 = get_nasdaq_list()
# Login to the session

option_chains_list = [

]
try:
    with open('./error_list.json','r') as f:
        error_list = json.load(f)
except: 
    print("error list probably doesn't exist locally... creating a empty error_list variable")
    error_list = []
done_list = []
def iter_requests(symbols, output_name):
    url = 'https://api.tdameritrade.com/v1/marketdata/chains'
    for symbol in tqdm(symbols):
        if symbol not in done_list:
            #print(symbol)
            opt_chain = {
                "apikey": client_id,
                'symbol': symbol,
                'contractType': 'CALL',
                'optionType': 'S',
                'fromDate': front_date,
                'toDate': back_date,
                'includeQuotes': True,
                'range': 'OTM',
                'strategy': 'SINGLE',
            }
            try:
                option_chains = requests.get(url,params=opt_chain).json()
                time.sleep(.5)
            except:
                # might be querying the API too quickly. wait and try again
                print("error getting data from TD retrying ...")
                time.sleep(7) # compeletely reset per second rule from TDA 
                option_chains = requests.get(url,params=opt_chain).json()
            try: 
                quote = option_chains['underlying']['mark']
            except:
                print('error getting options chains for', symbol)
                error_list.append(symbol)
            # print(option_chains)
            option_chains_list.append(option_chains)
            done_list.append(symbol)
            # with open(json_file_path, 'w') as f:
            #     json.dump(option_chains, f)
        # with open('callie_scripts/option_chains_list.json', 'w') as f:
        #     json.dump(option_chains_list, f)

        #time zone stuff and date time stuff
        tz = timezone('EST')
        d = str(datetime.datetime.now(tz))
        option_chains_dict = {
            "scanTime": d,
            "optionChainsList": option_chains_list
        } 
    print('script finished check option_scripts directory for json files')
    with open(f'/tmp/json/{output_name}.json', 'w') as f:
        json.dump(option_chains_dict, f)
    with open(f"./error_list.json", "w") as f:
        json.dump(error_list, f)
iter_requests(symbols, 'optionChainsList')
iter_requests(symbols2, 'optionChainsListLong')
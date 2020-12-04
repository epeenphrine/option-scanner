#%%
#from td.client import TDClient
import datetime
from pytz import timezone
import time
from yahoo_earnings_calendar import YahooEarningsCalendar
import csv
from datetime import date
from config import client_id, redirect_uri, date_delta

import json
import os
import re
import requests 

class MakeRequest:
    date_delta = 60 
    def get_front_date(date_delta):
        dates_list = []
        for i in range(0, date_delta):
            d = datetime.date.today()
            d += datetime.timedelta(i)
            if d.weekday() == 4:
                dates_list.append(str(d))
        #print(dates_list[-2])
        return dates_list[0]

    def get_back_date(date_delta):
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

    symbols = []
    watchlist_filename = "./callie_scripts/2020-11-04-watchlist.csv"
    with open(watchlist_filename, newline="") as watchlist_file:
        fr = csv.reader(watchlist_file, delimiter=',', quotechar='|')
        for row in fr:
            if len(row) > 1 and row[0] != "Symbol":
                symbols.append(row[0])

    # Login to the session

    option_chains_list = [

    ]

    url = 'https://api.tdameritrade.com/v1/marketdata/chains'
    for symbol in symbols:
        #print(symbol)
        opt_chain = {
            "apikey": client_id,
            'symbol': symbol,
            'contractType': 'CALL',
            'optionType': 'S',
            'fromDate': front_date,
            'toDate': back_date,
            #'strikeCount': 15,
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
            print('error getting stock quote for', symbol)

        print(option_chains)
        option_chains_list.append(option_chains)
    with open('callie_scripts/option_chains_list.json', 'w') as f:
        json.dump(option_chains_list, f)

    with open('callie_scripts/scan_time.json', 'w') as f:
        tz = timezone('EST')
        d = str(datetime.datetime.now(tz)) 
        json.dump(d, f)
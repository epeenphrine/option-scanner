#%%
import requests
from headers_generator import * 
import json 
import time
import pandas as pd 

HEADERS = make_headers()
print(HEADERS)
NASDAQ_LISTINGS_URL = 'https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=50&download=true'
res = requests.get(NASDAQ_LISTINGS_URL, headers=HEADERS, timeout=4).json()
nasdaq_listings = res['data']['rows']
df = pd.DataFrame.from_dict(nasdaq_listings)
df['volume'] = pd.to_numeric(df['volume'])
# print(df.dtypes)
df = df.sort_values(by=['volume'], ascending=False) #convert dtype for this column to sort volume
df = df[:1500] # get first 1.5k rows
df_dict = df.to_dict('records')
with open('/tmp/json/nasdaq_listings_sorted_volume.json', 'w') as f:
    json.dump(df_dict, f)
print(df_dict)
time.sleep(20)
#%%
import time
import requests
from headers_generator import *
import json 
HEADERS = make_headers()
year_month = time.strftime("%Y-%m")
NASDAQ_UPCOMING_IPO_URL = f'https://api.nasdaq.com/api/ipo/calendar?date={year_month}'
res = requests.get(NASDAQ_UPCOMING_IPO_URL, headers=HEADERS, timeout=4).json()['data']
upcoming = res['upcoming']['upcomingTable']['rows']
with open("/tmp/json/upcoming_ipos.json",'w') as f:
    json.dump(upcoming, f)
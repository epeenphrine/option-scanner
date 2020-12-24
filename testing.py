#%% get dat::a
import requests
dev_url = 'http://127.0.0.1:5000'
query_string = '20'
res = requests.get(f'{dev_url}/api/callieSpreads?days={query_string}').content
print(res)
#%% test query 
import requests 

dev_url = 'http://192.168.2.10:5000'
res = requests.get(f"{dev_url}/api/callieSpreads?days=20&totalVolume=500&openInterest=500").json()
print(res)

#%% TDA request example for option chains
import requests
from config import client_id 


url = 'https://api.tdameritrade.com/v1/marketdata/chains'

payload = { 
    "apikey": client_id, 
    "symbol": "SGMO",
    "optionType": 'S',
    'fromDate': "2020-12-02",  ## yyyy-mm-dd format
    'toDate': "2020-12-25",
    "includeQuotes": True,
    "range": "OTM",
    "strategy": "SINGLE"
}

res = requests.get(url, params=payload).json()
print(res)

#%% get watch list
import requests 
from config import client_id, tda_account_num
url = f"https://api.tdameritrade.com/v1/accounts/{tda_account_num}/watchlists"
payload= {
    "apikey": client_id
}
res = requests.get(url, params=payload).content
print(res)

#%% tda api request manual test
from option_scripts.get_options_from_tda import MakeRequest
start = MakeRequest

#%% earnings test
from option_scripts.get_earnings_date_from_yahoo import get_earnings
get_earnings()

#%% script tests
from option_scripts.filter_json import get_callies

days = 20
goldenRatio = .6
totalVolume = 200
openInterest = 200 

something = get_callies(date_delta=days,
            goldenRatio=goldenRatio,
            totalVolume=totalVolume, 
            openInterest=openInterest,)
print('testing for trigger')
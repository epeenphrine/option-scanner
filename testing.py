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

#%%
from callie_scripts.make_options_req import MakeRequest
start = MakeRequest

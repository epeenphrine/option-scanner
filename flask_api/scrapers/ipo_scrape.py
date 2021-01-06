#%%
import requests 
import random
import pandas as pd
import json

'''
scrapes and then saves as json
'''
url = "https://www.nasdaq.com/market-activity/stocks/screener"
url2 = "https://www.nasdaq.com/market-activity/ipos"
url3 = "https://www.marketwatch.com/tools/ipo-calendar"

user_agent_list = [
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
        'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
        'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
        'Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre'
]

user_agent_pick = random.choice(user_agent_list)
headers = {
    "User-Agent": user_agent_pick, 
}
res = requests.get(url3, headers=headers).content
df = pd.read_html(res)
this_week = df[1]
next_week = df[2]

# print(this_week)
# print(next_week)

this_week_dict = this_week.to_dict('records')
next_week_dict = next_week.to_dict('records')

with open('/tmp/json/this_week.json', 'w') as f:
    json.dump(this_week_dict, f)
with open('/tmp/json/next_week.json', 'w') as f:
    json.dump(next_week_dict, f)
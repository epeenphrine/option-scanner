#%%
import pandas as pd 
import json 

with open('/tmp/json/nasdaq_listings.json', 'r') as f:
    nasdaq_listings = json.load(f)['data']['rows']

df = pd.DataFrame.from_dict(nasdaq_listings)
df['volume'] = pd.to_numeric(df['volume'])
# print(df.dtypes)
df = df.sort_values(by=['volume'], ascending=False) #convert dtype for this column to sort volume
df = df[:1500] # get first 1.5k rows
df_dict = df.to_dict('records')
with open('/tmp/json/nasdaq_listings_sorted_volume.json', 'w') as f:
    json.dump(df_dict, f)
#%%
import time
year_month = time.strftime("%Y-%m")
print(year_month)
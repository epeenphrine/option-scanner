##future feature
#%%
import requests 
import json 

def get_halts():
    """
    use nyse api to get halts. Saves a json locally and then compares the new reponse to the local json to see if new halts or resumptions
    """
    res = requests.get('https://www.nyse.com/api/trade-halts/current?offset=0&max=50').json()
    halts = res['results']['tradeHalts']
    try:
        with open('/tmp/json/halts.json', 'r') as f:
            halts_json = json.load(f)
    except:
        halts_json = []
    new_halts = []
    for halt in halts:
        if halt not in halts_json:
            halts_json.append(halt)
            new_halts.append(halt)
    with open('/tmp/json/halts.json', 'w') as f:
        json.dump(halts_json, f)
    return new_halts 
get_halts()
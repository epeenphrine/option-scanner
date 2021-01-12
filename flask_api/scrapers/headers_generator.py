#%% 
import random
with open('user-agents.txt', 'r') as f:
    USER_AGENTS_LIST = f.read().splitlines()
ACCEPT_LANGUAGE = 'en/us'
ACCEPT_ENCODING = "br, gzip, deflate"
ACCEPT = "test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
REFERER = 'https://google.com'

def make_headers():
    '''generate random user agents'''
    headers = {
        'User-Agent': random.choice(USER_AGENTS_LIST), 
        'Accept-Language': ACCEPT_LANGUAGE,
        'Accept-Encoding': ACCEPT_ENCODING,
        'Accept': ACCEPT,  
        'Referer': REFERER
    }
    return headers

make_headers()
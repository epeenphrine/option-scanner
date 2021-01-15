#%% 
import random
##having issue with headers list, some user agents not working
with open('user-agents.txt', 'r') as f:
    USER_AGENTS_LIST = f.read().splitlines()
ACCEPT_LANGUAGE = 'en/us'
ACCEPT_ENCODING = "br, gzip, deflate"
ACCEPT = "test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
REFERER = 'https://google.com'
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
def make_headers():
    '''generate random user agents'''
    headers = {
        'User-Agent': USER_AGENT, 
        'Accept-Language': ACCEPT_LANGUAGE,
        'Accept-Encoding': ACCEPT_ENCODING,
        'Accept': ACCEPT,  
        'Referer': REFERER
    }
    return headers
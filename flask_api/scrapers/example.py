#%%%
import requests, pandas as pd, bs4 as bs 
from headers_generator  import make_headers
## for future uses
URL = "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=50&download=true"
res = requests.get(URL, headers=make_headers()).json()
rows = res['data'].keys()
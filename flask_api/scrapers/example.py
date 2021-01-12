#%%%
import requests, pandas as pd, bs4 as bs 
from headers_generator  import make_headers
## for future uses
URL = ""
res = requests.get(URL, headers=make_headers()).content
#%%%
import requests, pandas as pd, bs4 as bs 
from headers_generator  import make_headers
## for future uses
URL = ""
http://192.168.2.10:8081/res = requests.get(URL, headers=make_headers()).content
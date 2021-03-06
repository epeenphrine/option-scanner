#%%
from tokens import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import json
import tweepy

## example
## https://realpython.com/twitter-bot-python-tweepy/

# api = twitter.Api(consumer_key=API_KEY, ## consumer key > API_KEY
#                   consumer_secret=API_KEY_SECRET, ## consumer secret > API_SECRET_KEY
#                   access_token_key=ACCESS_TOKEN,
#                   access_token_secret=ACCESS_TOKEN_SECRET)
def get_tweet_urls():
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    handles = [
        'zerohedge', 
        'LiveSquawk', 
        'DeItaone',
        'elonmusk',
        'CitronResearch', 
        'pakpakchicken',
        'cnbcnow',
        'Trinhnomics',
        'firstsquawk',
        'Trade_The_News',
        'realwillmeade',
        'jimcramer',
        'PeterSchiff',
        'hoodietrades',
        'nope_its_lily',
        'alpharivelino',
    ]
    try:
        print('opening json')
        with open('/tmp/json/tweets.json', 'r') as f:
            tweet_urls = json.load(f) 
    except:
        tweet_urls= [

        ]
    new_tweets = [

    ]
    for handle in handles:
        try:
            handle_recent = api.user_timeline(handle, count=1)[0]
            tweet_url = f'https://twitter.com/{handle}/statuses/{handle_recent.id}'
            if tweet_url not in tweet_urls:
                tweet_urls.append(tweet_url)
                new_tweets.append(tweet_url)
        except:
            print('broke in handle in tweets.py')
    with open('/tmp/json/tweets.json','w') as f:
        json.dump(tweet_urls, f)
    return new_tweets 
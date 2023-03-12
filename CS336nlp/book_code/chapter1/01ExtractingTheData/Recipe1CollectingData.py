"""
As discussed, there are a lot of free APIs through which we can collect data
and use it to solve problems. We will discuss the Twitter API in particular
(it can be used in other scenarios as well).
"""
import numpy as np
import tweepy
import json
import pandas as pd
from tweepy import OAuthHandler

# credentials
consumer_key = "adjbiejfaaoeh"
consumer_secret = "had73haf78af"
access_token = "jnsfby5u4yuawhafjeh"
access_token_secret = "jhdfgay768476r"
# calling API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# Provide the query you want to pull the data. For example,
# pulling data for the mobile phone ABC
query ="ABC"

# Fetching tweets
Tweets = api.search(query, count = 10,lang='en',
exclude='retweets',tweet_mode='extended')

"""
The query above will pull the top 10 tweets when the product ABC is
searched. The API willpull English tweets since the language given is ‘en’
and it will exclude retweets.
"""


import twitter
import pandas as pd
from datetime import date, timedelta
pd.set_option('display.max_colwidth', 600)
today = date.today()
last_week = today - timedelta(days=7)

# Accessing the Twitter API #
def access_twitter_API():
    ck = 'rdzwb0dO8KtRdLSBjdcjaDDZV'
    cs = 'tDWA8sMzaiMxc24u97oV2OAlMAutnJXSosuCBJKd9o9ENbgC5E'
    atk = '28185124-0Aaz2oojuiAqta2TsMeA0d7vfjxeVfsri7YgdCcek'
    ats = 'zHjzYniHsqMkZZQ5PvThN33IFxbqUcEFIus0wRD6hcrRB'

    api = twitter.Api(consumer_key=ck,
                      consumer_secret=cs,
                      access_token_key=atk,
                      access_token_secret=ats)
    return api

# Get First Tweet Function #

def get_first_tweet(api, search_query):
    twitter_users = []
    tweet_time = []
    tweet_string = []
    tweet_id = []

    tweets = api.GetSearch(term=search_query, count=100, lang="en", since=today)

    for tweet in tweets:
            if (not tweet.retweeted) and ('RT @' not in tweet.text):
                twitter_users.append(tweet.user.name)
                tweet_time.append(tweet.created_at)
                tweet_string.append(tweet.text)
                tweet_id.append(tweet.id)
    df_first_tweets = pd.DataFrame({'Name': twitter_users, 'Time': tweet_time, 'Tweet': tweet_string, 'Tweet ID': tweet_id})

    return df_first_tweets

# Get Tweets Function #

def get_tweets(api, search_query, last_id):
    twitter_users = []
    tweet_time = []
    tweet_string = []
    tweet_id = []

    tweets = api.GetSearch(term=search_query, count=100, lang="en", max_id=last_id, since=last_week)

    for tweet in tweets:
            if (not tweet.retweeted) and ('RT @' not in tweet.text):
                twitter_users.append(tweet.user.name)
                tweet_time.append(tweet.created_at)
                tweet_string.append(tweet.text)
                tweet_id.append(tweet.id)
    df_tweets = pd.DataFrame({'Name': twitter_users, 'Time': tweet_time, 'Tweet': tweet_string, 'Tweet ID': tweet_id})

    return df_tweets
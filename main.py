# Importing Libraries and Setting Options #
import pandas as pd
pd.set_option('display.max_colwidth', 400)
from helper_fns import *
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from datetime import date, timedelta, datetime
import os


api = access_twitter_API()
search_query = 'sports direct'
df_tweets_all = pd.DataFrame()
latest_tweets = pd.DataFrame()

latest_tweets = get_first_tweet(api, search_query)
last_id = int(latest_tweets['Tweet ID'].head(1))

for tweet in range(0,30):
    df_tweets = get_tweets(api, search_query, last_id)
    last_id = int(df_tweets['Tweet ID'].tail(1))
    df_tweets_all = df_tweets_all.append(df_tweets, ignore_index=True)

df_tweets_all = df_tweets_all.drop_duplicates()
print(df_tweets_all['Tweet'])

# Sentiment Analysis #

#str_tweets = df_tweets_all['Tweet'].to_string(index=False)
#blob = TextBlob(str_tweets, analyzer=NaiveBayesAnalyzer())
#print(blob.sentiment)
company = 'sports_direct'

path = os.getcwd()
company_path = os.path.join(path, company)

if not os.path.exists(company_path):
    os.makedirs(company_path)

file_path = os.path.join(company_path, 'twitter.csv')
df_tweets_all.to_csv(file_path, index=False)

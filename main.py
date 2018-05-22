#!/usr/bin/python3
# Tweepyライブラリをインポート
import tweepy
# 各種キーをセット
CONSUMER_KEY = 'XXX'
CONSUMER_SECRET = 'XXX'
ACCESS_TOKEN = 'XXX'
ACCESS_SECRET = 'XXX'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

for mentions in tweepy.Cursor(api.mentions_timeline).items():
    # process mentions here
    print(mentions.entities.user_mentions.id)

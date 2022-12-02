import tweepy
import os
import json

TWITTER_API = os.environ.get("TWITTER_API")
TWITTER_SECRET = os.environ.get("TWITTER_SECRET")
TWITTER_BEARER = os.environ.get("TWITTER_BEARER")

auth = tweepy.OAuth2BearerHandler(TWITTER_BEARER)
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search_tweets, q="#KanyeWest").items(250)

tweets = [tweet for tweet in tweets]

with open("data.json", "w") as f:
	json.dump(tweets, f)

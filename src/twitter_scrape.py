import tweepy
import os
import json

TWITTER_API = os.environ.get("TWITTER_API")
TWITTER_SECRET = os.environ.get("TWITTER_SECRET")
TWITTER_BEARER = os.environ.get("TWITTER_BEARER")

api = tweepy.Client(TWITTER_BEARER)

tweets = api.search_recent_tweets("#KanyeWest", max_results=100)

tweets = [tweet.data for tweet in tweets.data]

with open("data.json", "w") as f:
	json.dump(tweets, f)

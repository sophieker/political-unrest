import tweepy
import os
import json

TWITTER_API = os.environ.get("TWITTER_API")
TWITTER_SECRET = os.environ.get("TWITTER_SECRET")
TWITTER_BEARER = os.environ.get("TWITTER_BEARER")

api = tweepy.Client(TWITTER_BEARER)

tweets_unrest1 = api.search_recent_tweets("#ukraine", max_results=100)
tweets_unrest2 = api.search_recent_tweets("manipulative algorithm", max_results=100)
tweets_unrest3 = api.search_recent_tweets("#TrumpCrimeFamily", max_results=100)
tweets_rest1 = api.search_recent_tweets("Halle", max_results=100)
tweets_rest2 = api.search_recent_tweets("Nadal", max_results=100)
tweets_rest3 = api.search_recent_tweets("lebron james", max_results=100)

tweets_unrest = [tweet.data for tweet in tweets_unrest1.data]
tweets_unrest += [tweet.data for tweet in tweets_unrest2.data]
tweets_unrest += [tweet.data for tweet in tweets_unrest3.data]
tweets_rest = [tweet.data for tweet in tweets_rest1.data]
tweets_rest += [tweet.data for tweet in tweets_rest2.data]
tweets_rest += [tweet.data for tweet in tweets_rest3.data]

with open("unrest_data.json", "w") as f:
	json.dump(tweets_unrest, f)

with open("rest_data.json", "w") as f:
	json.dump(tweets_rest, f)

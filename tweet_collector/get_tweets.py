import tweepy
import pymongo
import os



BEARER_TOKEN = os.getenv('BEARER_TOKEN')

client = pymongo.MongoClient(host="mongodb", port=27017)
db = client.twitter



client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True,
)


search_query = "GretaThunberg -is:retweet -is:reply -is:quote lang:de -has:links"

cursor = tweepy.Paginator(
    method=client.search_recent_tweets,
    query=search_query,
    tweet_fields=['author_id', 'created_at', 'public_metrics'],
).flatten(limit=20)

for tweet in cursor:
    db.tweets.insert_one(dict(tweet))
    print(tweet.text)

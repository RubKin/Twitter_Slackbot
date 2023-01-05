import pymongo
import time
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s  = SentimentIntensityAnalyzer()

time.sleep(10)

client = pymongo.MongoClient(host="mongodb", port=27017)

db = client.twitter

pg = create_engine('postgresql://rub:123456@postgresdb:5432/twitter', echo=True)

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

docs = db.tweets.find(limit=5)
for doc in docs:
    text = doc['text']
    sentiment = s.polarity_scores(doc['text'])
    print(sentiment)
    score = sentiment['compound']
    query = "INSERT INTO tweets VALUES (%s, %s);"
    pg.execute(query, (text, score))
    print(doc)


#print("Hello World")


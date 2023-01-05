# Twitter_Slackbot

In this project i built a pipeline with Docker which collects tweets and stores them in MongoDB. 
After being stored i perform a Sentiment Analysis with VaderSentimentAnaylsis giving each tweet a score of 1 or 0. Next the Tweets are stored in a PostgreSQL database though an ETL-Job. 
and finally the Slack-Bot publishes the last Tweet collected with a Sentiment Analysis Score.

STACK:
-Tweepy, requests, pymongo, VaderSentiment, SQLAlchemy, pandas, Psycopg2

-Docker

-MongoDB

-PostgresSQL

![Screenshot_Slackbot_1](https://user-images.githubusercontent.com/104838359/210833371-a46316c3-c185-4e28-a48a-6cb4b84ddc93.png)

![Screenshot_Slackbot_2](https://user-images.githubusercontent.com/104838359/210833394-dd49dad3-cd3e-4e48-bdad-acc5f31c5322.png)

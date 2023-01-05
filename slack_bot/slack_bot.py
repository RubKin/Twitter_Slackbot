import requests
import time
from sqlalchemy import create_engine
import psycopg2
import os

time.sleep(10)

#private
webhook_url_2 = "https://hooks.slack.com/services/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"


#pg = create_engine('postgresql://rub:123456@postgresdb:5432/twitter', echo=True)




connection = psycopg2.connect(user = "rub",
	                password = "123456",
			host = "postgresdb",
			port = "5432",
			database = "twitter")

cursor = connection.cursor()


cursor.execute('''SELECT * FROM tweets''')
tweet = cursor.fetchone()

    			      

data = {'text': tweet[0] + "\n" + "  ...THE FEELING IS...  " + str(tweet[1])}





requests.post(url=webhook_url_2, json = data)

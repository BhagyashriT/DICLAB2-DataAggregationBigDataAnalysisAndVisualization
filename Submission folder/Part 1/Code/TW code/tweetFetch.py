import tweepy
import json
import time
import datetime
import logging
logging.basicConfig()
#Twitter API credentials
consumer_key = "5mx9HVu1hI2LS2rUKEg30sSMM"
consumer_secret = "QYw5ZwSTe8hDqRihTj5dCO3G64EnwSZKgWP3vNoRPhiEfUj9R1"
access_key = "3253333722-W3502erKdX2tXk03dygEKsIRG6D97N14OQqgHJB"
access_secret = "zvH2WKmft76R92PEanE4MDZcGzopRyofXSoAtLLdBEF2X"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# searchquery1 = ["\"Marvel\"OR\"Avengers\"OR\"Game of Thrones\"OR\"Academy Awards\"-RT",
# "\"Star Wars\"OR\"Fiction movies\"OR\"Action movies\"OR\"Drama\" -RT"]
# searchquery1 = ['Marvel','Avengers','Game of Thrones','Academy Awards','Star Wars','Fiction movies','Drama movies','Action movies']
searchquery1 = ['Movies']
for query in searchquery1:
    print("Downloading for topic: "+query)
    file = open(query+'.json','w')
    tweetCount = 0

    # tweets = api.search(q="\""+query+"\""+"-RT", lang="en",geocode="39.7837304,-100.4458825,5000mi")
    tweets = tweepy.Cursor(api.search, q="\"Movies\""+"-RT", lang="en", geocode="39.7837304,-100.4458825,5000mi").items()
    while True:
        try:
            tweet = tweets.next()
            jsonToWrite = json.dumps(tweet._json)
            file.write(jsonToWrite+"\n")
            tweetCount += 1
            if tweetCount >= 25000:
                break
        except StopIteration:
            print("Breaking out of while")
            break
        except tweepy.TweepError:
            print("Waiting for 16 seconds")
            time.sleep(16 * 60)

    print("Total tweets collected: "+str(tweetCount))
    # for tweet in tweets:
    #     try:
    #
    #         print(tweet._json)
    #         jsonToWrite = json.dumps(tweet._json)
    #         file.write(jsonToWrite+"\n")
    #         # json.dump(tweet._json, file, indent=0, sort_keys=True)
    #     except tweepy.TweepError:
    #         print("Sleeping for 16 minutes")
    #         time.sleep(16 * 60)
    # print("================================================================")


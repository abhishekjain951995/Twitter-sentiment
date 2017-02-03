import twitter as twitter
from textblob import TextBlob
from .models import SearchTerm, tweet_data
from datetime import datetime
from dateutil.parser import parse as parse_date


def saveTweets(search_word):
    consumer_key = 'SuMpOUvcjPybple68SR4RkCdm'
    consumer_secret = 'du05NY1Y5LiFAST57T2VqTvYFWelnHpXcFBYa2poak8P5COOFA'
    access_token = '100738477-A4LbTA3nfjyfOWZxFlODhnh71v8w2gZivHpE0TYE'
    access_token_secret = 'xMVA2wzmdJCmjwPmwXH5sSRBo1Lru7Bfmkrso9Ujl6d3I'

    auth = twitter.oauth.OAuth(access_token,access_token_secret,consumer_key,consumer_secret)
    twitter_api = twitter.Twitter(auth=auth)

    #Fetch Twitter tweets
    q = search_word.search_text
    count = 100
    location = "37.0902,95.7129,50mi"
    search_results = twitter_api.search.tweets(q=q,count=count, location=location)
    statuses = search_results["statuses"]


    #Save tweets in Database 'tweet_data'
    for status in statuses:
        dt = parse_date(status['created_at'])
        blob = TextBlob(status["text"])
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        tweet_data.objects.create(search = search_word,
                        tweet_text = status["text"],
                        tweet_user = status["user"]["name"],
                        tweet_date = dt,
                        tweet_polarity = polarity,
                        tweet_subjectivity = subjectivity
                        )

    return len(statuses)

def getTweets(search_word):
    tweets = tweet_data.objects.filter(search = search_word).order_by("tweet_date")
    return tweets

def getPolarity(tweets):
    positive = 0
    negetive = 0
    totalpos = 0
    totalneg = 0
    totalneu = 0
    for tweet in tweets:
        polarity = tweet.tweet_polarity
        if(polarity>0):
            positive += polarity
            totalpos += 1
        elif(polarity<0):
            negetive += -polarity
            totalneg += 1
        else :
            totalneu += 1
    total = totalpos + totalneu + totalneg
    totalpos /= total/100
    totalneg /= total/100
    totalneu /= total/100

    return totalpos,totalneg,totalneu,positive,negetive

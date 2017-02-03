import twitter
from textblob import TextBlob
from .models import SearchTerm, Tweets




def getTweets(search_word):
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

    #Save tweets in Database 'feed'
    for status in statuses:
        blob = TextBlob(status["text"])
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        search_word.tweet_data_set.create(tweet_text = status["text"],
                                    tweet_user = status["user"]["name"]
                                    tweet_date = status['created_at'],
                                    tweet_polarity = polarity,
                                    tweet_subjectivity = subjectivity)

    return len(statuses)

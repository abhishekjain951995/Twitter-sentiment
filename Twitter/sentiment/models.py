from __future__ import unicode_literals

from django.db import models


class SearchTerm(models.Model):
    search_text = models.CharField(max_length=200)

    def __str__(self):
        return self.search_text


class tweet_data(models.Model):
    search = models.ForeignKey(SearchTerm, on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=200)
    tweet_user = models.CharField(max_length=200)
    tweet_date = models.DateTimeField('date published')
    tweet_polarity = models.DecimalField('Sentiment', max_digits=9, decimal_places=2, default=0)
    tweet_subjectivity = models.DecimalField('Sentiment', max_digits=9, decimal_places=2, default=0)




class Tweets(models.Model):
    search = models.ForeignKey(SearchTerm, on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=200)
    def __str__(self):
        return self.tweet_text

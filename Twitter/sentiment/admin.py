from django.contrib import admin

from .models import SearchTerm,Tweets

admin.site.register(SearchTerm)

admin.site.register(Tweets)

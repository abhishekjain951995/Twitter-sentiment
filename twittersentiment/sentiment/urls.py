from django.conf.urls import url

from . import views

app_name = 'sentiment'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]

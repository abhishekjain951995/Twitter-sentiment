from models import SearchTerm, Tweets, tweet_data
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import utils
from django.views.decorators.csrf import csrf_exempt



def index(request):
    latest_search_list = SearchTerm.objects.all()
    template = loader.get_template('sentiment/index.html')
    context = {
        'latest_search_list': latest_search_list,
    }
    return render(request,'sentiment/index.html',context)


def senti_search(request):
    search_word = SearchTerm.objects.create(search_text = request.POST['term'])
    print("Seacrh term Saved")
    utils.saveTweets(search_word)
    print("Tweets Saved")
    tweets = utils.getTweets(search_word)
    print("Tweets Retrieved")
    print type(tweets)
    positivePercent, negetivePercent, neutralPercent, positiveTotal, negetiveTotal = utils.getPolarity(tweets)
    return render(request,'sentiment/donutchart.html',{ 'tweets':tweets,
                                                        'positiveTotal':positiveTotal,
                                                        'negetiveTotal':negetiveTotal,
                                                        'neutralPercent':neutralPercent,
                                                        'positivePercent':positivePercent,
                                                        'negetivePercent':negetivePercent
                                                        })



    #return render(request, 'sentiment/charts.html',{'tweets':tweets})



def detail(request, search_id):
    search = get_object_or_404(SearchTerm, pk=search_id)
    return render(request, 'sentiment/detail.html', {'search': search})


def results(request, search_id):
    response = "You're looking at the results of search %s."
    search = get_object_or_404(SearchTerm, pk=search_id)
    return render(request, 'sentiment/results.html', {'search': search})

def vote(request, search_id):
    search = get_object_or_404(SearchTerm, pk=search_id)
    try:
        new_term = request.POST['term']
    except (KeyError):
        # Redisplay the search voting form.
        return render(request, 'sentiment/detail.html', {
            'search': search,
            'error_message': "You didn't write new term.",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('sentiment:results', args=(search.id,)))

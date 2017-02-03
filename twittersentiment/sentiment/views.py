from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
#from django.views.decorators.csrf import csrf_protect

from .models import Choice, Question

from .forms import NameForm

def index(request):
    if request.method=='POST':
        template = loader.get_template('sentiment/index.html')
        return HttpResponse(template.render(request))
        print "Hello IF"
    else:
        print "Hello Else"
        template = loader.get_template('sentiment/index.html')
        return HttpResponse(template.render(request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def vote(request, question_id):
    if request.method=='POST':
        print "It was a post request"
    else:
        print "It was a get Request"
    # try:
    #     searchedWord = request.POST['search']
    #     return HttpResponse("the search was %s"% searchedWord)
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return HttpResponse("Something went wrong")
    # else:
    #
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    return HttpResponse("HOLA")

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})





# def save_to_db (request):
#    var => db

# def show_to_user (request):
#    return => fatch from db

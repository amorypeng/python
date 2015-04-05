from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world")

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("question does not exist")	
	return render(request, 'polls/detail.html', {'question': question})
	
def results(request, question_id):
	return HttpResponse("results of question %s." % question_id)
	
def vote(request, question_id):
	return httpResponse("voting on question %s." % question_id)
	
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {'latest_question_list': latest_question_list, })
	
	return HttpResponse(template.render(context))
	
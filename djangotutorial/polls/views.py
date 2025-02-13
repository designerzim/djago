from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question

polls_index = "polls/index.html"


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    # output = ", ".join([q.question_text for q in latest_question_list])
    return render(request, polls_index, context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, polls_index, {"question": question})


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're looking at the results of {question_id}")

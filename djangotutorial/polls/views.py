from django.db.models import F
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice

polls_index = "polls/index.html"
polls_details = "polls/detail.html"
polls_results = "polls/results.html"


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    # output = ", ".join([q.question_text for q in latest_question_list])
    return render(request, polls_index, context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, polls_details, {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, polls_results, {"question": question})


def vote(request, question_id):
    """
    references polls:vote 'action' in details.html
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        # gets 'choice' id
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # increment votes by 1
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

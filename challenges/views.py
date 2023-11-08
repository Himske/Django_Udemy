from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Eat only meat for an entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Eat only meat for an entire month!",
    "april": "Eat only meat for an entire month!",
    "may": "Eat only meat for an entire month!",
    "june": "Eat only meat for an entire month!",
    "july": "Eat only meat for an entire month!",
    "august": "Eat only meat for an entire month!",
    "september": "Eat only meat for an entire month!",
    "october": "Eat only meat for an entire month!",
    "november": "Eat only meat for an entire month!",
    "december": None,
}

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request: HttpRequest, month: int) -> HttpResponseRedirect | Http404:
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except Exception:
        raise Http404()


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse | Http404:
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month": month})
    except Exception:
        raise Http404()

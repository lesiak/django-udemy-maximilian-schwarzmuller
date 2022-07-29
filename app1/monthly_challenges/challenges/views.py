from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    'january': 'January challenge',
    'february': 'February challenge',
    'march': 'March challenge',
    'april': 'April challenge',
    'may': 'May challenge',
    'june': 'June challenge',
    'july': 'July challenge',
    'august': 'August challenge',
    'september': 'September challenge',
    'october': 'October challenge',
    'november': 'November challenge',
    'december': None,
}


def index(request):
    return render(request, "challenges/index.html", {
        "months": list(monthly_challenges.keys())
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month - 1]
        redirect_path = reverse('month-challenge', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except IndexError:
        raise Http404()


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            'month': month,
            'challenge_text': challenge_text
        })
    except KeyError as e:
        raise Http404()

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

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
    'december': 'December challenge',
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month - 1]
        return HttpResponseRedirect('/challenges/' + redirect_month)
    except IndexError:
        return HttpResponseNotFound(f"Month {month} is not supported")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except KeyError as e:
        return HttpResponseNotFound(f"Month {e} is not supported")

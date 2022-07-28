from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    'december': 'December challenge',
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month - 1]
        redirect_path = reverse('month-challenge', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except IndexError:
        return HttpResponseNotFound(f"<h1>Month {month} is not supported</h1>")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except KeyError as e:
        return HttpResponseNotFound(f"<h1>Month {month} is not supported</h1>")

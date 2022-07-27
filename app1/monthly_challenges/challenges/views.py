from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    if month == 'january':
        return HttpResponse('January challenge!')
    elif month == 'february':
        return HttpResponse('February challenge')
    else:
        return HttpResponseNotFound("This month is not supported")

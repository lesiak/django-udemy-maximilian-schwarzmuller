from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
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


def index(request):
    def list_item(month: str):
        redirect_path = reverse('month-challenge', args=[month])
        return f"<li><a href={redirect_path}>{month.capitalize()}</a></li>"
    list_items = (list_item(month) for month in monthly_challenges.keys())
    months_list = '\n'.join(list_items)
    response_data = f"""
    <ul>
        {months_list}
    </ul>
    """
    return HttpResponse(response_data)


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
        # response_data = f"<h1>{challenge_text}</h1>"
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except KeyError as e:
        return HttpResponseNotFound(f"<h1>Month {month} is not supported</h1>")

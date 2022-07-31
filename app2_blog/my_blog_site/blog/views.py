from django.http import HttpResponse
from django.shortcuts import render


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return HttpResponse("All Posts")


def post_details(request, slug):
    return HttpResponse("Single Post: " + slug)
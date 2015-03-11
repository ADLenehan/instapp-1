from django.shortcuts import render
from instagram.client import InstagramAPI
from django.http import HttpResponse


def index(request):
    """The home page for the wom website"""

    context = {'title': 'InstApp'}
    return render(request, 'homepage.html', context)

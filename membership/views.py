from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse


# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'membership/membership.html')


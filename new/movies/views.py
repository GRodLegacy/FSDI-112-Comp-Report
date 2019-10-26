from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

from .models import Genre, Movie, Serie

# Create your views here.

"""
Working with DB using Django Models:

Get all: 
Movie.objects.all()

Get single (specific registry):
Movie.objects.get(id=1)

Filter (search)
Movie.objects.filter(in_stock > 0)


"""

def index(request):
    #all_movies = Movie.objects.all() # query to DB for all the movie entries
    return render(request, 'views/index.html', {'title': 'Home Page'})

def about(request):
    test = Genre()
    test.name = "some x"
    print(test)

    return render(request, 'views/about.html', {'name': 'Victor Gonzalez'})

def read_test(request):
    all = Genre.objects.all()
    print(all)
    names = ''
    for g in all:
        names += g.names
    return HttpResponse(names)
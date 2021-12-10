
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .scraper import search_movie
from .dbmanager import *


def index(request):
    template = loader.get_template('themovieapp/index.html')
    movie=search_movie('Warrior')
    print(movie)
    return render(request,'index.html',movie)

def search(request):
    template = loader.get_template('themovieapp/index.html')
    title=request.GET.get('title')
    advanced=request.GET.get('advanced')
    actor=request.GET.get('actor')
    year=request.GET.get('year')
    movie=movie_exists_db(title,year)
    if movie==None:
      print('not found in db')
      if advanced=='true' and (actor or year):
        movie = search_movie(title=title,advanced=True,actor=actor,year=year)
      else:
        movie=search_movie(title)
      save_movie_to_DB(movie)
    if movie:
        template = loader.get_template('themovieapp/index.html')
        return render(request, 'index.html', movie)
    else:
        template = loader.get_template('themovieapp/not_found.html')
        print(movie)
        return render(request, 'not_found.html')




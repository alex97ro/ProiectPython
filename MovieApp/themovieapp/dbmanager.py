from django.db import models
import json

class Movie(models.Model):
    title=models.CharField(max_length=500)
    cast=models.CharField(max_length=500)
    release_year=models.SmallIntegerField()
    thumbnail_url=models.CharField(max_length=1000)
    audience_score=models.SmallIntegerField()
    critics_score=models.SmallIntegerField()
    movie_reviews=models.CharField(max_length=1000)
    youtube_trailer=models.CharField(max_length=1000)


def movie_exists_db(title,year=None):
    print(title)
    if title and year:
        for movie in Movie.objects.all():
            if movie.title.replace(' ','').lower()==title.replace(' ','').lower() and movie.release_year==year:
             return dict({
                  'title':movie.title,
                  'cast':json.loads(movie.cast),
                  'release_year':movie.release_year,
                  'thumbnail_url':movie.thumbnail_url,
                  'audience_score':movie.audience_score,
                  'critics_score':movie.critics_score,
                  'movie_reviews':json.loads(movie.movie_reviews),
                  'youtube_trailer':movie.youtube_trailer
              })
    else:
        if title:
         for movie in Movie.objects.all():
            if movie.title.replace(' ', '').lower() == title.replace(' ','').lower():
                return dict({
                    'title': movie.title,
                    'cast': movie.cast.strip('][').split(", "),
                    'release_year': movie.release_year,
                    'thumbnail_url': movie.thumbnail_url,
                    'audience_score': movie.audience_score,
                    'critics_score': movie.critics_score,
                    'movie_reviews': movie.movie_reviews.strip('][').split("."),
                    'youtube_trailer': movie.youtube_trailer
                })

def save_movie_to_DB(dict):
    movie=Movie(title=dict['title'],cast=(dict['cast']),release_year=dict['release_year'],thumbnail_url=dict['thumbnail_url'],audience_score=dict['audience_score'],critics_score=dict['critics_score'],movie_reviews=(dict['movie_reviews']),youtube_trailer=dict['youtube_trailer'])
    movie.save()

#def save_to_db():
#get_JSON():

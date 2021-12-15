import uuid

from django.db import models
import json

class Movie(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=500)
    cast=models.CharField(max_length=500)
    release_year=models.CharField(max_length=10)
    thumbnail_url=models.CharField(max_length=1000)
    audience_score=models.CharField(max_length=10)
    critics_score=models.CharField(max_length=10)
    youtube_trailer=models.CharField(max_length=1000)

class MovieReview(models.Model):
    movie_id=models.ForeignKey('Movie', on_delete=models.CASCADE)
    review=models.CharField(max_length=500)


def movie_exists_db(title,year=None,actor=None):
    print(title)
    if title and year and actor:
        for movie in Movie.objects.all():
            if movie.title.replace(' ', '').lower() == title.replace(' ', '').lower() and movie.release_year == year and actor.replace(' ','').lower() in movie.cast.replace(' ','').lower():
                reviews = MovieReview.objects.filter(movie_id=movie.id)
                movie_reviews = []
                for review in reviews:
                    movie_reviews.append(review.review)
                return dict({
                    'title': movie.title,
                    'cast': movie.cast.replace('[', '').replace(']', '').replace('\'', '').split(","),
                    'release_year': movie.release_year,
                    'thumbnail_url': movie.thumbnail_url,
                    'audience_score': movie.audience_score,
                    'critics_score': movie.critics_score,
                    'movie_reviews': movie_reviews,
                    'youtube_trailer': movie.youtube_trailer
                })
    elif title and year:
        for movie in Movie.objects.all():
            if movie.title.replace(' ','').lower()==title.replace(' ','').lower() and movie.release_year==year:
                reviews = MovieReview.objects.filter(movie_id=movie.id)
                movie_reviews = []
                for review in reviews:
                    movie_reviews.append(review.review)
                return dict({
                  'title':movie.title,
                  'cast':movie.cast.replace('[','').replace(']','').replace('\'','').split(","),
                  'release_year':movie.release_year,
                  'thumbnail_url':movie.thumbnail_url,
                  'audience_score':movie.audience_score,
                  'critics_score':movie.critics_score,
                  'movie_reviews':movie_reviews,
                  'youtube_trailer':movie.youtube_trailer
              })
    else:
        if title:
         for movie in Movie.objects.all():
             if movie.title.replace(' ', '').lower() == title.replace(' ', '').lower():
                reviews=MovieReview.objects.filter(movie_id=movie.id)
                movie_reviews=[]
                for review in reviews:
                    movie_reviews.append(review.review)
                return dict({
                    'title': movie.title,
                    'cast': movie.cast.replace('[','').replace(']','').replace('\'','').split(","),
                    'release_year': movie.release_year,
                    'thumbnail_url': movie.thumbnail_url,
                    'audience_score': movie.audience_score,
                    'critics_score': movie.critics_score,
                    'movie_reviews': movie_reviews,
                    'youtube_trailer': movie.youtube_trailer
                })

def save_movie_to_DB(dict):
    if Movie.objects.filter(title=dict['title'],release_year=dict['release_year']):
        return False
    else :
        movie=Movie(title=dict['title'],cast=(dict['cast']),release_year=dict['release_year'],thumbnail_url=dict['thumbnail_url'],audience_score=dict['audience_score'],critics_score=dict['critics_score'],youtube_trailer=dict['youtube_trailer'])
        movie.save()
        for review in dict['movie_reviews']:
         movie_review=MovieReview(movie_id=movie,review=review)
         movie_review.save()

def movies_list():
    movie_list=[]
    for movie in Movie.objects.all():
            reviews = MovieReview.objects.filter(movie_id=movie.id)
            movie_reviews = []
            for review in reviews:
                movie_reviews.append(review.review)
            movie_list.append(dict({
                'title': movie.title,
                'cast': movie.cast.replace('[', '').replace(']', '').replace('\'', '').split(","),
                'release_year': movie.release_year,
                'thumbnail_url': movie.thumbnail_url,
                'audience_score': movie.audience_score,
                'critics_score': movie.critics_score,
                'movie_reviews': movie_reviews,
                'youtube_trailer': movie.youtube_trailer
            }))
    return movie_list

#def save_to_db():
#get_JSON():

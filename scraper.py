import json
import re
import requests
from bs4 import BeautifulSoup
import lxml
from difflib import SequenceMatcher
import random

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
def similarity_ratio(string1,string2):
    return SequenceMatcher(None, string1, string2).ratio()

def check_list(movies,movie_title):
    best_ratio_movie=movies[0]
    best_ratio = 0
    for movie in movies:
        titles=movie.find_all('a',slot='title')
        for title in titles:
            formated_title=title.decode_contents().replace(" ","").replace("\n","").lower()
            print(similarity_ratio(formated_title,movie_title))
            if formated_title == movie_title:
                return movie
            else:
                if similarity_ratio(movie_title,formated_title) > best_ratio:
                    best_ratio=similarity_ratio(movie_title,formated_title)
                    best_ratio_movie=movie
    return best_ratio_movie

def check_movie_tab(soup,title):
    movie_tab=soup.find_all('search-page-result',slot='movie')
    movie_tab=BeautifulSoup(str(movie_tab),'html.parser')
    movies=movie_tab.find_all('search-page-media-row')
    return check_list(movies,title)

def get_movie_page(url):
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')

    return soup


def get_audience_score(moviepageurl):
    soup=get_movie_page(moviepageurl)
    audience_score=soup.find_all('score-board')[0].get('audiencescore')
    if audience_score:
        return audience_score
    else:
        return '-'

def get_critic_score(moviepageurl):
    soup=get_movie_page(moviepageurl)
    critic_score=soup.find_all('score-board')[0].get('tomatometerscore')
    if critic_score:
        return critic_score
    else:
        return '-'

def get_critic_reviews(moviepageurl):
    soup=get_movie_page(moviepageurl)
    what_to_know=str(soup.find_all('section',id='what-to-know'))
    if BeautifulSoup(what_to_know,'html.parser').find_all('a'):
     review_url='https://www.rottentomatoes.com'+str(BeautifulSoup(what_to_know,'html.parser').find_all('a')[0].get('href'))
     request = requests.get(review_url, headers=headers)
     soup = BeautifulSoup(request.content, 'html.parser')
     reviews=soup.find_all('div',{'class':'review_table'})
     reviews=BeautifulSoup(str(reviews),'html.parser').find_all('div',{'class':'the_review'})
     reviews_list=[]
     for review in reviews:
         if 70 <= len(str(re.sub(' +', ' ', review.decode_contents().replace("\n", "").replace("\r", "")))) >= 20:
            reviews_list.append(str(re.sub(' +',' ',review.decode_contents().replace("\n","").replace("\r","").replace("[Full Review in Spanish]",""))))
     if len(reviews_list) > 2:
         return random.sample(reviews_list,3)
    else:
        return ['No reviews available for this movie!']

def get_thumbnail_src(moviepageurl):
    soup=get_movie_page(moviepageurl)
    return BeautifulSoup(str(soup.find_all('div',{'class':'movie-thumbnail-wrap'})[0]),'html.parser').find_all('img')[0].get('data-src')

def get_trailer(title,year):
   url='https://www.google.com/search?q='+(title.replace(' ','+')+'+'+year).replace(r'++','+')+'+trailer'
   trailer_ids=[]
   print(url)
   request = requests.get(url, headers=headers)
   links=re.findall(r'[(http(s)?):\/\/(www.\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)',request.text)
   for link in links:
       if link.startswith('/watch?v'):
           trailer_ids.append(link.replace("/watch?v=",""))
   return trailer_ids

def get_embeded_trailer(title,year):
    trailer_ids=get_trailer(title,year)
    return 'http://www.youtube.com/embed/'+trailer_ids[0]

def search_movie(title):
    urls=['https://www.rottentomatoes.com/search?search='+str(title)+'/']
    request = requests.get(urls[0], headers = headers)
    soup = BeautifulSoup(request.content,'html.parser')
    formated_title=title.replace(" ","").lower()

    movies=soup.find_all('search-page-media-row')
    if movies:
        movie=check_movie_tab(soup,formated_title)
        movie_title=str(movie.find_all('img')[0].get('alt'))
        cast=str(movie.get('cast')).split(',')
        #score=str(movie.get('tomatometerscore'))
        release_year=str(movie.get('releaseyear'))
        url=str(movie.find_all('a',slot='thumbnail')[0].get('href'))
        thumbnail_src = get_thumbnail_src(url)
        audience_score=get_audience_score(url)
        critic_score=get_critic_score(url)
        movie_reviews=list(get_critic_reviews(url))
        youtube_trailer=get_embeded_trailer(title,release_year)

        movie_dict=dict({
            'title':movie_title,
            'cast':cast,
            'release_year':release_year,
            'thumbnail_url':thumbnail_src,
            'audience_score':audience_score,
            'critics_score':critic_score,
            'movie_reviews':movie_reviews,
            'youtube_trailer':youtube_trailer
            })
       # print('\n'+'Ttile:'+movie_title+'\n'+'Movie Cast:'+str(cast)+'\n'+'Release Year:'+release_year+'\n')
        # print('Audience Score:' + get_audience_score(url))
        # print('\n' + 'Tomato Meter:' + get_critic_score(url))
        # print(get_critic_reviews(url))
        print(str(get_trailer(title,release_year))+'!!!!!!!!!')
        return movie_dict
    else:
        return False


#def save_to_DB(json):
print(search_movie('warrior'))
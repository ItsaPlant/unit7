
import random as rs
import datetime as dt
from typing import Iterator
from faker import Faker
fake = Faker()
mopics = []

class Movie:
    def __init__(self, name, year, genre):
        self.name = name
        self.year = year
        self.genre = genre
        #var
        self.count = 0 #może ustawic tu i zabrać z interfaceu

    def __repr__(self):
        return f"{self.name}"

    def play(self):
        self.count += 1

    def show(self):
        print(f"{self.name} {self.year}")

    def is_movie():
        return True

    def is_series():
        return False

####

class Series(Movie):
    def __init__(self, ep_num, ses_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ep_num = ep_num
        self.ses_num = ses_num
        

    def show(self):
        seson = self.ses_num
        if seson < 10:
            seson = f"0{seson}"
        epizode = self.ep_num
        if epizode < 10:
            epizode = f"0{epizode}"

        ep = f"S{seson}E{epizode}"
        print(f"{self.name} {ep}")

    def num_of_ep(self, title):
        count = len(search(title))
        return count

    def is_movie():
        return False

    def is_series():
        return True
      


#### ####

def add_mopic(type, title, year, genere, season_num=None, episode_num=None):
    """mov or ser"""
    if type == "mov":
        title = Movie(title, year, genere)
        mopic = title
    elif type == "ser":
        title = Series(title, year, genere, season_num, episode_num)
        mopic = title
    mopics.append(mopic)

def add_series(names, year, genre, ses_num):                                                                              
    for Iterator, name in enumerate(names):
        title = Series(Iterator, ses_num, name, year, genre)
        mopics.append(title)

def get_movies():
    movies = []
    for title in mopics:
        if title.is_movie:
            movies.append(title)
    return sorted(movies, key=lambda movie: movie.name)


def get_series():
    series = []
    for title in mopics:
        if title.is_series:
            series.append(title)
    return sorted(series, key=lambda movie: movie.name)


def search(title):
    film_list = [None]
    for mopic in mopics:
        if mopic.title == title:
            film_list.append(title)
    return film_list

def generate_views():
    mopic = rs.choice(mopics)
    mopic.count += rs.randint()

def boost_views():
    for i in range(10):
        generate_views()

def top_titles(contetnt_type):
    """ mov or ser"""
    _mopics = []
    if contetnt_type == "mov":
        _mopics = get_movies()
    elif contetnt_type == "ser":
        _mopics = get_series()
    else:
        _mopics = mopics

    count_dict = {}
    for mopic in _mopics:
        count_dict[mopic] = mopic.count
    count_dict = dict(sorted(count_dict.items(), key = lambda item: item[1]))
    return count_dict
        
####

print("Biblioteka filmów")

for i in range(100):
    add_mopic("mov", fake.country(), fake.year(), fake.day_of_week())
    titles = []
    for i in range(24):
        titles.append(fake.country())
    add_series(titles, fake.year(), fake.day_of_week(), rs.randint(1,20))


date = dt.datetime.now().isoformat()

print(f"Most mopular movies&series of today {date} ")
top = top_titles("ser")

for title in top:
    print(title, top[title])

import random as rs
mopics = []

class Movie:
    def __init__(self, name, year, genre):
        self.name = name
        self.year = year
        self.genre = genre
        #var
        self.count = 0 #może ustawic tu i zabrać z interfaceu

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

    def is_movie():
        return False

    def is_series():
        return True
      


#### ####

def add_mopic(type, title, year, genere, season_num=None, episode_num=None):
    """mov or ser"""
    if type == "mov":
        title = Movie(type, title, year, genere)
        mopic = title
    elif type == "ser":
        title = Series(type, title, year, genere, season_num, episode_num)
        mopic = title

    mopics.append(mopic)

def get_movies():
    movies = []
    for title in mopics:
        if title.is_movie:
            movies.append(title)
    return sorted(movies)

def get_series():
    series = []
    for title in mopics:
        if title.is_series:
            series.append(title)
    return sorted(series)

def search(title):
    for mopic in mopics:
        if mopic.title == title:
            return mopic
        return None

def generate_views():
    mopic = rs.choice(mopics)
    mopic.count += rs.randit()

def boost_views():
    for i in range(10):
        generate_views()

def top_titles():
    count_dict = []
    for mopic in mopics:
        count_dict[mopic] = (mopic.count)
    count_dict = dict(sorted(count_dict.items(), key = lambda item: item[1]))
    return count_dict
        


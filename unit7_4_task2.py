
import random as rs
mopics = []

class Movie:
    def __init__(self, name, year, genre, count):
        self.name = name
        self.year = year
        self.genre = genre
        self.count = count

    def play(self):
        self.count += 1

    def show(self):
        print(f"{self.name} {self.year}")


class Series(Movie):
    def __init__(self, ep_num, ses_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ep_num = ep_num
        self.ses_num = ses_num

    def play(self):
        super().play(self)

    def show(self): #############################DOKONCZYC STRINGI
        seson = self.ses_num
        epizode = self.ep_num
        ep = f"S{seson}E{epizode}"
        print(f"{self.name} {ep}")

def add_mopic(type, title, data):
    """mov or ser"""
    if type == "mov":
        title = title.Movie(data)
        mopic = title
    elif type == "ser":
        title = title.Movie(data)
        mopic = title

    mopics.append(mopic)

def get_movies():
    movies = []
    for title in mopics:
        is_Movie = isinstance(title, Movie)
        is_Series = isinstance(title, Series)

        Is_SERIES = (is_Movie * is_Series)
        if not Is_SERIES:
            movies.append(title)
    return sorted(movies)

def get_series():
    series = []
    for title in mopics:
        is_Movie = isinstance(title, Movie)
        is_Series = isinstance(title, Series)

        Is_SERIES = (is_Movie * is_Series)
        if Is_SERIES:
            series.append(title)
    return sorted(series)

def search(title):
    for _title in mopics:
        if title is _title:
            print("shall we play?")
            break
        else:
            print("no such title")

def generate_views():
    mopic = rs.choice(mopics)
    mopic.count += 100

def boost_views():
    for i in range(10):
        generate_views()

def top_titles():
    count_dict = []
    for mopic in mopics:
        count_dict[mopic] = (mopic.count)
    count_dict = dict(sorted(count_dict.items(), key = lambda item: item[1]))
    return count_dict
        


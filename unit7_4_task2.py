
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

    def play:
        super().play()

    def show(self): #############################DOKONCZYC STRINGI
        seson = self.ses_num
        epizode = self.ep_num
        ep = f"S{seson}E{epizode}"
        print(f"{self.name} {ep}")

def add_mopic(type):
    """mov or ser"""
    if type == mov:
        mopic = Movie(input('txtxtxt'))
    elif type == ser:
        mopic = Series(input("txtxtxt"))
    
    mopics.append(mopic)



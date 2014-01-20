__author__ = 'ekondareva'


class Album:
    def __init__(self,
                 name,
                 popularity,
                 href,
                 artist):
        self.name = name
        self.artist = artist
        self.popularity = popularity
        self.href = href

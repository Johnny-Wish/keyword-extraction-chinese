import os

DEFAULT_STOPWORDS_PATH = "dataset/stopwords.txt"


class Stopwords:
    def __init__(self, path=DEFAULT_STOPWORDS_PATH):
        if not os.path.isfile(path):
            raise IOError("{} is not a file".format(path))

        with open(path) as f:
            self.words = f.read().split()

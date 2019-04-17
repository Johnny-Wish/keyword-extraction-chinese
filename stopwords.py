import os

DEFAULT_STOPWORDS_PATH = os.path.join("dataset", "stopwords.txt")


class Stopwords:
    def __init__(self, path=DEFAULT_STOPWORDS_PATH):
        if not os.path.isfile(path):
            raise IOError("{} is not a file".format(path))

        with open(path) as f:
            self.words = f.read().split()


try:
    DEFAULT_STOPWORDS = Stopwords().words
except Exception as e:
    print(e)
    print("WARNING: DEFAULT_STOPWORDS fall back to empty")
    DEFAULT_STOPWORDS = []

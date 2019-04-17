import os
import jieba
from gensim.corpora import Dictionary
from stopwords import Stopwords


class Document:
    def __init__(self, path, stopwords=None, puncts=None):
        if not os.path.isfile(path):
            raise IOError("path {} is not a file".format(path))

        if stopwords is None:
            stopwords = []
        if puncts is None:
            puncts = []
        skipped = set(stopwords + puncts + ['\n'])

        with open(path) as f:
            raw_text = f.read()
        words = list(jieba.lcut(raw_text))

        self.tokens = [word for word in words if word not in skipped]
        self.ids = None

    def token2id(self, dictionary: Dictionary):
        self.ids = [dictionary.token2id[token] for token in self.tokens]

    def __len__(self):
        return len(self.tokens)

    def __str__(self):
        return "Document object with tokens {}".format(self.tokens.__str__())

    def __repr__(self):
        return "<{}>".format(self.__str__())
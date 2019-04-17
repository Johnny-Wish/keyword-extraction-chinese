import os
import jieba
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
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

    def set_ids(self, dictionary: Dictionary):
        self.ids = [dictionary.token2id[token] for token in self.tokens]

    def set_bow(self, dictionary: Dictionary):
        self.bow = dictionary.doc2bow(self.tokens)

    def set_tfidf_score(self, model: TfidfModel):
        self.tfidf_score = list(model[self.bow])

    def set_tfidf_keywords(self, n=5, dictionary: Dictionary = None):
        sorted_pairs = sorted(self.tfidf_score, key=lambda p: p[1], reverse=True)
        n = min(len(sorted_pairs), n)  # in case bow contains less than n words
        if dictionary is None:
            self.tfidf_keywords = [id for id, score in sorted_pairs[:n]]
        else:
            self.tfidf_keywords = [dictionary[id] for id, score in sorted_pairs[:n]]

    def __len__(self):
        return len(self.tokens)

    def __str__(self):
        return "Document object with tokens {}".format(self.tokens.__str__())

    def __repr__(self):
        return "<{}>".format(self.__str__())

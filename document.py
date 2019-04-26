import os
import jieba
import math
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.summarization.keywords import keywords


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
        self.spaced = " ".join(words)

        self.tokens = [word for word in words if word not in skipped]
        self.ids = None

    def set_ids(self, dictionary: Dictionary):
        self.ids = [dictionary.token2id[token] for token in self.tokens]

    def set_bow(self, dictionary: Dictionary):
        self.bow = dictionary.doc2bow(self.tokens)

    def set_tfidf_score(self, model: TfidfModel):
        self.tfidf_score = list(model[self.bow])

    @staticmethod
    def get_keyword_by_score(id_score_pair, n=5, dictionary=None, larger_is_better=True):
        sorted_pairs = sorted(id_score_pair, key=lambda p: p[1], reverse=larger_is_better)
        n = min(len(sorted_pairs), n)  # in case bow contains less than n words
        if dictionary is None:
            return [id for id, score in sorted_pairs[:n]]
        else:
            return [dictionary[id] for id, score in sorted_pairs[:n]]

    def set_tfidf_keywords(self, n=5, dictionary: Dictionary = None):
        self.tfidf_keywords = \
            Document.get_keyword_by_score(self.tfidf_score, n=n, dictionary=dictionary, larger_is_better=True)

    def set_spans(self):
        first_pos = {}
        spans = {}

        for pos, id in enumerate(self.ids):  # time complexity = O(n)
            if id not in first_pos:
                first_pos[id] = pos
            spans[id] = pos - first_pos[id]

        self.spans = spans

    def set_tfidf_span_score(self):
        weighting = lambda id: math.log(1 + self.spans[id])
        self.tfidf_span_score = [(id, score * weighting(id)) for id, score in self.tfidf_score]

    def set_tfidf_span_keywords(self, n=5, dictionary: Dictionary = None):
        self.tfidf_span_keywords = \
            Document.get_keyword_by_score(self.tfidf_span_score, n=n, dictionary=dictionary, larger_is_better=True)

    def set_textrank_keywords(self, n=5, ratio=1.0):
        try:
            kws = keywords(self.spaced, split=True, ratio=ratio, deacc=False)
            kws = [kw.replace(" ", "") for kw in kws]
            n = min(len(kws), n)
            self.textrank_keywords = kws[:n]
        except (IndexError, ZeroDivisionError) as e:
            print(e)
            print("setting textrank_keywords to empty")
            self.textrank_keywords = []

    def __len__(self):
        return len(self.tokens)

    def __str__(self):
        return "Document object with tokens {}".format(self.tokens.__str__())

    def __repr__(self):
        return "<{}>".format(self.__str__())

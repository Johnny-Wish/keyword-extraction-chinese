import os
from document import Document
from stopwords import DEFAULT_STOPWORDS
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
import numpy as np
import pandas as pd
import nltk
import jieba

DEFAULT_ALLOWED_EXTENSIONS = ['txt']
DEFAULT_CORPUS_PATH = "dataset/corpus"


class Corpus:
    def __init__(self, path, extensions=DEFAULT_ALLOWED_EXTENSIONS, stopwords=None, puncts=None):
        if not os.path.isdir(path):
            raise IOError("{} is not a directory".format(path))

        filenames = [f for f in os.listdir(path) if "." in f and f.rsplit(".")[-1] in extensions]
        self.documents = [Document(os.path.join(path, f), stopwords=stopwords, puncts=puncts) for f in filenames]
        self.tokens = [doc.tokens for doc in self.documents]
        self.ids = None
        self.bow = None
        self.tfidf_model = None
        self.tfidf_score = None
        self.tfidf_keywords = None
        self.spans = None
        self.tfidf_span_score = None
        self.dictionary = Dictionary(self.tokens)
        self.set_ids()
        self.set_bow()
        self.set_tfidf_model()
        self.set_tfidf_score()
        self.set_spans()

    def set_ids(self):
        for document in self.documents:
            document.set_ids(self.dictionary)
        self.ids = [doc.ids for doc in self.documents]

    def set_bow(self):
        for document in self.documents:
            document.set_bow(self.dictionary)
        self.bow = [doc.bow for doc in self.documents]

    def set_tfidf_model(self):
        self.tfidf_model = TfidfModel(self.bow, dictionary=self.dictionary)

    def set_tfidf_score(self):
        for document in self.documents:
            document.set_tfidf_score(self.tfidf_model)
        self.tfidf_score = [doc.tfidf_score for doc in self.documents]

    def set_tfidf_keywords(self, n=5, lookup=False):
        for document in self.documents:
            document.set_tfidf_keywords(n=n, dictionary=self.dictionary if lookup else None)
        self.tfidf_keywords = [doc.tfidf_keywords for doc in self.documents]

    def set_spans(self):
        for document in self.documents:
            document.set_spans()
        self.spans = [doc.spans for doc in self.documents]

    def set_tfidf_span_score(self):
        for document in self.documents:
            document.set_tfidf_span_score()
        self.tfidf_span_score = [doc.tfidf_span_score for doc in self.documents]

    def __len__(self):
        return len(self.documents)

    @property
    def lengths(self):
        return [len(doc) for doc in self.documents]


if __name__ == '__main__':
    corpus = Corpus(DEFAULT_CORPUS_PATH, stopwords=DEFAULT_STOPWORDS)

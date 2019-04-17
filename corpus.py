import os
from document import Document
from stopwords import Stopwords
from gensim.corpora import Dictionary
import numpy as np
import pandas as pd
import nltk
import jieba

DEFAULT_ALLOWED_EXTENSIONS = ['txt']


class Corpus:
    def __init__(self, path, extensions=DEFAULT_ALLOWED_EXTENSIONS, stopwords=None, puncts=None):
        if not os.path.isdir(path):
            raise IOError("{} is not a directory".format(path))

        filenames = [f for f in os.listdir(path) if "." in f and f.rsplit(".")[-1] in extensions]
        self.documents = [Document(os.path.join(path, f), stopwords=stopwords, puncts=puncts) for f in filenames]
        self.tokens = [doc.tokens for doc in self.documents]
        self.dictionary = Dictionary(self.tokens)


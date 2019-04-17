import os
import jieba
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

    def __str__(self):
        return "Document object with tokens {}".format(self.tokens.__str__())

    def __repr__(self):
        return "<{}>".format(self.__str__())


if __name__ == '__main__':
    stopwords = Stopwords().words
    document = Document("dataset/corpus/doc1.txt", stopwords=stopwords)

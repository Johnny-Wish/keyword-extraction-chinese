import os
from document import Document
from stopwords import DEFAULT_STOPWORDS
from gensim.corpora import Dictionary
from gensim.models import TfidfModel

DEFAULT_ALLOWED_EXTENSIONS = ['txt']
DEFAULT_DOC_CORPUS_PATH = os.path.join("dataset", "corpus-with-keywords", "docs")


class Corpus:
    def __init__(self, dir='', filenames=None, extensions=DEFAULT_ALLOWED_EXTENSIONS, stopwords=None, puncts=None):
        """
        :param dir: directory containing .txt files used as corpus
        :param filenames: ordered list of file paths, used together with`dir`
        :param extensions: legal extensions of documents, used to automatically fetch documents
        :param stopwords: list of stopwords
        :param puncts: list of punctuations
        """
        if filenames is None:  # auto-detect document files
            if not (isinstance(dir, str) and os.path.isdir(dir)):
                raise IOError("{} is not a directory".format(dir))
            filenames = [f for f in os.listdir(dir) if "." in f and f.rsplit(".")[-1] in extensions]

        self.documents = [Document(os.path.join(dir, f), stopwords=stopwords, puncts=puncts) for f in filenames]
        self.tokens = [doc.tokens for doc in self.documents]
        self.spaced = [doc.spaced for doc in self.documents]
        self.dictionary = Dictionary(self.tokens)
        self.ids = ...
        self.bow = ...
        self.tfidf_model = ...
        self.tfidf_score = ...
        self.tfidf_keywords = ...
        self.spans = ...
        self.tfidf_span_score = ...
        self.tfidf_span_keywords = ...
        self.textrank_keywords = ...

        # setup the model
        self._set_ids()
        self._set_bow()
        self._set_tfidf_model()
        self._set_tfidf_score()
        self._set_spans()
        self._set_tfidf_span_score()

    def _set_ids(self):
        for document in self.documents:
            document.set_ids(self.dictionary)
        self.ids = [doc.ids for doc in self.documents]

    def _set_bow(self):
        for document in self.documents:
            document.set_bow(self.dictionary)
        self.bow = [doc.bow for doc in self.documents]

    def _set_tfidf_model(self):
        self.tfidf_model = TfidfModel(self.bow, dictionary=self.dictionary)

    def _set_tfidf_score(self):
        for document in self.documents:
            document.set_tfidf_score(self.tfidf_model)
        self.tfidf_score = [doc.tfidf_score for doc in self.documents]

    def set_tfidf_keywords(self, n=5, lookup=False):
        for document in self.documents:
            document.set_tfidf_keywords(n=n, dictionary=self.dictionary if lookup else None)
        self.tfidf_keywords = [doc.tfidf_keywords for doc in self.documents]

    def _set_spans(self):
        for document in self.documents:
            document.set_spans()
        self.spans = [doc.spans for doc in self.documents]

    def _set_tfidf_span_score(self):
        for document in self.documents:
            document.set_tfidf_span_score()
        self.tfidf_span_score = [doc.tfidf_span_score for doc in self.documents]

    def set_tfidf_span_keywords(self, n=5, lookup=False):
        for document in self.documents:
            document.set_tfidf_span_keywords(n=n, dictionary=self.dictionary if lookup else None)
        self.tfidf_span_keywords = [doc.tfidf_span_keywords for doc in self.documents]

    def set_textrank_keywords(self, n=5, ratio=1.0):
        for document in self.documents:
            document.set_textrank_keywords(n=n, ratio=ratio)
        self.textrank_keywords = [doc.textrank_keywords for doc in self.documents]

    def __len__(self):
        return len(self.documents)

    @property
    def lengths(self):
        return [len(doc) for doc in self.documents]

import os

DEFAULT_ALLOWED_EXTENSIONS = ['txt']
DEFAULT_KEYWORD_CORPUS_PATH = os.path.join("dataset", "corpus-with-keywords", "keywords")


class KeywordCorpus:
    def __init__(self, dir="", filenames=None, extensions=DEFAULT_ALLOWED_EXTENSIONS):
        """
        :param dir: see `dir` of corpus.Corpus.__init__()
        :param filenames: see `filenames` of corpus.Corpus.__init__()
        :param extensions: see `extensions` of corpus.Corpus.__init()
        """
        if filenames is None:
            if not (isinstance(dir, str) and os.path.isdir(dir)):
                raise ValueError("{} is not valid directory".format(dir))

            filenames = [os.path.join(dir, f) for f in os.listdir(dir) if f.split(".")[-1] in extensions]

        self._keywords = []
        for filename in filenames:
            with open(os.path.join(dir, filename)) as f:
                self._keywords.append(f.read().strip().split())

    @property
    def keywords(self):
        return self._keywords

    @property
    def lengths(self):
        return [len(kw) for kw in self._keywords]


if __name__ == '__main__':
    kw_filenames = ["keywords{}.txt".format(i + 1) for i in range(20)]
    kwc = KeywordCorpus(dir=DEFAULT_KEYWORD_CORPUS_PATH, filenames=kw_filenames)

from corpus import Corpus, DEFAULT_DOC_CORPUS_PATH
from keywords import KeywordCorpus, DEFAULT_KEYWORD_CORPUS_PATH


def print_keywords(keywords):
    for idx, kws in enumerate(keywords):
        print("In article {}, keywords are: ".format(idx + 1), ", ".join(kws))


if __name__ == '__main__':
    doc_filenames = ["doc{}.txt".format(idx + 1) for idx in range(20)]
    kw_filenames = ["keywords{}.txt".format(idx + 1) for idx in range(20)]

    doc_corpus = Corpus(dir=DEFAULT_DOC_CORPUS_PATH, filenames=doc_filenames)
    kw_corpus = KeywordCorpus(dir=DEFAULT_KEYWORD_CORPUS_PATH, filenames=kw_filenames)

    doc_corpus.set_tfidf_keywords(10, lookup=True)
    doc_corpus.set_tfidf_span_keywords(10, lookup=True)
    doc_corpus.set_textrank_keywords(10)

    print("tfidf: ")
    print_keywords(doc_corpus.tfidf_keywords)
    print("tfidf with span: ")
    print_keywords(doc_corpus.tfidf_span_keywords)
    print("textrank: ")
    print_keywords(doc_corpus.textrank_keywords)

from corpus import Corpus, DEFAULT_DOC_CORPUS_PATH
from keywords import KeywordCorpus, DEFAULT_KEYWORD_CORPUS_PATH


def display_predicted_keywords(keywords):
    for idx, kws in enumerate(keywords):
        print("In article {}, keywords are: ".format(idx + 1), ", ".join(kws))


def compute_scores(keywords_true, keywords_pred, adjust_length=True):
    TP = TN = FP = FN = 1e-10  # to avoid division by zero in extreme cases
    for kws_true, kws_pred in zip(keywords_true, keywords_pred):
        if isinstance(adjust_length, bool) and adjust_length:
            length = min(len(kws_pred), len(kws_true))
            kws_pred = kws_pred[:length]
        elif isinstance(adjust_length, int) and adjust_length > 1:
            length = min(len(kws_pred), adjust_length)
            kws_pred = kws_pred[:length]

        for kw in kws_pred:
            if kw in kws_true:
                TP += 1  # true positive
            else:
                FP += 1  # false positive

        for kw in kws_true:
            if kw not in kws_pred:
                FN += 1  # false negative

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = 2 / (1 / precision + 1 / recall)
    return precision, recall, f1


if __name__ == '__main__':
    doc_filenames = ["doc{}.txt".format(idx + 1) for idx in range(20)]
    kw_filenames = ["keywords{}.txt".format(idx + 1) for idx in range(20)]

    doc_corpus = Corpus(dir=DEFAULT_DOC_CORPUS_PATH, filenames=doc_filenames)
    kw_corpus = KeywordCorpus(dir=DEFAULT_KEYWORD_CORPUS_PATH, filenames=kw_filenames)

    doc_corpus.set_tfidf_keywords(10, lookup=True)
    doc_corpus.set_tfidf_span_keywords(10, lookup=True)
    doc_corpus.set_textrank_keywords(10)

    predictions = {
        "tfidf": doc_corpus.tfidf_keywords,
        "tfidf with span": doc_corpus.tfidf_span_keywords,
        "textrank": doc_corpus.textrank_keywords,
    }

    for method, pred in predictions.items():
        print("{}: precision={}, recall={}, f1-score={}".format(method, *compute_scores(kw_corpus.keywords, pred)))
        display_predicted_keywords(pred)

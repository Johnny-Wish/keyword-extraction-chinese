# Keyword Extraction Implementation for Chinese Corpuses

[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

## Description

This is a simple implementation of keyword extraction algorithms for Chinese corpuses.
Implemented algorithms are:

- TF-IDF

- TF-IDF with word span information 

- Textrank 

## Dependencies

In the following are recommended (but not necessarily required) dependencies and versions:

1. Python interpreter `python` >= 3.6
2. Python package `gensim` >= 3.4.0
3. Python package `jieba` >=0.39

## Instructions

### Data

There are 20 demo documents along with keywords under the directory `dataset/corpus-with-keywords`, which have been used for debugging.

If more data (documents and keywords) are needed, place each document under `dataset/corpus-with-keywords/docs` and  `dataset/corpus-with-keywords/keywords` . Make sure each documents is encoded in `UTF-8` format (rather than `GBK`/`GB18030`) and has a `.txt` extension.

### Run

To run a test, first `cd` to the project directory and run the following command:

```bash
python main.py
```

### Platform

The program should run fine on MacOS, Linux and other *nix platforms.

In case the program is run a Windows machine, or any other system that uses a path separator other than the forward slash `/`, please change the path constants accordingly.

If any other error occurs, please [open an Issue](https://github.com/Johnny-Wish/keyword-extraction-chinese/issues/new) along with detailed description of the error. It is recommended to include the printed error message and descriptions on how to reproduce the error.

### Performance Summary

```
tfidf: precision=0.35820895522430385, recall=0.35820895522430385, f1-score=0.35820895522430385
tfidf with span: precision=0.3432835820900201, recall=0.3432835820900201, f1-score=0.3432835820900201
textrank: precision=0.15000000000116664, recall=0.13432835821004677, f1-score=0.14173228346569533
```

### Demo Output

For a demo output, check out [this file](demo-output.md).


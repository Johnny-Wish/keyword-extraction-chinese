# Keyword Extraction Implementation for Chinese Corpuses

## Description

This is a simple implementation of keyword extraction / text summarization algorithms for Chinese corpuses.
Implemented algorithms are:

- (Keyword Extraction) TF-IDF

- (Keyword Extraction) TF-IDF with word span information 

- (Text Summarization) Textrank 

## Instructions

### Run

To run a test, first `cd` to the project directory and run

```bash
python corpus.py
```

### Data

There are 3 demo documents under the directory `dataset/corpus`, which have been used for debugging.

If more data (documents) are needed, place each document under `dataset/corpus`. Make sure each documents is encoded in `UTF-8` format (rather than `GBK`/`GB18030`) and has a `.txt` extension.

### Platform

The program should run fine on MacOS, Linux and other *nix platforms.

In case the program is run a Windows machine, or any other system that uses a path separator other than the forward slash `/`, please change the path constants accordingly.

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

There are 3 demo documents under the directory `dataset/corpus`, which have been used for debugging.

If more data (documents) are needed, place each document under `dataset/corpus`. Make sure each documents is encoded in `UTF-8` format (rather than `GBK`/`GB18030`) and has a `.txt` extension.

### Run

To run a test, first `cd` to the project directory and run the following command:

```bash
python corpus.py
```

### Platform

The program should run fine on MacOS, Linux and other *nix platforms.

In case the program is run a Windows machine, or any other system that uses a path separator other than the forward slash `/`, please change the path constants accordingly.

If any other error occurs, please [open an Issue](https://github.com/Johnny-Wish/keyword-extraction-chinese/issues/new) along with detailed description of the error. It is recommended to include the printed error message and descriptions on how to reproduce the error.

### Demo Output

```
Building prefix dict from the default dictionary ...
Loading model from cache /var/folders/jr/qgh_hd1945bb_g0k8fwy_gn00000gp/T/jieba.cache
Loading model cost 0.796 seconds.
Prefix dict has been built succesfully.
Using tf-idf score:
In article 1, keywords are:  有赞, 时间, 想, 规定, 工作
In article 2, keywords are:  利益, 精神, 明星, 高大, 未来
In article 3, keywords are:  工作, 一边, 互联网, 成为, 生活

Using tf-idf score with span:
In article 1, keywords are:  有赞, 想, 时间, 工作, 规定
In article 2, keywords are:  利益, 精神, 明星, 高大, 未来
In article 3, keywords are:  工作, 互联网, 选择, 公司, 经济

Using text rank:
In article 1, keywords are:  劳动法第三十六条
In article 2, keywords are:  劳动者, 心甘情愿, 忘我工作, 现身说法, 负面效应
In article 3, keywords are:  工作制, 涂脂抹粉
```


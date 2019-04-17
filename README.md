# Keyword Extraction Implementation for Chinese Corpuses

## Description

This is a simple implementation of keyword extraction / text summarization algorithms for Chinese corpuses.
Implemented algorithms are:

- (Keyword Extraction) TF-IDF

- (Keyword Extraction) TF-IDF with word span information 

- (Text Summarization) Textrank 

## Dependencies

In the following are recommended (but not necessarily required) dependencies and versions:

1. Python interpreter `python` >= 3.6
2. Python package `gensim` >= 3.4.0
3. Python pacakge `jieba` >=0.39

## Instructions

### Data

There are 3 demo documents under the directory `dataset/corpus`, which have been used for debugging.

If more data (documents) are needed, place each document under `dataset/corpus`. Make sure each documents is encoded in `UTF-8` format (rather than `GBK`/`GB18030`) and has a `.txt` extension.

### Run

To run a test, first `cd` to the project directory and run

```bash
python corpus.py
```

### Platform

The program should run fine on MacOS, Linux and other *nix platforms.

In case the program is run a Windows machine, or any other system that uses a path separator other than the forward slash `/`, please change the path constants accordingly.

### Demo Output

```
Building prefix dict from the default dictionary ...
Loading model from cache /var/folders/jr/qgh_hd1945bb_g0k8fwy_gn00000gp/T/jieba.cache
Loading model cost 0.999 seconds.
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
In article 1, keywords are:  
In article 2, keywords are:  不得不 说 ， 这碗 由 明星 企业家 精心 烹制 的 鸡汤 虽然 看上去 很 高大 上 ， 但 明显 有毒 ， 劳动者 很难 笑纳 。 还 需要 警惕 的 是 ， 这种 毒 鸡汤 论调 无异于 对 奋斗 精神 的 解构 ， 对 建设 法治 社会 的 消解 ， 它 一再 被 端出来 ， 将 对 弘扬 奋斗 精神 的 时代 主旋律 构成 干扰 ， 有 思想 上 造成 混乱 的 危险 。 
In article 3, keywords are:  

```


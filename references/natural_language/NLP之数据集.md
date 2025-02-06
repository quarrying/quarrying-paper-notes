# Benchmark & Datasets

## CLUE, Chinese Language Understanding Evaluation Benchmark
---
- https://www.cluebenchmarks.com/index.html

## OpenCompass
----
> OpenCompass is an open-source, efficient, and comprehensive evaluation suite and platform designed for large models.

- https://opencompass.org.cn/

## GLUE, General Language Understanding Evaluation; SuperGLUE
----
a collection of 9 datasets for evaluating natural language understanding systems.

- https://gluebenchmark.com/
- https://super.gluebenchmark.com/
- [2018 ICLR] Glue: A multi-task benchmark and analysis platform for natural language understanding

## C-Eval
----
> C-Eval评测基准由上海交通大学、清华大学以及爱丁堡大学联合创建，是面向中文语言模型的综合考试评测集，覆盖了52个来自不同行业领域的学科。

- https://cevalbenchmark.com/

## MMLU, Massive Multitask Language Understanding
----
> MMLU由加州大学伯克利分校等知名高校共同打造，集合了科学、工程、数学、人文、社会科学等领域的57个科目，主要目标是对模型的英文跨学科专业能力进行深入测试。其内容广泛，从初级水平一直涵盖到高级专业水平。

- https://github.com/hendrycks/test
- https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu

## SQuAD, Stanford Question Answering Dataset
---
- https://rajpurkar.github.io/SQuAD-explorer/

## CoQA, A Conversational Question Answering Challenge
-----
- https://stanfordnlp.github.io/coqa/

## AGIEval
----
> AGIEval评测基准由微软研究院发起，旨在全面评估基础模型在人类认知和问题解决相关任务上的能力，包含了中国的高考、司法考试，以及美国的SAT、LSAT、GRE和GMAT等20个公开且严谨的官方入学和职业资格考试。

- https://github.com/microsoft/AGIEval

## Gaokao
----
> Gaokao评测基准是复旦大学研究团队创建的评测框架，以中国高考题目作为数据集，用于测试大模型在中文语言理解和逻辑推理能力方面的表现。

- https://github.com/OpenLMLab/GAOKAO-Bench


## decaNLP
-----

## WMT 2014 English-to-German
---

## WMT 2014 English-to-French
----

## WuDaoCorpora, WuDao
----
中文语料库.

- [2021] WuDaoCorpora: A super large-scale Chinese corpora for pre-training language models
- https://github.com/THUDM/Chinese-Transformer-XL
- https://data.baai.ac.cn/details/WuDaoCorporaText

## C4, colossal clean crawled corpus
---
C4 语料库被用来训练 T5 模型, 806GB.

## CLUECorpus2020 
----

## THUCTC2
---
> THUCTC2 is a Chinese text classification toolkit accompanying by a 2.19 GB dataset containing 740,000 news documents. 

- https://github.com/thunlp/THUCTC
- http://thuctc.thunlp.org/

## Pile, The Pile
---
- [2020] The Pile: An 800GB Dataset of Diverse Text for Language Modeling


## RedPajama-Data
----
- https://github.com/togethercomputer/RedPajama-Data


## [awesome-nlp-chinese-corpus](https://github.com/wangmuy/awesome-nlp-chinese-corpus )
---

## [Chinese-Names-Corpus](https://github.com/wainshine/Chinese-Names-Corpus )
---

## [2013 EMNLP] SST, Stanford Sentiment Treebank
---
> The Stanford Sentiment Treebank is a corpus with fully labeled parse trees that allows for a complete analysis of the compositional effects of sentiment in language. The corpus is based on the dataset introduced by Pang and Lee (2005) and consists of 11,855 single sentences extracted from movie reviews. It was parsed with the Stanford parser and includes a total of 215,154 unique phrases from those parse trees, each annotated by 3 human judges.
> Each phrase is labelled as either negative, somewhat negative, neutral, somewhat positive or positive. The corpus with all 5 labels is referred to as SST-5 or SST fine-grained. Binary classification experiments on full sentences (negative or somewhat negative vs somewhat positive or positive with neutral sentences discarded) refer to the dataset as SST-2 or SST binary.

- [2013 EMNLP] Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank

## MultiNLI, Multi-Genre Natural Language Inference
----
433k sentence pairs annotated with textual entailment information

- https://cims.nyu.edu/~sbowman/multinli/
- https://paperswithcode.com/sota/natural-language-inference-on-multinli


## LCQMC, A Large-scale Chinese Question Matching Corpus
----
> Question matching is a fundamental task of QA, which is usually recognized as a semantic matching task, sometimes a paraphrase identification task. The goal of the task is to search questions that have similar intent as the input question from an existing database. We introduce a large-scale Chinese question matching corpus (named LCQMC). LCQMC is more general than paraphrase corpus as it focuses on intent matching rather than paraphrase. The corpus contains 260,068 question pairs with manual annotation and we split it into three parts, i.e., a training set containing 238,766 question pairs, a development set with 8,802 question pairs, and a test set with 12,500 question pairs. 

- http://icrc.hitsz.edu.cn/Article/show/171.html

## BQ Corpus, Bank Question Corpus
----
> As the semantic matching task, sentence semantic equivalence identification (SSEI) is a fundamental task of natural language processing (NLP) in question answering (QA), automatic customer service and chat-bots. In customer service systems, two questions are defined as semantically equivalent if they convey the same intent or they could be answered by the same answer. We introduce the Bank Question (BQ) corpus, a large-scale domain-specific Chinese corpus for SSEI. The BQ corpus contains 120,000 question pairs from online bank custom service logs. It is split into three parts: 100,000 pairs for training, 10,000 pairs for validation, and 10,000 pairs for test. We present five SSEI benchmark performance on our corpus, including state-of-the-art algorithms. As the largest manually annotated public Chinese SSEI corpus in the bank domain, the BQ corpus is not only useful for Chinese question semantic matching research, but also a significant resource for cross-lingual and cross-domain SSEI research.

- http://icrc.hitsz.edu.cn/info/1037/1162.htm


## STS-Benchmark, STS-B
----

## IMDb sentiment classification
---
- [2011 ACL] Learning word vectors for sentiment analysis

## BooksCorpus
----
> It contains over 7,000 unique unpublished books from a variety of genres including Adventure, Fantasy, and Romance.

- [2015 ICCV] Aligning books and movies: Towards story-like visual explanations by watching movies and reading books

## [2017 EMNLP] RACE, ReAding Comprehension from Examinations
---
> The ReAding Comprehension from Examinations (RACE) (Lai et al., 2017) task is a large-scale reading comprehension dataset with more than 28,000 passages and nearly 100,000 questions. The dataset is collected from English examinations in China, which are designed for middle and high school students. In RACE, each passage is associated with multiple questions. For every question, the task is to select one correct answer from four options. RACE has significantly longer context than other popular reading comprehension datasets and the proportion of questions that requires reasoning is very large.

- [2017 EMNLP] RACE_ Large-scale reading comprehension dataset from examinations

## CoNLL-2003 Named Entity Recognition
---
- Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition

## OpenWebText
---
仿照 WebText 构建的数据集, 有 38GB.

- https://skylion007.github.io/OpenWebTextCorpus/


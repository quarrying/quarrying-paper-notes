# Tasks
- sentiment analysis
- topic detection
- language detection
- key phrase extraction
- document categorization
- question answering
- machine translation: 机器翻译.
- reading comprehension
- text summarization: 文本摘要
- part-of-speech (POS) tagging: 词性标注
- named entity recognition (NER): 命名实体识别
- dependency parsing (DEP)
- text classification
- knowledge graph: 知识图谱
- relation extraction: 关系抽取


# Papers

## Survey
---
- [Awesome-Chinese-NLP](https://github.com/crownpku/Awesome-Chinese-NLP )

## [2015] Byte Pair Encoding, BPE
----
- [2015] Neural Machine Translation of Rare Words with Subword Units

## [2019] BERT, Bidirectional Encoder Representations from Transformers; BERT-wwm 
---
**MLM (Masked Language Modeling) 中 Masking 方法**:
- Single-token Masking: 原始 BERT 中的方法.
- Whole Word Masking (WWM)
- Entity Mention Replacement (EMR)

BERT 的思想通俗来说就是完形填空 (cloze).

### 模型结构
- BERT base, 参数量 110M
- BERT large, 参数量 340M

### 参考
- [2019]] Bert: Pre-training of deep bidirectional transformers for language understanding


## [2018] GPT, generative pre-training
----
与 generative pre-training 相对的是 contrastive pre-training.

- [2018] Improving language understanding by generative pre-training


## [2019] GPT-2
----
GPT-2 的训练集为 WebText.

Parameters | Layers | $d_{model}$
-----------|--------|--------------
117M       | 12     | 768
345M       | 24     | 1024
762M       | 36     | 1280
1542M      | 48     | 1600

- [2019] Language models are unsupervised multitask learners

## [2019] T5, Text-to-Text Transfer Transformer
----
- [2019] Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer

## [2020] Scaling laws for neural language models
----

## [2020] GPT-3
----
- [2020 NeurIPS] Language models are few-shot learners

## [2018] ELMo
----
基于 LSTM, 双向编码.

- [2018 NAACL] Deep contextualized word representations

## [2019] XLNet
----
- [2019 NeurIPS] Xlnet: Generalized autoregressive pretraining for language understanding

## [2019] RoBERTa
---
- [2019] Roberta: A robustly optimized bert pretraining approach

## [2020] ALBERT
---
- [2020 ICLR] Albert: Alite bert for self-supervised learning of language representations

## [2020] DeBERTa
---
- [2020] DeBERTa: Decoding-enhanced BERT with Disentangled Attention

## [2021] RoFormer
---
- [2021] RoFormer: Enhanced transformer with rotary position embedding

## [2022 ACL] GLM, ChatGLM
----
- https://github.com/THUDM/ChatGLM-6B
- https://github.com/THUDM/GLM
- https://chatglm.cn
- [2022 ACL] GLM: General Language Model Pretraining with Autoregressive Blank Infilling

## [2023] LLaMA
----
Meta 开源的大语言模型, 很多学术界的 LLM 都是基于它微调的.

LLaMA 完全基于开源数据训练, 在很多基准数据集上 LLaMA-13B 可以匹敌 GPT-3 (175B), LLaMA-65B 可以匹敌 Chinchilla-70B 和 PaLM-540B.

> LLaMA is an auto-regressive language model, based on the transformer architecture. The model comes in different sizes: 7B, 13B, 33B and 65B parameters.

- https://ai.facebook.com/blog/large-language-model-llama-meta-ai/
- [2023] LLaMA: Open and Efficient Foundation Language Models

## [2022] BLOOM, BigScience Language Open-science Open-access Multilingual
----
- [2022] BLOOM: A 176B-Parameter Open-Access Multilingual Language Model

## [2023] Stanford Alpaca
----
- https://github.com/tatsu-lab/stanford_alpaca
- [2023] Stanford Alpaca: An Instruction-following LLaMA model

## [2022] Self-Instruct
----
- [2022] Self-Instruct: Aligning Language Model with Self Generated Instructions

## Other LLMs
- MPT, MosaicML Pretrained Transformer
- StableLM
- Pythia
- RedPajama
- Megatron-Turing NLG 530B, MT-530B
- Megatron-11B
- GPT-Neo
- GPT-J-6B
- Pangu-α-13B
- FairSeq
- [GPT-NeoX-20B](https://github.com/EleutherAI/gpt-neox)
- baichuan-7B

# Benchmark

## CLUE, 中文语言理解测评基准
---
- https://www.cluebenchmarks.com/index.html

## C-Eval
----
> C-Eval评测基准由上海交通大学、清华大学以及爱丁堡大学联合创建，是面向中文语言模型的综合考试评测集，覆盖了52个来自不同行业领域的学科。

## AGIEval
----
> AGIEval评测基准由微软研究院发起，旨在全面评估基础模型在人类认知和问题解决相关任务上的能力，包含了中国的高考、司法考试，以及美国的SAT、LSAT、GRE和GMAT等20个公开且严谨的官方入学和职业资格考试。

## Gaokao
----
> Gaokao评测基准是复旦大学研究团队创建的评测框架，以中国高考题目作为数据集，用于测试大模型在中文语言理解和逻辑推理能力方面的表现。

## MMLU
----
> MMLU由加州大学伯克利分校等知名高校共同打造，集合了科学、工程、数学、人文、社会科学等领域的57个科目，主要目标是对模型的英文跨学科专业能力进行深入测试。其内容广泛，从初级水平一直涵盖到高级专业水平。


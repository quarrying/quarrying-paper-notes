# Tasks
- sentiment analysis
- topic detection
- language detection
- key phrase extraction
- document categorization
- question answering
- machine translation
- reading comprehension
- summarization
- part-of-speech (POS)
- named entity recognition (NER)
- dependency parsing (DEP)
- text classification


# Papers

## [2019] BERT, Bidirectional Encoder Representations from Transformers; BERT-wwm 
---
- WWM, Whole Word Masking
- MLM, Masked Language Modeling

BERT 的思想通俗来说就是完形填空 (cloze).

### 模型结构
- BERT base
- BERT large

### 参考
- [2019]] Bert: Pre-training of deep bidirectional transformers for language understanding

## [2018] GPT, generative pre-training
----
- [2018] Improving language understanding by generative pre-training


## [2019] GTP-2
----
GTP-2 的训练集为 WebText.

Parameters | Layers | $d_{model}$
-----------|--------|--------------
117M       | 12     | 768
345M       | 24     | 1024
762M       | 36     | 1280
1542M      | 48     | 1600

- [2019] Language models are unsupervised multitask learners

## [2020] Scaling laws for neural language models
----

## [2020] GPT-3
----
- [2020 NeurIPS] Language models are few-shot learners

## [2018] ELMo
----
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

## GLM, ChatGLM
----
- https://github.com/THUDM/ChatGLM-6B
- https://github.com/THUDM/GLM
- https://chatglm.cn

## [2023] LLaMA
----
Meta 开源的大语言模型, 很多学术界的 LLM 都是基于它微调的.

LLaMA 完全基于开源数据训练, 在很多基准数据集上 LLaMA-13B 可以匹敌 GPT-3 (175B), LLaMA-65B 可以匹敌 Chinchilla-70B 和 PaLM-540B.

- https://ai.facebook.com/blog/large-language-model-llama-meta-ai/
- [2023] LLaMA: Open and Efficient Foundation Language Models

## [2022] BLOOM, BigScience Language Open-science Open-access Multilingual
----
- [2022] BLOOM: A 176B-Parameter Open-Access Multilingual Language Model

## [2023] Stanford Alpaca
----
- https://github.com/tatsu-lab/stanford_alpaca
- [2023] Stanford Alpaca: An Instruction-following LLaMA model



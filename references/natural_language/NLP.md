# Tasks
- sentiment analysis
- topic detection
- language detection
- key phrase extraction
- document categorization
- question answering
- machine translation: 机器翻译.
- reading comprehension
- part-of-speech (POS) tagging: 词性标注
- named entity recognition (NER): 命名实体识别
- dependency parsing (DEP)
- text classification: 文本分类
- text matching: 文本匹配
- text summarization: 文本摘要
- knowledge graph: 知识图谱
- relation extraction: 关系抽取
- Recognizing Textual Entailment (RTE): 文本蕴涵


# Papers

## Survey
---
- [Awesome-Chinese-NLP](https://github.com/crownpku/Awesome-Chinese-NLP )

## [2015] Byte Pair Encoding, BPE
----
- [2015] Neural Machine Translation of Rare Words with Subword Units

## [2018] BERT, Bidirectional Encoder Representations from Transformers; BERT-wwm 
---
**MLM (Masked Language Modeling) 中 Masking 方法**:
- Single-token Masking: 原始 BERT 中的方法.
- Whole Word Masking (WWM)
- Entity Mention Replacement (EMR)

BERT 的思想通俗来说就是完形填空 (cloze).

BERT 支持的最大序列长度为 512, 词汇表大小默认为 30522.

### 模型结构

name       | #layers  | hidden size | #heads | #params
-----------|----------|-------------|--------|-----------
BERT base  | 12       | 768         | 12     | 110M
BERT large | 24       | 1024        | 16     | 340M


### 参考
- [2019]] Bert_ Pre-training of deep bidirectional transformers for language understanding


## [2018] GPT, generative pre-training
----
与 generative pre-training 相对的是 contrastive pre-training.

GPT 的词汇表大小为 40,478?


- [2018] Improving language understanding by generative pre-training


## [2019] GPT-2
----
GPT-2 的训练集为 WebText.

GPT-2 的词汇表大小为 50,257?


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
175B

- [2020 NeurIPS] Language models are few-shot learners

## GPT-3.5, GPT-4
----
GPT3.5 的 max tokens 是 4K (相当于 5 页纸?), GPT4 的 max tokens 是 32K (相当于 40 页纸?).

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

## [2022] Self-Instruct
----
- [2022] Self-Instruct: Aligning Language Model with Self Generated Instructions

## [2022 ACL] GLM, ChatGLM
----
- [2022 ACL] GLM: General Language Model Pretraining with Autoregressive Blank Infilling
- https://huggingface.co/THUDM/chatglm-6b
- https://github.com/THUDM/ChatGLM-6B
- https://github.com/THUDM/GLM
- https://chatglm.cn

## [2023] LLaMA, LLaMA 2
----
Meta 开源的大语言模型, 很多学术界的 LLM 都是基于它微调的.

LLaMA 完全基于开源数据训练, 在很多基准数据集上 LLaMA-13B 可以匹敌 GPT-3 (175B), LLaMA-65B 可以匹敌 Chinchilla-70B 和 PaLM-540B.

> LLaMA is an auto-regressive language model, based on the transformer architecture. The model comes in different sizes: 7B, 13B, 33B and 65B parameters.

LLaMA 2 有 7B, 13B, 34B, 70B 四种参数大小的模型.


- https://ai.facebook.com/blog/large-language-model-llama-meta-ai/
- [2023] LLaMA: Open and Efficient Foundation Language Models

#
## [2022] BLOOM, BigScience Language Open-science Open-access Multilingual
----
- [2022] BLOOM: A 176B-Parameter Open-Access Multilingual Language Model

## [2023] Stanford Alpaca
----
- https://github.com/tatsu-lab/stanford_alpaca
- [2023] Stanford Alpaca: An Instruction-following LLaMA model

## Vicuna
---
Vicuna-13B 是基于 LLaMA 微调的.
> Vicuna-13B, an open-source chatbot trained by fine-tuning LLaMA on user-shared conversations collected from ShareGPT. 

- https://lmsys.org/blog/2023-03-30-vicuna/


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
- Google Bard
- [GPT-NeoX-20B](https://github.com/EleutherAI/gpt-neox)
- 百川, baichuan-7B
- 通义千问, Qwen-7B

## word2vec
----

## GloVe
----

## FastText
----

## EMLo
----

## OPT
----
- [2022] OPT_ open pre-trained transformer language models
- https://huggingface.co/facebook/opt-66b

## FlanT5
----
- [2022] Scaling instruction-finetuned language models
- https://huggingface.co/google/flan-t5-xxl


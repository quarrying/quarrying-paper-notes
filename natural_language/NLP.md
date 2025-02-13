# Tasks
- sentiment analysis
- topic detection
- language detection
- key phrase extraction
- document categorization
- question answering
- machine translation: 机器翻译
- reading comprehension
- part-of-speech (POS) tagging: 词性标注
- named entity recognition (NER): 命名实体识别
- dependency parsing (DEP)
- text classification: 文本分类
- text matching: 文本匹配
- text summarization: 文本摘要
- knowledge graph: 知识图谱
- knowledge probing: 知识探索
- relation extraction: 关系抽取
- Fine-grained Entity Typing (FET): 细粒度实体分类
- Recognizing Textual Entailment (RTE): 文本蕴涵
- natural language understanding (NLU): 自然语言理解
- Retrieval Augmented Generation (RAG): 检索增强生成
- Supervised Fine-Tuning (SFT): 监督微调
- Chain-of-Thought (CoT): 思维链
- semantic textual similarity (STS)
- task-oriented dialogue (TOD) 
- Language Agents (LA)

# Papers

## Survey
---
- [Awesome-Chinese-NLP](https://github.com/crownpku/Awesome-Chinese-NLP )

## [2014] GloVe
----
- [2014] GloVe: Global Vectors for Word Representation
- https://nlp.stanford.edu/projects/glove/

## [2018] ELMo
----
基于 LSTM, 双向编码.

- [2018 NAACL] Deep contextualized word representations

## [2018] BERT, Bidirectional Encoder Representations from Transformers; BERT-wwm 
---
**MLM (Masked Language Modeling) 中 Masking 方法**:
- Single-token Masking: 原始 BERT 中的方法.
- Whole Word Masking (WWM)
- Entity Mention Replacement (EMR)

BERT 的思想通俗来说就是完形填空 (cloze).

BERT 支持的最大序列长度为 512, 词汇表大小默认为 30522.

BERT 的损失函数: MLM (Masked LM) loss + NSP ( Next Sentence Prediction) loss.

> In contrast to denoising auto-encoders (Vincent et al., 2008), we only predict the masked words rather than reconstructing the entire input.

> The training data generator chooses 15% of the token positions at random for prediction. If the i-th token is chosen, we replace the i-th token with (1) the [MASK] token 80% of the time (2) a random token 10% of the time (3) the unchanged i-th token 10% of the time. Then, Ti will be used to predict the original token with cross entropy loss.

### 模型结构

name       | #layers  | hidden size | #heads | #params
-----------|----------|-------------|--------|-----------
BERT base  | 12       | 768         | 12     | 110M
BERT large | 24       | 1024        | 16     | 340M


### 参考
- [2019] Bert_ Pre-training of deep bidirectional transformers for language understanding
- https://github.com/google-research/bert


## [2018] GPT, generative pre-training
----
与 generative pre-training 相对的是 contrastive pre-training. GPT 的词汇表大小为 40,478?

pretext task 为 next-token prediction task.

> During transfer, we utilize task-specific input adaptations derived from traversal-style approaches [52], which process structured text input as a single contiguous sequence of tokens.

- [2018] Improving language understanding by generative pre-training


## [2019] GPT-2
----
GPT-2 的训练集为 WebText, 该数据集未开源. 

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
参数量为 175B. 

提出 in-context learning 的概念.

- [2020 NeurIPS] Language models are few-shot learners

## [2019] XLNet
----
- [2019 NeurIPS] Xlnet: Generalized autoregressive pretraining for language understanding

## [2019] RoBERTa
---
相对于 BERT, 移除了 next sentence prediction objective.

- [2019] RoBERTa_ A robustly optimized bert pretraining approach

## [2019 EMNLP] Sentence-BERT, SBERT
---
- [2019 EMNLP] Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks
- https://www.sbert.net/

## [2020] DistillBERT
---
- student 模型将 BERT 的层数减半
- 使用 teacher 模型对 student 模型进行初始化 (二取其一).
- 损失函数: distillation loss, masked language modeling loss, cosine embedding loss

DistilBERT vs BERT: 40% smaller, 60% faster, that retains 97% of the language understanding capabilities.

- [2020] DistilBERT, a distilled version of BERT_ smaller, faster, cheaper and lighter

## [2020] ALBERT
---
- [2020 ICLR] Albert: Alite bert for self-supervised learning of language representations

## [2020] DeBERTa
---
- [2020] DeBERTa: Decoding-enhanced BERT with Disentangled Attention

## [2020] MiniLM
---
- [2020] Minilm: Deep self-attention distillation for task-agnostic compression of pre-trained transformers

## [2021] RoFormer
---
- [2021] RoFormer: Enhanced transformer with rotary position embedding

## [2022] Self-Instruct
----
- [2022] Self-Instruct: Aligning Language Model with Self Generated Instructions

## [2022] OPT
----
- [2022] OPT_ open pre-trained transformer language models
- https://huggingface.co/facebook/opt-66b

## [2022] FlanT5, FLAN-T5, Flan-PaLM
----
- [2022] Scaling instruction-finetuned language models
- https://huggingface.co/google/flan-t5-xxl

## [2022] PaLM, PaLM2
---
- [2022] Palm_ Scaling language modeling with pathways


# LLM Products

## GPT-3.5, GPT-4
----
GPT-3.5 的 max tokens 是 4K (相当于 5 页纸?), GPT-4 的 max tokens 是 32K (相当于 40 页纸?).

GPT-3.5 和 GPT-4 的 tokenization 方法为 byte pair encoding (BPE).

## GLM, ChatGLM, General Language Model
----
- [2022 ACL] GLM: General Language Model Pretraining with Autoregressive Blank Infilling
- https://huggingface.co/THUDM/chatglm-6b
- https://github.com/THUDM/ChatGLM-6B
- https://github.com/THUDM/GLM
- https://chatglm.cn

## LLaMA
----
Meta 开源的大语言模型, 很多学术界的 LLM 都是基于它微调的.

LLaMA 完全基于开源数据训练, 在很多基准数据集上 LLaMA-13B 可以匹敌 GPT-3 (175B), LLaMA-65B 可以匹敌 Chinchilla-70B 和 PaLM-540B.

> LLaMA is an auto-regressive language model, based on the transformer architecture. The model comes in different sizes: 7B, 13B, 33B and 65B parameters.

### LLaMA 2
LLaMA 2 有 7B, 13B, 34B, 70B 四种参数大小的模型.

### LLaMa 3

- https://ai.facebook.com/blog/large-language-model-llama-meta-ai/
- [2023] LLaMA: Open and Efficient Foundation Language Models

## BLOOM, BigScience Language Open-science Open-access Multilingual
----
- [2022] BLOOM: A 176B-Parameter Open-Access Multilingual Language Model

## Stanford Alpaca
----
Alpaca 是基于 LLaMA 微调的.

- https://github.com/tatsu-lab/stanford_alpaca
- [2023] Stanford Alpaca: An Instruction-following LLaMA model

## Vicuna
---
Vicuna-13B 是基于 LLaMA 微调的.
> Vicuna-13B, an open-source chatbot trained by fine-tuning LLaMA on user-shared conversations collected from ShareGPT. 

- https://lmsys.org/blog/2023-03-30-vicuna/

## Qwen, 通义千问
----
### Qwen1
- 通用模型 Qwen-7B
- 对话模型 Qwen-7B-Chat 
- 视觉语言模型 Qwen-VL, Qwen-VL-Chat

### Qwen2
- Qwen2-0.5B
- Qwen2-1.5B
- Qwen2-7B
- Qwen2-72B, Qwen2-72B-Instruct
- Qwen2-57B-A14B

> All models were pre-trained on a high-quality, large-scale dataset comprising over 7 trillion tokens, covering a wide range of domains and languages.

## Mistral
---
- mistralai/Mistral-7B-Instruct-v0.1
- mistralai/Mistral-7B-Instruct-v0.2

**References**
- [Mistral 7B](https://mistral.ai/news/announcing-mistral-7b/)
- [[2023] Mistral 7B](https://arxiv.org/abs/2310.06825)

## DeepSeek
---

## Other LLMs
---
- MPT, MosaicML Pretrained Transformer
- StableLM
- Pythia
- RedPajama
- Megatron-Turing NLG 530B, MT-530B
- Megatron-11B
- FairSeq
- Google Bard
- [GPT-NeoX-20B](https://github.com/EleutherAI/gpt-neox)
- 百川, baichuan-7B
- 书生, InternLM-7B
- Claude


# Instruction tuning, instruction finetuning

## [2022 ICLR] Finetuned Language Models Are Zero-Shot Learners
---
提出 Instruction tuning 的概念.

## [2022] InstructGPT
----
- [2022] Training language models to follow instructions with human feedback

## [2023] Exploring the Relationship between In-Context Learning and Instruction Tuning
----
> In-Context Learning (ICL) and Instruction Tuning (IT) are two primary paradigms of adopting Large Language Models (LLMs) to downstream applications. However, they are significantly different. In ICL, a set of demonstrations are provided at inference time but the LLM's parameters are not updated. In IT, a set of demonstrations are used to tune LLM's parameters in training time but no demonstrations are used at inference time. Although a growing body of literature has explored ICL and IT, studies on these topics have largely been conducted in isolation, leading to a disconnect between these two paradigms. In this work, we explore the relationship between ICL and IT by examining how the hidden states of LLMs change in these two paradigms. Through carefully designed experiments conducted with LLaMA-2 (7B and 13B), we find that ICL is implicit IT. In other words, ICL changes an LLM's hidden states as if the demonstrations were used to instructionally tune the model. Furthermore, the convergence between ICL and IT is largely contingent upon several factors related to the provided demonstrations. Overall, this work offers a unique perspective to explore the connection between ICL and IT and sheds light on understanding the behaviors of LLM.

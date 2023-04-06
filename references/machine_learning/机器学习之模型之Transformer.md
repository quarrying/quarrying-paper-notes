# Transformer
---

## [2017] Attention is All You Need
---
!TODO: 精读

Attention (Scaled Dot-Product Attention) 的定义: 
$$\mathrm{Attention}(Q,K,V) = \mathrm{softmax}\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V$$

符号说明: 
1) $Q\in\mathbb{R}^{n\times d_k}$ 为 query, $n$ 是 target sequence length.
2) $K\in\mathbb{R}^{m\times d_k}$ 为 key, $m$ 是 source sequence length.
3) $V\in\mathbb{R}^{m\times d_v}$ 为 value.

最终的 $\mathrm{Attention}(Q,K,V)$ 的尺寸为 $n\times d_v$, 即 attention 将 $n\times d_k$ 的 $Q$ 编码成了一个新的 $n\times d_v$ 的序列. 

当 $Q = K = V$ 时, 称为自注意力 (self attention). 此时不妨设它们的尺寸为 $n\times d$, 输出的尺寸也为 $n\times d$.

关于为什么要除以 $\sqrt{d_k}$, 下面摘抄一下原文:
> We suspect that for large values of $d_k$, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients. To counteract this effect, we scale the dot products by $1/\sqrt{d_k}$ .

**TIPS** (自己理解, 待明确): 
1) softmax 函数是多元函数 (自变量是向量), 上面式子中的 softmax 函数的自变量是矩阵, 与定义不符, 此处的 `softmax(x)` 应该理解为 `torch.nn.functional.softmax(x, dim=1)` (借用 pytorch 中的函数.)


### 带投影的 Scaled Dot-Product Attention

$$ \mathrm{Attention}(QW^Q, KW^K, VW^V)W^O$$

$Q\in\mathbb{R}^{n\times e_q}$ 为 query embedding, $n$ 为 target sequence length, $e_q$ 为 query embedding dimension.

$K\in\mathbb{R}^{m\times e_k}$ 为 key embedding, $m$ 为 source sequence length, $e_k$ 为 key embedding dimension.

$V\in\mathbb{R}^{m\times e_v}$ 为 value embedding, $m$ 为 source sequence length, $e_v$ 为 value embedding dimension.

$W^Q \in \mathbb{R}^{e_q\times d_k}$ 为 query projection matrix.

$W^K \in \mathbb{R}^{e_k\times d_k}$ 为 key projection matrix.

$W^V \in \mathbb{R}^{e_v\times d_v}$ 为 value projection matrix.

$W^O \in \mathbb{R}^{d_v\times d_o}$ 为 output projection matrix.

$QW^Q \in \mathbb{R}^{n\times d_k}$ 为 query.

$KW^K \in \mathbb{R}^{m\times d_k}$ 为 key.

$VW^V \in \mathbb{R}^{m\times d_v}$ 为 value.

### 多头注意力 (Multi-Head Attention; MHA)

$$\mathrm{MultiHead}(Q, K, V) = \mathrm{Concat}(\mathrm{head}_1, ..., \mathrm{head}_h)W_O$$

$$\mathrm{head}_i = \mathrm{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

其中 $h$ 表示头的个数.

在 PyTorch 的 `nn.MultiheadAttention` 中 $n = m$; $d_k = d_v = d_o$, 且其值等于 `embed_dim`.

`q` 的尺寸为 `(..., embed_dim)`

`k` 的尺寸为 `(..., e_k)`

`v` 的尺寸为 `(..., e_v)`

`q_proj_weight` 的尺寸为 `(embed_dim, embed_dim)`

`k_proj_weight` 的尺寸为 `(embed_dim, e_k)`

`v_proj_weight` 的尺寸为 `(embed_dim, e_v)`

`out_proj.weight` 的尺寸为 `(embed_dim, embed_dim)`

`attn_output` 的尺寸为 `(n, embed_dim)`

当 `embed_dim = e_k = e_v` 时, 会将 `q_proj_weight`, `k_proj_weight` 和 `v_proj_weight` 合并为 `in_proj_weight`, 其尺寸为 `(3*embed_dim, embed_dim)`

```python
>>> multihead_attn = nn.MultiheadAttention(embed_dim=256, num_heads=1, kdim=32, vdim=16)
>>> print_named_parameters(multihead_attn)
[1] q_proj_weight                                     : torch.Size([256, 256])
[2] k_proj_weight                                     : torch.Size([256, 32])
[3] v_proj_weight                                     : torch.Size([256, 16])
[4] in_proj_bias                                      : torch.Size([768])
[5] out_proj.weight                                   : torch.Size([256, 256])
[6] out_proj.bias                                     : torch.Size([256])
>>> multihead_attn = nn.MultiheadAttention(embed_dim=256, num_heads=4, kdim=32, vdim=16)
>>> print_named_parameters(multihead_attn)
[1] q_proj_weight                                     : torch.Size([256, 256])
[2] k_proj_weight                                     : torch.Size([256, 32])
[3] v_proj_weight                                     : torch.Size([256, 16])
[4] in_proj_bias                                      : torch.Size([768])
[5] out_proj.weight                                   : torch.Size([256, 256])
[6] out_proj.bias                                     : torch.Size([256])
>> multihead_attn = nn.MultiheadAttention(embed_dim=256, num_heads=4)
>>> print_named_parameters(multihead_attn)
[1] in_proj_weight                                    : torch.Size([768, 256])
[2] in_proj_bias                                      : torch.Size([768])
[3] out_proj.weight                                   : torch.Size([256, 256])
[4] out_proj.bias                                     : torch.Size([256])
```

### 多头注意力的计算量

简便起见, $Q, K, V\in \mathbb{R}^{n\times d}$, $W_i^Q, W_i^K, W_i^V \in \mathbb{R}^{d \times d}$

$QW_i^Q$, $KW_i^K$, $VW_i^V$ 的计算量均为 $nd^2$. 共 $h$ 个头, 所以总计算量为 $3hnd^2$.

不妨令 $Q'=QW_i^Q, K'=KW_i^K, V'=VW_i^V$, $\mathrm{head}_i = \mathrm{Attention}(Q', K', V')$ 的计算量为 $2n^2d$ ( $Q'K'^T$ 的计算量为 $n^2d$, 其经过 softmax 等操作, 乘上 $V'$ 的计算量也为 $n^2d$ ). 共 $h$ 个头, 所以总计算量为 $2hn^2d$.

不妨令 $S = \mathrm{Concat}(\mathrm{head}_1, ..., \mathrm{head}_h)$, 其尺寸为 $n\times hd$, $S W_O$ 的计算量为 $hnd^2$.

综上计算量为: $4hnd^2 + 2hn^2d$, 计算复杂度为 $O(nd^2 + hn^2d)$.

### References
- [《Attention is All You Need》浅读（简介+代码）](https://kexue.fm/archives/4765)
- [[2017] Attention is All You Need](https://arxiv.org/pdf/1706.03762.pdf)
- https://stackoverflow.com/questions/65703260/computational-complexity-of-self-attention-in-the-transformer-model


## [2020 ICML] iGPT
---
- [2020 ICML] Generative pretraining from pixels

## [2020] ViT, Vision Transformer
---
!TODO: 精读

iGPT 和 ViT 是 transformer 在 CV 中的两大先驱工作.

- [2020] An image is worth 16x16 words_ Transformers for image recognition at scale

## [2020] Visual Transformers: Token-based Image Representation and Processing for Computer Vision
---

## [2021] A Survey on Visual Transformer
---

## [2021] Swin Transformer
---
**TIPS**: Swin 系 shift window 的缩略词.

> We observe that significant chalenges in transferring its high performance in the language domain to the visual domain can be explained by differences between the two modalities. One of these differences involves scale. Unlike the word tokens that serve as the basic elements of processing in language Transformers, visual elements can vary substantially in scale, a problem that receives attention in tasks such as object detection [41, 52, 53]. In existing Transformer-based models [61, 19], tokens are all of a fixed scale, a property unsuitable for these vision applications. Another difference is the much higher resolution of pixels in images compared to words in passages of text. There exist many vision tasks such as semantic segmentation that require dense prediction at the pixel level, and this would be intractable for Transformer on high-resolution images, as the computational complexity of its self-attention is quadratic to image size.

name   | scale | counterpart
-------|-------|--------
Swin-B | 1x    | ViT-B, DeiT-B
Swin-T | 0.25x | ResNet-50, DeiT-S
Swin-S | 0.5x  | ResNet-101
Swin-L | 2x    | /

- [2021] Swin transformer: Hierarchical vision transformer using shifted windows


## [2021] Swin Transformer V2: Scaling Up Capacity and Resolution
---
使用 scaled cosine attention 替换常见的 scaled dot-product attention.


## [2020] DeiT
---
!TODO

- [2020] Training data-efficient image transformers & distillation through attention

## [2022] DaViT
---

### Typo
1) in `2 Related Work`: objection detection

**References**
- [2022] DaViT_ Dual Attention Vision Transformers

## [2021 ICCV] PVT, Pyramid vision transformer
----
- [2021 ICCV] Pyramid vision transformer: A versatile backbone for dense prediction without convolutions
- [2021] PVTv2_ Improved Baselines with Pyramid Vision Transformer

## [2021] CvT, convolutions to vision transformers
----
- [2021] Cvt: Introducing convolutions to vision transformers

## [2021 ICCV] ViL
----
- [2021 ICCV] Multi-scale vision longformer: A new vision transformer for high-resolution image encoding

## [2021 CVPR] HaloNet
----
- [2021 CVPR] Scaling local self-attention for parameter efficient visual backbones

## [2021] Twins
----
- [2021] Twins: Revisiting spatial attention design in vision transformers

## MobileViT
----
- MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer
- Separable Self-attention for Mobile Vision Transformers
- MobileViTv3: Mobile-Friendly Vision Transformer with Simple and Effective Fusion of Local, Global and Input Features

## CPVT
----
CPVT uses 3 × 3 Conv together with the PE to implement a data-driven PE (positional encoding).

- [2021] Conditional positional encodings for vision transformers


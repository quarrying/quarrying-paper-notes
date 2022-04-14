# Transformer
---

## Attention is All You Need
---
!TODO: 精读

Attention (Scaled Dot-Product Attention) 的定义: 
$$\mathrm{Attention}(Q,K,V) = \mathrm{softmax}\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V$$

其中 $Q\in\mathbb{R}^{n\times d_k}, K\in\mathbb{R}^{m\times d_k}, V\in\mathbb{R}^{m\times d_v}$. $Q,K,V$ 分别是 query, (memory) key, (memory) value 的简写. 最终的 $\mathrm{Attention}(Q,K,V)$ 的尺寸为 $n\times d_v$. 可见 attention 将 $n\times d_k$ 的 $Q$ 编码成了一个新的 $n\times d_v$ 的序列.

当 $Q = K = V$ 时, 称为自注意力 (self attention). 此时不妨设它们的尺寸为 $n\times d$.

**TIPS** (自己理解, 待明确): softmax 函数是多元函数 (自变量是向量), 上面式子中的 softmax 函数的自变量是矩阵, 与定义不符, 此处的 `softmax(x)` 应该理解为 `torch.nn.functional.softmax(x, dim=1)` (借用 pytorch 中的函数.)

关于为什么要除以 $\sqrt{d_k}$, 下面摘抄一下原文:
> We suspect that for large values of $d_k$, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients. To counteract this effect, we scale the dot products by $1/\sqrt{d_k}$ .

### Multi-Head Attention

$$\mathrm{MultiHead}(Q, K, V) = \mathrm{Concat}(\mathrm{head}_1, ..., \mathrm{head}_h)W_O$$

$$\mathrm{head}_i = \mathrm{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

其中 $h$ 表示头的个数, $W_i^Q \in \mathbb{R}^{d_{model}\times d_k}$, $W_i^K \in \mathbb{R}^{d_{model}\times d_k}$, $W_i^V \in \mathbb{R}^{d_{model}\times d_v}$, $W^O \in \mathbb{R}^{hd_{v}\times d_{model}}$.

### *Multi-Head Attention 的计算量*

简便起见, 假设 $d_{model} = d_k = d_v = d$, 且 $Q, K,V\in \mathbb{R}^{n\times d}$.

$QW_i^Q$, $KW_i^K$, $VW_i^V$ 的计算量均为 $nd^2$. 共 $h$ 个头, 所以总计算量为 $3hnd^2$.

不妨令 $Q'=QW_i^Q, K'=KW_i^K, V'=VW_i^V$, $\mathrm{head}_i = \mathrm{Attention}(Q', K', V')$ 的计算量为 $2n^2d$ ( $Q'K'^T$ 的计算量为 $n^2d$, 其经过 softmax 等操作, 乘上 $V'$ 的计算量也为 $2n^2d$ ). 共 $h$ 个头, 所以总计算量为 $2hn^2d$.

不妨令 $S = \mathrm{Concat}(\mathrm{head}_1, ..., \mathrm{head}_h)$, 其尺寸为 $n\times hd$, $S W_O$ 的计算量为 $hnd^2$.

综上计算量为: $4hnd^2 + 2hn^2d$, 计算复杂度为 $O(nd^2 + hn^2d)$.

### **References**
- [《Attention is All You Need》浅读（简介+代码）](https://kexue.fm/archives/4765)
- [[2017] Attention is All You Need]()
- https://stackoverflow.com/questions/65703260/computational-complexity-of-self-attention-in-the-transformer-model


## iGPT
---
- [2020 ICML] Generative pretraining from pixels

## ViT, Vision Transformer
---
iGPT 和 ViT 是 transformer 在 CV 中的两大先驱工作.

!TODO

- [2020] An image is worth 16x16 words_ Transformers for image recognition at scale

## [2020] Visual Transformers: Token-based Image Representation and Processing for Computer Vision
---

## [2021] A Survey on Visual Transformer
---

## [2021] Swin Transformer
---
> We observe that significant chalenges in transferring its high performance in the language domain to the visual domain can be explained by differences between the two modalities. One of these differences involves scale. Unlike the word tokens that serve as the basic elements of processing in language Transformers, visual elements can vary substantially in scale, a problem that receives attention in tasks such as object detection [41, 52, 53]. In existing Transformer-based models [61, 19], tokens are all of a fixed scale, a property unsuitable for these vision applications. Another difference is the much higher resolution of pixels in images compared to words in passages of text. There exist many vision tasks such as semantic segmentation that require dense prediction at the pixel level, and this would be intractable for Transformer on high-resolution images, as the computational complexity of its self-attention is quadratic to image size.

name   | scale | counterpart
-------|-------|--------
Swin-B | 1x    | ViT-B, DeiT-B
Swin-T | 0.25x | ResNet-50, DeiT-S
Swin-S | 0.5x  | ResNet-101
Swin-L | 2x    | /

- [2021] Swin transformer: Hierarchical vision transformer using shifted windows

## [2020] DeiT
---
- [2020] Training data-efficient image transformers & distillation through attention

## [2022] DaViT
---

### Typo
1) in `2 Related Work`: objection detection

**References**
- [2022] DaViT_ Dual Attention Vision Transformers

## Others
---
- PVT, Pyramid vision transformer
    - [2021 ICCV] Pyramid vision transformer: A versatile backbone for dense prediction without convolutions
- CvT, convolutions to vision transformers
    - [2021] Cvt: Introducing convolutions to vision transformers
- ViL
    - [2021 ICCV] Multi-scale vision longformer: A new vision transformer for high-resolution image encoding
- HaloNet
    - [2021 CVPR] Scaling local self-attention for parameter efficient visual backbones


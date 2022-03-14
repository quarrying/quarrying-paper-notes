## Attention is All You Need
---
!TODO: 精读

Attention 的定义: 
$$\mathrm{Attention}(\boldsymbol{Q},\boldsymbol{K},\boldsymbol{V}) = \mathrm{softmax}\left(\frac{\boldsymbol{Q}\boldsymbol{K}^{\top}}{\sqrt{d_k}}\right)\boldsymbol{V}$$

其中 $\boldsymbol{Q}\in\mathbb{R}^{n\times d_k}, \boldsymbol{K}\in\mathbb{R}^{m\times d_k}, \boldsymbol{V}\in\mathbb{R}^{m\times d_v}$. 可见 attention 将 $n\times d_k$ 的 $\boldsymbol{Q}$ 编码成了一个新的 $n\times d_v$ 的序列. $\boldsymbol{Q},\boldsymbol{K},\boldsymbol{V}$ 分别是 query, (memory) key, (memory) value 的简写.

> We suspect that for large values of $d_k$, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients. To counteract this effect, we scale the dot products by $1/\sqrt{d_k}$ .

当 $\boldsymbol{Q} = \boldsymbol{K} = \boldsymbol{V}$ 时, 称为自注意力 (self attention).

**References**
- [《Attention is All You Need》浅读（简介+代码）](https://kexue.fm/archives/4765)
- [2017] Attention is All You Need


## ViT, Vision Transformer
---
- [2020] An image is worth 16x16 words_ Transformers for image recognition at scale

## DETR
---
- [2020] End-to-end object detection with transformers

## [2020] Visual Transformers_ Token-based Image Representation and Processing for Computer Vision
---

## [2020] Toward Transformer-Based Object Detection
---

## [2021] A Survey on Visual Transformer
---

## Swin Transformer
---
> We observe that significant chalenges in transferring its high performance in the language domain to the visual domain can be explained by differences between the two modalities. One of these differences involves scale. Unlike the word tokens that serve as the basic elements of processing in language Transformers, visual elements can vary substantially in scale, a problem that receives attention in tasks such as object detection [41, 52, 53]. In existing Transformer-based models [61, 19], tokens are all of a fixed scale, a property unsuitable for these vision applications. Another difference is the much higher resolution of pixels in images compared to words in passages of text. There exist many vision tasks such as semantic segmentation that require dense prediction at the pixel level, and this would be intractable for Transformer on high-resolution images, as the computational complexity of its self-attention is quadratic to image size.

name   | scale | counterpart
-------|-------|--------
Swin-B | 1x    | ViT-B, DeiT-B
Swin-T | 0.25x | ResNet-50, DeiT-S
Swin-S | 0.5x  | ResNet-101
Swin-L | 2x    | /


- [2021] Swin transformer: Hierarchical vision transformer using shifted windows

## DeiT
---
- [2020] Training data-efficient image transformers & distillation through attention

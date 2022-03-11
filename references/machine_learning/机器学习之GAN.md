## GAN
----
开山之作, 第一作者是 Ian Goodfellow.

- [2014] Generative Adversarial Nets

## cGAN, Conditional GAN
---
- [2014] Conditional Generative Adversarial Nets

## DCGAN, Deep Convolutional GAN
---
!TODO

- [2016 ICLR] Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks
- https://github.com/carpedm20/DCGAN-tensorflow
- https://github.com/Newmu/dcgan_code

## DiscoGAN
---
- [2017 ICML] Learning to Discover Cross-Domain Relations with Generative Adversarial Networks

## WGAN, Wasserstein GAN
---
- [2017 ICML] Wasserstein generative adversarial networks

## WGAN-GP, WGAN-Gradient penalty
---
- [2017 NIPS] Improved Training of Wasserstein GANs

## LSGAN, Least Squares GAN
---
- [2017] Least Squares Generative Adversarial Networks

## SNGAN
--- 
- [2018 ICLR] Spectral normalization for generative adversarial networks

## BEGAN, Boundary Equilibrium GAN
---
- [2017] BEGAN_ Boundary Equilibrium Generative Adversarial Networks

## PG-GAN, PGGAN
---
- [2018 ICLR] Progressive Growing of GANs for Improved Quality, Stability, and Variation
- https://github.com/nashory/pggan-pytorch

## Spectral Normalization
---
- [2018 ICLR] Spectral Normalization for Generative Adversarial Networks

## Fictitious GAN
---
- [2018] Fictitious GAN_ Training GANs with Historical Models

## TequilaGAN
---
- [2018] TequilaGAN_ How to easily identify GAN samples

## SAGAN
---
- [2018] Self-Attention Generative Adversarial Networks

## BigGAN
---
- [2018 ICLR] Large scale gan training for high fidelity natural image synthesis

## PCGAN
---
- [2019 AAAI] Pcgan_ Partition-controlled human image generation

## StyleGAN
---
!TODO: truncation trick

一些标记:
- input latent space: $\mathcal{Z}$
- native latent space: $\mathcal{W}$
- extended latent space: $\mathcal{W}+$

**References**
- [2019 CVPR] A style-based generator architecture for generative adversarial networks

## StyleGAN2
----
- [2020 CVPR] Analyzing and improving the image quality of stylegan

## StyleGAN2-ada
----
StyleGAN2-ada proposes an adaptive discriminator augmentation mechanism which reduces the required number of images to several thousands.

> METFACES is our new dataset of 1336 high-quality faces extracted from the collection of Metropolitan Museum of Art (https://metmuseum.github.io/).

- [2020 NeurIPS] Training generative adversarial networks with limited data
- https://github.com/NVlabs/stylegan2-ada
- https://github.com/NVlabs/stylegan2-ada-pytorch

## InterFaceGAN 
---
> We therefore make an assumption that for any binary semantic (e.g., male v.s. female), there exists a hyperplane in the latent space serving as the separation boundary. Semantic remains the same when the latent code walks within one side of the hyperplane yet turns into the opposite when across the boundary.

- [2019] Interpreting the Latent Space of GANs for Semantic Face Editing

## Others
---
- [2016 NIPS] Improved Techniques for Training GANs
- [2017 ICLR] Adversarial Feature Learning
- [2018] The GAN Landscape_ Losses, Architectures, Regularization, and Normalization
- [2020] LSUN-Stanford Car Dataset_ Enhancing Large-Scale Car Image Datasets Using Deep Learning for Usage in GAN Training


# GAN Inversion, Image-to-code inversion
----
GAN Inversion 由 [2016 ECCV] Generative visual manipulation on the natural image manifold 提出. In this task, the latent vector from which a pretrained GAN most accurately reconstructs a given, known image, is sought.

## [2021] GAN inversion: A survey
---

## IcGAN
---
- [2016] Invertible conditional gans for image editing

## AEGAN
---
- [2017] Learning inverse mapping by autoencoder based generative adversarial nets

## IDInvert, In-domain invert encoding and inversion
---
- [2020 ECCV] In-domain gan inversion for real image editing

## Image2StyleGAN
----
- [2019 ICCV] Image2stylegan_ How to embed images into the stylegan latent space?

## StyleGAN2 projection
---
- [2019] Analyzing and improving the image quality of StyleGAN

## ALAE
---
- [2020 CVPR] Adversarial latent autoencoders

## PTI, Pivotal Tuning Inversion
---
本文提出的 Inversion 方法是一种基于优化的方法.

- [2021] Pivotal Tuning for Latent-based Editing of Real Images


# 一些链接
- https://github.com/hindupuravinash/the-gan-zoo
- https://github.com/zhangqianhui/AdversarialNetsPapers
- https://github.com/nightrome/really-awesome-gan
- https://github.com/nashory/gans-awesome-applications


## thisxdoesnotexist
- https://thisxdoesnotexist.com/
- https://thisvesseldoesnotexist.com/
- https://thispersondoesnotexist.com/
- https://thiscatdoesnotexist.com/


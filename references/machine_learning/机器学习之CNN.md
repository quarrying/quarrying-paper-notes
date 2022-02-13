# Network
---
### LeNet-5
---
- [1998 IEEE] Gradient-based learning applied to document recognition

### AlexNet
---
- [2012 NIPS] ImageNet Classiﬁcation with Deep Convolutional Neural Networks

### ZFNet
---
- [2014 ECCV] Visualizing and understanding convolutional networks

### VGG
---
- [2014] Very Deep Convolutional Networks for Large-Scale Image Recognition

### Inception
---
- [2015 CVPR] Going deeper with convolutions
- [2015 ICML] Batch normalization: Accelerating deep network training by reducing internal covariate shift
- [2015] Rethinking the inception architecture for computer vision
- [2016] Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning
- [2017 CVPR] Xception_ Deep Learning with Depthwise Separable Convolutions

### ResNet
---
- [2016 CVPR] Deep residual learning for image recognition
- [2016 ECCV] Identity mappings in deep residual networks
- [2016] Aggregated Residual Transformations for Deep Neural Networks
- [2016 BMVC] Wide Residual Networks

### DenseNet
---
为 ImageNet 设计的 DenseNet (参考文献中的 Table 1), 前两层为: `7 × 7 conv, stride 2` 和 `3 × 3 max pool, stride 2`. 在 [2018 CVPR] Scale-Transferrable Object Detectio 中提到这种设计并不好, 并用三个连续的卷积替换之:

> Inspired by DSOD [27], we replace the input layers (7 × 7 convolution layer, stride = 2 followed by a 3 × 3 max pooling layer, stride = 2) into three 3×3 convolution layers and one 2×2 mean pooling layer. The stride of the first convolution layer is 2 and the others are 1. The output channels for all three convolution layers are 64. We call these layers “stem block”. Table 1 depicts our network architecture in detail. Experiments show that this simple substitution can significantly improve the accuracy of object detection (see Table 3 in ablation study). One explanation could be that the input layers in the original DenseNet-169 have lost much information due to two consecutive down sampling. This will impair the performance of object detection, especially for small objects.

- [2016] Densely Connected Convolutional Networks

### DPN
---
- [2017] Dual Path Networks

### GUNN
---
- [2017] Gradually Updated Neural Networks for Large-Scale Image Recognition

### SENet
---
- [2017] Squeeze-and-Excitation Networks

### DLA
---
- [2017] Deep Layer Aggregation

### BAM/CBAM
---
- [2018 BMVC] BAM_ Bottleneck Attention Module
- [2018 ECCV] CBAM_ Convolutional Block Attention Module

### IBN-Net
---
- [2018 ECCV] Two at Once_ Enhancing Learning and Generalization Capacities via IBN-Net

### SKNet
---
- [2019] Selective Kernel Networks

### Res2Net
---
- [2019] Res2Net_ A New Multi-scale Backbone Architecture

### GCNet
---
- [2019] GCNet_ Non-local Networks Meet Squeeze-Excitation Networks and Beyond

### ResNeSt
---
- [2020] ResNeSt_ Split-Attention Networks

    
# 轻量型 CNN
---
### SqueezeNet
---
- [2016] SqueezeNet_ AlexNet-level accuracy with 50x fewer parameters and less than 0.5MB model size

### IGCV
---
- [2017 ICCV] Interleaved Group Convolutions for Deep Neural Networks
- [2018] IGCV2_ Interleaved Structured Sparse Convolutional Neural Networks
- [2018] IGCV3_ Interleaved low-rank group convolutions for efficient deep neural networks

### CondenseNet
---
- [2017] CondenseNet_ An Efficient DenseNet using Learned Group Convolutions

### SqueezeNext
---
- [2018] SqueezeNext_ Hardware-Aware Neural Network Design

### MobileNet
---
- [2017] MobileNets_ Efficient Convolutional Neural Networks for Mobile Vision Applications
- [2018] Inverted Residuals and Linear Bottlenecks_ Mobile Networks for Classification, Detection and Segmentation
- [2019] Searching for MobileNetV3

### ShuffleNet
---
- [2017] ShuffleNet_ An Extremely Efficient Convolutional Neural Network for Mobile Devices
- [2018] ShuffleNet V2_ Practical Guidelines for Efficient CNN Architecture Design

### MobileFaceNets
---
- [2018] MobileFaceNets_ Efficient CNNs for Accurate Real-time Face Verification on Mobile Devices

### MnasNet
---
- [2018] MnasNet_ Platform-Aware Neural Architecture Search for Mobile

### ChannelNets
---
- [2018 NIPS] ChannelNets_ Compact and Efficient Convolutional Neural Networks via Channel-Wise Convolutions

### MobileNeXt
---
- [[2020] MobileNeXt_ Rethinking Bottleneck Structure for Efficient Mobile Network Design](https://arxiv.org/abs/2007.02269)
- https://github.com/zhoudaquan/rethinking_bottleneck_design


# Block or Module
---

## Deformable convolution
----
- [2017] Deformable Convolutional Networks

## SlimConv
---
- [如何评价新型即插即用模块SlimConv？](https://www.zhihu.com/question/393850908 )
- [2020] SlimConv: Reducing Channel Redundancy in Convolutional Neural Networks by Weights Flipping

## SKConv, Selective Kernel Convolution
---
- [2019 CVPR] Selective Kernel Networks

## MixConv
---
- [2019 BMVC] MixConv: Mixed Depthwise Convolutional Kernels

## OctConv, Octave Convolution
---
- [如何评价最新的Octave Convolution？](https://www.zhihu.com/question/320462422)
- [2019 ICCV] Drop an Octave: Reducing Spatial Redundancy in Convolutional Neural Networks with Octave Convolution



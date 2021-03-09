- 20201109
-----

![](<[2020] Attentional Feature Fusion/paper_title.png>)

本文主要特色是将注意力机制引入了特征融合, 且统一了各种特征融合模式. 特征融合是现代网络架构中的常见组成部分, 它将来自不同层或分支的特征进行组合, 这一组合通常是使用相加或串联方式实现的, 但这往往不是最佳的选择. 鉴于此, 该文提出了一个统一的通用的融合机制, AFF (attentional feature fusion). 具体地, 为了融合语义和尺度不一致的特征, 论文提出了一种多尺度通道注意模块 (MS-CAM, Multi-Scale Channel Attention Module), 其是 SE Block 的变形或扩展; 在 MS-CAM 基础上构建了 AFF; 为了减弱 initial integration 的影响, 论文提出了迭代的 AFF (iAFF). 作者在 CIFAR-100 和 ImageNet 上做了实验, 用较少的参数超过了 SOTA.


## Introduction
提高 CNN 表示能力的方式有: 网络加深 (ResNet), 网络加宽 (Wide ResNet), 提高基数 (ResNeXt), 动态优化特征(注意力机制, 代表有 SENet), 特征融合等. 

笔者注: DenseNet是稠密连接, ResNeXt是稀疏连接.

> The AFF framework generalizes the attention-based feature fusion from the same-layer scenario to cross-layer scenarios including short and long skip connections, and even the initial integration inside AFF itself. It provides a universal and consistent way to improve the performance of various networks, e.g., InceptionNet, ResNet, ResNeXt, and FPN, by simply replacing existing feature fusion operators with the proposed AFF module. Moreover, the AFF framework supports to gradually refine the initial integration, namely the input of the fusion weight generator, by iteratively integrating the received features with another AFF module, which we refer to as iterative attentional feature fusion (iAFF).

## Related Work
物体的scale variation是计算机视觉的一大挑战 (The scale variation of objects is one of the key challenges in computer vision). 常见的解决方法有: 图像金字塔和特征金字塔.

## MS-CAM
![](<[2020] Attentional Feature Fusion/ms_cam.png>)

由上面图示可见, MS-CAM 是 SE Block 的扩展.


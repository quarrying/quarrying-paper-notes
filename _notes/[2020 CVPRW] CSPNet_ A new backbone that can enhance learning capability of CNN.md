- 20210111
----
![](<[2020 CVPRW] CSPNet_ A new backbone that can enhance learning capability of CNN/paper_title.png>)

本文提出了一种名为 Cross Stage Partial Network (CSPNet) 的网络设置, 其结构大致为: 将输入在通道维度上分为两部分, 第一部分不进行任何操作, 第二部分按原来的网络连接操作, 最终的输出是第一部分本身与第二部分输出的某种融合 (见文献中的公式(4)). 作者在 ImageNet 数据集上做了充分的实验, 验证了 DenseNet, ResNet 和 ResNeXt 等经典网络在引入 CSPNet 之后可以在降低计算量的同时提升准确率. 论文还提出了一个新的特征金字塔融合策略, Exact Fusion Model (EFM, 其根据与 ground truth bounding box 匹配的 anchor 的尺寸来选择性的融合某些尺度的特征), 并通过实验验证了其在目标检测任务 (MS COCO 数据集) 中的有效性.

FACTS: 
> For segmentation tasks, since pixel-level labels usually do not contain global information, it is usually more preferable to consider larger patches for better information retrieval [21] ([2016 ICLR] ParseNet: Looking wider to see better). However, for tasks like image classification and object detection, some critical information can be obscure when observed from image-level and bounding box-level labels. Li et al. [15] ([2018 CVPR] Tell me where to look: Guided attention inference network) found that CNN can be often distracted when it learns from image-level labels and concluded that it is one of the main reasons that two-stage object detectors outperform one-stage object detectors.

FACTS: CSPNet 在 YOLOV4 和 Scaled-YOLOV4 中均有见 (这三篇论文的作者来自同一团队).



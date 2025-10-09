## [2016 ECCV] **CTPN**, Connectionist Text Proposal Network
---
只能检测水平方向文本,

**助记**: CTPN, RPN. 不要记做 CPTN.

- [2016 ECCV] Detecting Text in Natural Image with Connectionist Text Proposal Network
- https://github.com/eragonruan/text-detection-ctpn

## [2016] Deeptext
---
提出了 Inception-RPN

- [2016] Deeptext_ A unified framework for text proposal generation and text detection in natural images

## [2017 CVPR] DMPNet
---
- [2017 CVPR] Deep Matching Prior Network_ Toward Tighter Multi-oriented Text Detection

## [2017 CVPR] SegLink
----
改进版的 SSD

- [2017 CVPR] Detecting Oriented Text in Natural Images by link Segments

## [2017 ICCV] DDR, DeepReg, Deep Direct Regression
---
- [2017 ICCV] Deep direct regression for multi-oriented scene text detection

## [2017 ICCV] **EAST**, Efficient and Accurate Scene Text detector
----
- [2017 ICCV] East_ An efficient and accurate scene text detector

## [2017 ICCV] SSTD
---
- [2017 ICCV] Single shot text detector with regional attention

## [2017 AAAI] TextBoxes
---
在 SSD 的模型基础上改了一下 Anchor.

- [2017 AAAI] TextBoxes_ A Fast Text Detector with a Single Deep Neural Network
- https://github.com/MhLiao/TextBoxes

## [2018 TIP] TextBoxes++
---
可以做任意多方向的四边形文字的检测，同时可结合 CRNN 网络做成端到端协调训练的解决方案.

- [2018 TIP] TextBoxes++_ A Single-Shot Oriented Scene Text Detector
- https://github.com/MhLiao/TextBoxes_plusplus

## [2018] Mask TextSpotter
---
- [2018] Mask TextSpotter_ An End-to-End Trainable Neural Network for Spotting Text with Arbitrary Shapes

## [2018] PSENet
---
基于 instance segmentation 的检测框架, 可以检测任意形状文本.

- [2018] PSENet_ Shape Robust Text Detection with Progressive Scale Expansion Network
- https://github.com/WenmuZhou/PSENet.pytorch
- https://github.com/whai362/psenet

## [2018] AF-RPN, Anchor-Free Region Proposal Network
---
- [2018] An Anchor-Free Region Proposal Network for Faster R-CNN based Text Detection Approaches

## [2018 ACM MM] RRPN, Rotation Region Proposal Network
---
基于 region-proposal 的任意方向场景文本检测框架. 

文中提出的 Skew-NMS, 颇令人费解.

- [2018 ACM MM] Arbitrary-Oriented Scene Text Detection via Rotation Proposals
- https://github.com/mjq11302010044/RRPN

## [2018 CVPR] **CLRS**, Corner Localization and Region Segmentation
---
- [2018 CVPR] Multi-Oriented Scene Text Detection via Corner Localization and Region Segmentation

## [2019 CVPR] CRAFT
---
一个任意方向文本检测的算法.

- [2019 CVPR] Character Region Awareness for Text Detection

## [2020 AAAI] **DB**, DBNet, Differentiable Binarization, DBNet++
---
场景文本检测(Scene Text Detection; STD)算法大致可以分为两类: 基于回归的方法和基于分割的方法. 基于分割的STD的优势在于可以描述不同形状的文本, 包括horizontal, multi-oriented and curved text等, 但同时具有后处理复杂的缺点. 二值化是基于分割STD的后处理中的重要步骤, 之前的做法是直接根据固定的全局阈值对分割网络得到的probability map做二值化得到binarization map, 之后还要用一些启发式的方法将binarization map上的前景像素合并为text instances. 本文的主要贡献是: 提出了一个Differentiable Binarization (DB)模块, 其可以在线的学习probability map上每个位置的阈值 (即学习threshold map), 结合probability map和threshold map能得到一个高健壮性的binarization map (文中有述: The differentiable binarization with adaptive thresholds can not only help differentiate text regions from the background, but also separate text instances which are closely jointed.), 简化了后处理操作 (猜测: 不再需要前述的启发式方法合并前景像素这一步骤, 而这一步通常是比较耗时的). 

论文要点: 1) 标准的二值化函数是不可导的, 本文提出了一个标准二值化函数的平滑近似函数; 2) 损失函数分为三部分, 分别为: 监督probability map的损失, 监督threshold map的损失和监督binarization map的损失.

- [2020 AAAI] Real-time Scene Text Detection with Differentiable Binarization
- [2022 TPAMI] Real-Time Scene Text Detection with Differentiable Binarization and Adaptive Scale Fusion
- https://github.com/MhLiao/DB
- https://github.com/WenmuZhou/DBNet.pytorch

## [2018 ICPR] R2CNN
---
- [2018 ICPR] R2cnn_ Rotational region cnn for arbitrarily-oriented scene text detection

## [2018 CVPR] RRD
---
- [2018 CVPR] Rotation-sensitive regression for oriented scene text detection

## [2018] IncepText
---
- [2018] Inceptext_ A new inception-text module with deformable psroi pooling for multi-oriented scene text detection

## [2017 AAAI] FEN
---
- [2017 AAAI] Feature enhancement network_ A refined scene text detector

## [2018 PR] CTD
---
- [2018 PR] Curved scene text detection via transverse and longitudinal sequence connection

## [2018 ECCV] TextSnake
---
- [2018 ECCV] Textsnake_ A flexible representation for detecting text of arbitrary shapes

## [2018 ECCV] Mask TextSpotter
---
- [2018 ECCV] Mask textspotter: An end-to-end trainable neural network for spotting text with arbitrary shapes

## [2016 CVPR] SynthText, FCRN
---
- [2016 CVPR] Synthetic Data for Text Localisation in Natural Images
- https://github.com/ankush-me/SynthText

## [2019 AAAI] DeRPN
---
- [2019 AAAI] Derpn: Taking a further step toward more general object detection

## [2019 CVPR] LOMO
---
- [2019 CVPR] Look More Than Once_ An Accurate Detector for Text of Arbitrary Shapes

## [2019 ICCV] PAN, Pixel Aggregation Network
---
- [2019 ICCV] Efficient and Accurate Arbitrary-Shaped Text Detection with Pixel Aggregation Network

## [2020 CVPR]  ABCNet
---
- [2020 CVPR] Abcnet_ Real-time scene text spotting with adaptive bezier-curve network


# 传统方法

## [2010 CVPR] SWT, Stroke Width Transform
----
大致流程为：利用Canny算子得到图像的边缘图，利用梯度算子得到图像上每个像素的梯度方向（即归一化梯度向量），利用几何知识确定以边缘为开始且以该点处的梯度方向为方向的射线上像素的笔画宽度。边缘像素均做如上处理，得到SWT图。

- [2010 CVPR] Detecting Text in Natural Scenes with Stroke Width Transform

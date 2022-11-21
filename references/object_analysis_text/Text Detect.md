## **CTPN**, Connectionist Text Proposal Network
---
只能检测水平方向文本,

**助记**: CTPN, RPN. 不要记做 CPTN.

- [2016 ECCV] Detecting Text in Natural Image with Connectionist Text Proposal Network
- https://github.com/eragonruan/text-detection-ctpn

## Deeptext
---
提出了 Inception-RPN

- [2016] Deeptext_ A unified framework for text proposal generation and text detection in natural images

## DMPNet
---
- [2017 CVPR] Deep Matching Prior Network_ Toward Tighter Multi-oriented Text Detection

## SegLink
----
改进版的 SSD

- [2017 CVPR] Detecting Oriented Text in Natural Images by link Segments

## DDR, DeepReg, Deep Direct Regression
---
- [2017 ICCV] Deep direct regression for multi-oriented scene text detection

## **EAST**, Efficient and Accurate Scene Text detector
----
- [2017 ICCV] East_ An efficient and accurate scene text detector

## SSTD
---
- [2017 ICCV] Single shot text detector with regional attention

## TextBoxes
---
在 SSD 的模型基础上改了一下 Anchor.

- [2017 AAAI] TextBoxes_ A Fast Text Detector with a Single Deep Neural Network
- https://github.com/MhLiao/TextBoxes

## TextBoxes++
---
可以做任意多方向的四边形文字的检测，同时可结合 CRNN 网络做成端到端协调训练的解决方案.

- [2018 TIP] TextBoxes++_ A Single-Shot Oriented Scene Text Detector
- https://github.com/MhLiao/TextBoxes_plusplus

## Mask TextSpotter
---
- [2018] Mask TextSpotter_ An End-to-End Trainable Neural Network for Spotting Text with Arbitrary Shapes

## PSENet
---
基于 instance segmentation 的检测框架, 可以检测任意形状文本.

- [2018] PSENet_ Shape Robust Text Detection with Progressive Scale Expansion Network
- https://github.com/WenmuZhou/PSENet.pytorch
- https://github.com/whai362/psenet

## AF-RPN, Anchor-Free Region Proposal Network
---
- [2018] An Anchor-Free Region Proposal Network for Faster R-CNN based Text Detection Approaches

## RRPN, Rotation Region Proposal Network
---
基于 region-proposal 的任意方向场景文本检测框架. 

文中提出的 Skew-NMS, 颇令人费解.

- [2018 ACM MM] Arbitrary-Oriented Scene Text Detection via Rotation Proposals
- https://github.com/mjq11302010044/RRPN

## **CLRS**, Corner Localization and Region Segmentation
---
- [2018 CVPR] Multi-Oriented Scene Text Detection via Corner Localization and Region Segmentation

## **DB**, Differentiable Binarization
---
- [2020 AAAI] Real-time Scene Text Detection with Differentiable Binarization
- https://github.com/MhLiao/DB

## R2CNN
---
- [2018 ICPR] R2cnn_ Rotational region cnn for arbitrarily-oriented scene text detection

## RRD
---
- [2018 CVPR] Rotation-sensitive regression for oriented scene text detection

## IncepText
---
- [2018] Inceptext_ A new inception-text module with deformable psroi pooling for multi-oriented scene text detection

## FEN
---
- [2017 AAAI] Feature enhancement network_ A refined scene text detector

## CTD
---
- [2018 PR] Curved scene text detection via transverse and longitudinal sequence connection

## TextSnake
---
- [2018 ECCV] Textsnake_ A flexible representation for detecting text of arbitrary shapes

## Mask TextSpotter
---
- [2018 ECCV] Mask textspotter: An end-to-end trainable neural network for spotting text with arbitrary shapes

## SynthText, FCRN
---
- [2016 CVPR] Synthetic Data for Text Localisation in Natural Images
- https://github.com/ankush-me/SynthText

## DeRPN
---
- [2019 AAAI] Derpn: Taking a further step toward more general object detection

## LOMO
---
- [2019 CVPR] Look More Than Once_ An Accurate Detector for Text of Arbitrary Shapes

## PAN, Pixel Aggregation Network
---
- [2019 ICCV] Efficient and Accurate Arbitrary-Shaped Text Detection with Pixel Aggregation Network

## ABCNet
---
- [2020 CVPR] Abcnet_ Real-time scene text spotting with adaptive bezier-curve network


# 传统方法

## SWT, Stroke Width Transform
----
大致流程为：利用Canny算子得到图像的边缘图，利用梯度算子得到图像上每个像素的梯度方向（即归一化梯度向量），利用几何知识确定以边缘为开始且以该点处的梯度方向为方向的射线上像素的笔画宽度。边缘像素均做如上处理，得到SWT图。

- [2010 CVPR] Detecting Text in Natural Scenes with Stroke Width Transform

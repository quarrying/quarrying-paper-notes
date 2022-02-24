# 综述文献
- [2019] Revisiting a single-stage method for face detection


# 深度学习方法

## CascadeCNN
---
> Li et al. use cascade CNNs for face detection. An extra calibration stage is added after each detection stage which cost extra computing expense on bounding box calibration.
> 
> Li et al. use cascaded CNNs for face detection, but it requires bounding box calibration from face detection with extra computational expense and ignores the inherent correlation between facial landmarks localization and bounding box regression.

- [2015 CVPR] A Convolutional Neural Network Cascade for Face Detection

## Compact CascadeCNN
---
- [2015] Compact Convolutional Neural Network Cascade for Face Detection

## Faceness-Net
---
> Yang et al. extracte the features of hair, eyes, nose, mouth and neck regions with five separate CNNs, combine the result of five CNNs and use the position information to improve face detection result. Due to it’s complex structure, this approach is time costly in practice.

- [2015 ICCV] From Facial Parts Responses to Face Detection_ A Deep Learning Approach

## DP2MFD
---
- [2015] A deep pyramid deformable part model for face detection

## DDFD, Deep Dense Face Detector
---
- [2015 ICMR] Multi-view Face Detection Using Deep Convolutional Neural Networks

## STN, Supervised Transformer Network
---
- [2016] Supervised Transformer Network for Efficient Face Detection

## MTCNN
---
分为三级: Proposal Net (PNet), Refine Net (R-Net), Output Net (O-Net).

PNet 是全卷积的, RNet 和 ONet 都不是全卷积的 (但理论上都可以是全卷积的).

- [2016] Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks
- https://github.com/kpzhang93/MTCNN_face_detection_alignment
- https://github.com/kuaikuaikim/DFace
- https://github.com/DaFuCoding/MTCNN_Caffe/
    - Simple implementation of kpzhang93's paper from Matlab to c++, and don't change models.
- https://github.com/AlphaQi/MTCNN-light
- https://github.com/DuinoDu/mtcnn
- https://github.com/Seanlinx/mtcnn
- https://github.com/cpuimage/MTCNN : MTCNN face detection implementation base NCNN

## Grid loss
---
- [2016 ECCV] Grid loss_ Detecting occluded faces

## HyperFace
---
- [2016] HyperFace_ A Deep Multi-task Learning Framework for Face Detection, Landmark Localization, Pose Estimation, and Gender Recognition

## Xiaomi
----
- [2016] Bootstrapping Face Detection with Hard Negative Examples

## FaceCraft
---
- [2016 CVPR] Joint training of cascaded cnn for face detection

## Faster RCNN
---
- [2016] Face detection with the faster r-cnn
- [2016] CMS-RCNN: contextual multi-scale region-based cnn for unconstrained face detection
- [2017] Face detection using deep learning: An improved faster rcnn approach
- [2018] Face Detection Using Improved Faster RCNN

## 3D with CNN
---
- [2016 ECCV] Face detection with end-to-end integration of a convnet and a 3d model

## S3FD
---
- [2017 ICCV] S3FD_ Single Shot Scale-invariant Face Detector

## SSH
---
- [2017 ICCV] SSH_ Single Stage Headless Face Detector
- https://github.com/imistyrain/SSH-Windows
- https://github.com/mahyarnajibi/caffe-ssh
- https://github.com/Sugoshnr/SSH-Face-Detector
- https://github.com/walsvid/SSH-TensorFlow
- https://github.com/mahyarnajibi/SSH

## [2017] Improved Face Detection and Alignment using Cascade Deep Convolutional Network
---

## FAN, Face Attention Network
---
- [2017 Face++] Face Attention Network_ An Effective Face Detector for the Occluded Faces
- https://github.com/rainofmine/Face_Attention_Network

## FaceBox
---
- [2017 IJCB] Faceboxes: A CPU real-time face detector with high accuracy

## PyramidBox
---
- [2018 Baidu] PyramidBox_ A Context-assisted Single Shot Face Detector

## PyramidBox++
---
- [2019] PyramidBox++: High Performance Detector for Finding Tiny Face 

## BlazeFace
---
该检测框架改编自 SSD.

- [2019] BlazeFace_ Sub-millisecond Neural Face Detection on Mobile GPUs
- https://github.com/shanglianlm0525/BlazeFace

## RetinaFace
---
- [2019] RetinaFace_ Single-stage Dense Face Localisation in the Wild
- https://github.com/deepinsight/insightface/tree/master/RetinaFace

## RefineFace
---
- [2019] RefineFace_ Refinement Neural Network for High Performance Face Detection

## EXTD
---
- [2019] EXTD_ Extremely Tiny Face Detector via Iterative Filter Reuse
- https://github.com/clovaai/EXTD_Pytorch

## AInnoFace
----
- [2019] Accurate Face Detection for High Performance

## CenterFace
---
- [2019] CenterFace_ Joint Face Detection and Alignment Using Face as Point
- https://github.com/chenjun2hao/CenterFace.pytorch
- https://github.com/Star-Clouds/CenterFace

## DSFD
---
- [2019 CVPR] DSFD: Dual shot face detector

## TinaFace
---
- [2021] TinaFace_ Strong but Simple Baseline for Face Detection
- https://github.com/Media-Smart/vedadet/tree/main/configs/trainval/tinaface

## ASFD
---
- [2020] ASFD_ Automatic and Scalable Face Detector


# 传统方法

## Viola-Jones 或称 Haar-Cascade
---
- [2004 IJCV] Robust Real-Time Face Detection

## JDA
---
> Chen et al. jointly conduct alignment and detection with random forest using features of pixel value difference. But, these handcraft features limit its performance a lot.

- [2014 ECCV] Joint Cascade Face Detection and Alignment

## Real Adaboost
---
- [2004] Fast rotation invariant multi-view face detection based on real Adaboost

## Pico, Pixel Intensity Comparison-based Object detection
---
- [2014] Object Detection with Pixel Intensity Comparisons Organized in Decision Trees

## HeadHunter
---
- [2014 ECCV] Face detection without bells and whistles

## NPD, Normalized Pixel Difference
---
An NPD is computed as the ratio of the difference between any two pixel intensity values to the sum of their values, in the same form as the Weber Fraction in experimental psychology.
$$NPD\left( {x,y} \right) = \frac{{x - y}}{{x + y}} = \frac{x}{{x + y}} - \frac{y}{{x + y}}$$
NPD is invariant to scale change of the pixel intensities.

- [2015 TPAMI] A Fast and Accurate Unconstrained Face Detector
- https://github.com/biotrump/NPD/tree/master/NPDFaceDetector

## DPM
---
- [2014 CVPR] The fastest deformable part model for object detection
- [2012 CVPR] Face detection, pose estimation, and landmark localization in the wild


# 戴口罩人脸检测
- 肺炎疫情攻防战--口罩佩戴识别检测 
    - https://god.yanxishe.com/38
- 极市平台视觉算法季度赛-口罩识别
    - http://www.cvmart.net/race/4/base
- Real-World Masked Face Dataset
    - https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset
- face-mask: Wear face masks in the given picture.
    - https://github.com/Prodesire/face-mask
    
    
# 代码
- libfacedetection, 于仕琪开源的项目
    - https://github.com/ShiqiYu/libfacedetection
- DBFace
    - https://github.com/dlunion/DBFace
- Ultra-Light-Fast-Generic-Face-Detector-1MB
    - https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB
- Lightweight-face-detection-CenterNet
    - https://github.com/nvlong21/Lightweight-face-detection-CenterNet

    
# 数据集

## Wider Face
---
WIDER FACE dataset is a face detection benchmark dataset, of which images are selected from the publicly available WIDER dataset. WIDER FACE dataset consists of **393,703 labeled face bounding boxes in 32,203 images** where 50% of them for testing, 40% for training and the remaining for validation. Specifically, the validation set and the test set are divided into three subsets (Easy, Medium, and Hard) for evaluation based on different level of difficulties.

WiderFace dataset contains 32,203 images and 393,703 annotated faces with a high degree of variability in scale, pose and occlusion. 158,989 of these are chosen as train set, 39,496 are in validation set and the rest are test set. The validation set and test set are split into 'easy', 'medium', 'hard' subsets, in terms of the difficulties of the detection.

Furthermore, based on the detection rate of EdgeBox, each subset is defined into three levels of difficulty: 'Easy', 'Medium', 'Hard'. And from further analysis, we find that data in 'Hard' covers 'Medium' and 'Easy', which demonstrate that performance on 'Hard' can better reflect the effectiveness of different methods.

**References**:
- http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/
- http://shuoyang1213.me/WIDERFACE/index.html
- [2016 CVPR] WIDER FACE_ A Face Detection Benchmark

## FDDB
---
FDDB 系 Face Detection Data Set and Benchmark 的简称.

FDDB is a data set of face regions designed for studying the problem of unconstrained face detection. This data set contains the annotations for 5171 faces in a set of 2845 images taken from the Faces in the Wild data set.

There exists a mismatch between annotations in WIDER FACE and FDDB. In particular, the former uses bounding box annotation and the latter employs bounding ellipse annotation.

FDDB, which contains 5, 171 faces extracted from 2, 845 Yahoo news images.

**References**:
- http://vis-www.cs.umass.edu/fddb/
- http://vis-www.cs.umass.edu/fddb/results.html
- [2010 UMass] FDDB_ A benchmark for face detection in unconstrained settings

## MALF
---
MALF 系 Multi-Attribute Labelled Faces 的简称.

**References**:
- http://www.cbsr.ia.ac.cn/faceevaluation/
- [2015 FG] Fine-grained Evaluation on Face Detection in the Wild.

## MAFA
---
MAFA 系 MAsked FAces 的简称.

MAFA dataset contains 30,811 images with 35,806 masked faces collected from Internet. It is a face detection benchmark for masked face, in which faces have vast various orientations and occlusion. Beside, this dataset is divided into masked face subset and unmasked face subset according to whether at least one part of each face is occluded by mask. 

**References**:
- http://www.escience.cn/people/geshiming/mafa.html
- [2017 CVPR] Detecting masked faces in the wild with LLE-CNNs

## UFDD
---
UFDD 系 Unconstrained Face Detection Dataset 的简称.

**References**:
- https://ufdd.info/
- [2018] Pushing the Limits of Unconstrained Face Detection: a Challenge Dataset and Baseline Results

## FDDB-360
---
**References**:
- [2019] FDDB-360_ Face Detection in 360-degree Fisheye Images

## Pascal Faces
---
Pascal Faces is a subset of the Pascal VOC dataset and contains 851 images annotated for face detection.

**References**:
- [2014] Face detection by structural models




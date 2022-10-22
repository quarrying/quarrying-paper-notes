# 综述
- [2014 CVPR] Ten Years of Pedestrian Detection, What Have We Learned?


# 深度学习方法

## [2019 CVPR] SSA-CNN: Semantic Self-Attention CNN for Pedestrian Detection
----

## [2019 CVPR] High-level Semantic Feature Detection:A New Perspective for Pedestrian Detection
----
- https://github.com/liuwei16/CSP

## [2019 CVPR] Pedestrian Detection with Autoregressive Network Phases
---
- https://github.com/garrickbrazil/AR-Ped

## [2018 ECCV] Bi-box regression for pedestrian detection and occlusion estimation
---
The Bi-box model proposes a network to simultaneously detect pedestrian and estimate occlusion by regressing two bounding boxes for full body and visible part estimation respectively. These methods can alleviate the occlusion issue to some extent.

## [2018 CVPR] Domain Adaptive Faster R-CNN for Object Detection in the Wild
---

## [2018 arXiv] MixedPeds-Pedestrian Detection in Unannotated Videos using Synthetically-Generated Human-agents for Training
----
合成训练数据

## [2018 CVPR] Occluded Pedestrian Detection Through Guided Attention in CNNs
---

## [2018 arXiv] Aggregated Channels Network for Real-Time Pedestrian Detection
---

## [2018 CVPR] Structure Inference Net_Object Detection Using Scene Level Context and Instance Level Relationships
---

## [2018 arXiv] Fused Deep Neural Networks for Efficient pedestrian detection
---

## [2018 CVPR] Repulsion loss_ Detecting pedestrians in a crowd
---
The repulsion loss pushes each proposal not only to approach its designated target, but also to keep it away from the other ground truth objects and their corresponding designated proposals.

## [2017 WACV] Fused DNN_ A deep neural network fusion approach to fast and robust pedestrian detection
---

## [2017 BMCV] PCN- Part and Context Information for pedestrian detection with cnns
---

## [2016 TCSVT] Pushing the Limits of Deep CNNs for Pedestrian detection
---

## [2016 SPIC] Deep convolutional neural networks for pedestrian detection
---

## [2016 ECCV] Is faster R-CNN doing well for pedestrian detection
---

## [2016 CVPR] Exploit All the Layers_ Fast and Accurate CNN Object Detector With Scale Dependent Pooling and Cascaded Rejection Classifiers
---

## [2016 arXiv] A Real-Time Pedestrian Detector using Deep Learning for Human-Aware Navigation
---

## [2016 arXiv] A Real-Time Deep Learning Pedestrian Detector for Robot Navigation
---

## [2016 ECCV] Density-Aware Pedestrian Proposal Networks for Robust People Detection in Crowded Scenes
---

## [2016 TMM] Scale-aware Fast R-CNN for Pedestrian Detection
---

## [2016 CVPR] How far are we from solving pedestrian detection
---
修正了 Caltech 数据集标签

## [2015 ICCV] Deep learning strong parts for pedestrian detection
---

## [2015 Neurocomputing] Pedestrian detection based on hierarchical co-occurrence model for occlusion handling
---

## [2015 CVPR] Taking a Deeper Look at Pedestrians
---

## [2015 ICRA] Pedestrian detection with a large-field-of-view deep network
---

## [2015 arXiv] Pedestrian detection aided by deep learning semantic tasks
---

## [2015 BMVC] Real-Time Pedestrian Detection with Deep Network Cascades
---

## [2013 ICCV] Joint deep learning for pedestrian detection
---

## [2012 CVPR] Pedestrian detection at 100 frames per second
---


# 传统方法

## HOG
---
- [2006 CVPR] Fast Human Detection Using a Cascade of Histograms of Oriented Gradients

## ICF
---
- [2009 BMVC] Integral channel features

## GGP
---
- [2009 CVPR] Granularity-Tunable gradients partition (GGP)

## ACF
----
- [2010 BMVC] The fastest pedestrian detector in the west
- [2014] Fast feature pyramids for object detection
- [2014] Aggregate Channel Features for Multi-view Face Detection

## FFP
---
- [2014] Fast feature pyramids for object detection

## LDCF, Locally Decorrelated Channel Features
---
- [2014 NIPS] Local decorrelation for improved pedestrian detection


# 人体与人体部位

## Hand and face detection
---
- https://gitlab.com/StrangeAI/handface_detect.git

## [2020 AAAI] Relational learning for joint head and human detection
---
该论文揭示了人头检测由于判别性信息少容易误检, 人体检测由于遮挡容易漏检, 所以将两者结合可以缓解彼此.

本文工作还包括, 给 CityPersons 和 Caltech-USA 数据集增加了人头包围盒的标注.


# 数据集
----

## CityPersons
---
CityPersons, a new set of person annotations on top of the Cityscapes dataset.

There are 6.5 pedestrians per image and the image resolution is of 2048x1024 pixels.

**References**:
- [2017 CVPR] CityPersons_ A Diverse Dataset for Pedestrian Detection
- https://www.cityscapes-dataset.com/


## Caltech, Caltech-USA
---
The standard Caltech pedestrian dataset consists of 4,250 images for training and 4,024 for test. However, there are only 0.32 pedestrians per image and the image resolution is low (i.e., 640×480 pixels).

**References**:
- [2012 TPAMI] Pedestrian Detection_ An Evaluation of the State of the Art
- [2009 CVPR] Pedestrian Detection_ A Benchmark
- [2018 TPAMI] Towards reaching human performance in pedestrian detection
- http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/


## KITTI
---
**References**:
- [2012 CVPR] Are we ready for autonomous driving_ the KITTI vision benchmark suite
- [2013 IJRR] Vision meets Robotics_ The KITTI Dataset
- http://www.cvlibs.net/datasets/kitti


## INRIA Person Dataset
---
**References**:
- [2015 CVPR] Histograms of Oriented Gradients for Human Detection
- http://pascal.inrialpes.fr/data/human/


## WIDER Pedestrian
---
**References**:
- http://wider-challenge.org/


## CrowdHuman
---
Face++ 开源的一份数据集. 

> Finally, ∼25,000 images are collected in the CrowdHuman dataset. We randomly select 15,000, 4,370 and 5,000 images for training, validation, and testing, respectively.

**References**:
- [2018] CrowdHuman_ A Benchmark for Detecting Human in a Crowd
- http://www.crowdhuman.org/


## RGB-D People Dataset
---
**References**:
- http://www2.informatik.uni-freiburg.de/~spinello/RGBD-dataset.html


## WiderPerson
---
It consists of 13,382 images with 399,786 annotations, i.e., 29.87 annotations per image, varying largely in scenario and occlusion.

**References**:
- [201909] WiderPerson_ A Diverse Dataset for Dense Pedestrian Detection in the Wild
- http://www.cbsr.ia.ac.cn/users/sfzhang/WiderPerson/


## Tsinghua-Daimler Cyclist, TDC
---
**References**:
- [2016] A new benchmark for vision-based cyclist detection


## Multispectral pedestrian
---
**References**:
- [2015 CVPR] Multispectral pedestrian detection: Benchmark dataset and baselin


## EuroCity Persons
----
**References**:
- [2018 TPAMI] The eurocity persons dataset_ A novel benchmark for object detection

## COCOPersons, person subset of MSCOCO
----

# 早期数据集
---

## MIT
----
**References**:
- http://cbcl.mit.edu/software-datasets/PedestrianData.html


## GM-ATCI
---
**References**:
- [2014] Vision-based pedestrian detection for rear-view cameras


## CVC-ADAS
---
**References**:
- [2007] Adaptive image sampling and windows classification for on-board pedestrian detection


## ETH
---
**References**:
- [2007 ICCV] Depth and appearance for mobile scene analysis


## NICTA
---
**References**:
- [2008] A new pedestrian dataset for supervised learning


## USC Pedestrian Detection Test Set
---
**References**:
- http://iris.usc.edu/Vision-Users/OldUsers/bowu/DatasetWebpage/dataset.html
- [2007 ICCV] Cluster boosted tree classifier for multi-view, multi-pose object detection


## TUD-Brussels
---
**References**:
- [2009 CVPR] Multi-cue onboard pedestrian detection


## Daimler
---
**References**:
- [2009 TPAMI] Monocular pedestrian detection_ Survey and experiments

    
## Human-Parts
---
Human-Parts with 14,962 images and 106,879 annotations.
**References**:
- https://github.com/xiaojie1017/Human-Parts

```bibtex
@article{didnet,
	title={Detector-in-Detector: Multi-Level Analysis for Human-Parts},
	author={Xiaojie Li, Lu yang, Qing Song, Fuqiang Zhou},
	journal={arXiv preprint arXiv:****},
	year={2019}
}
```

# Literatures

## Survey
---
- https://github.com/wangxiao5791509/Pedestrian-Attribute-Recognition-Paper-List
- [2019] Pedestrian Attribute Recognition_ A Survey

## [2018] MsVAA
---
- [2018 ECCV] Deep imbalanced attribute classification using visual attention aggregation

## [2019] VAC
---
- [2019 CVPR] Visual attention consistency under image transforms for multi-label image classification

## ALM
---
- [2019 ICCV] Improving pedestrian attribute recognition with weakly-supervised multi-scale attribute-specic localization

## [2020] Rethinking of Pedestrian Attribute Recognition_ Realistic Datasets and A Strong Baseline
---
该论文指出 PETA, RAPv1, RAPv2 数据集的训练集和测试集存在身份重叠.

论文中碰到一个概念: **data leakage**


# Challenges & Datasets

## PETA, PEdesTrian Attribute
---
The PETA dataset consists of 19000 images, with resolution ranging from 17-by-39 to 169-by-365 pixels. Those 19000 images include 8705 persons, each annotated with 61 binary and 4 multi-class attributes.

**References**:
- [2014 ACM MM] Pedestrian attribute recognition at far distance
- http://mmlab.ie.cuhk.edu.hk/projects/PETA.html


## Market-1501 Attribute
---
We annotate 27 attributes for Market-1501. The original dataset contains 751 identities for training and 750 identities for testing. The attributes are annotated in the identity level, thus the file contains 28 x 751 attributes for training and 28 x 750 attributesfor test.

| attribute | repr. in file | label |
| :----: | :----: | :----: |
| gender | gender | male(1), female(2) |
| hair length | hair| short hair(1), long hair(2)    |
| sleeve length | up | long sleeve(1), short sleeve(2) |
| length of lower-body clothing | down | long lower body clothing(1), short(2)    |
| type of lower-body clothing| clothes| dress(1), pants(2)    |
| wearing hat| hat | no(1), yes(2) |
| carrying backpack| backpack | no(1), yes(2) |
| carrying bag| bag | no(1), yes(2) |
| carrying handbag| handbag | no(1), yes(2) |
| age| age | young(1), teenager(2), adult(3), old(4) |
| 8 color of upper-body clothing| upblack, upwhite, upred, uppurple, upyellow, upgray, upblue, upgreen | no(1), yes(2) |
| 9 color of lower-body clothing| downblack, downwhite, downpink, downpurple, downyellow, downgray, downblue, downgreen,downbrown | no(1), yes(2) |

**References**:
- https://github.com/vana77/Market-1501_Attribute
- [2019] Improving Person Re-identification by Attribute and Identity Learning

    
## DukeMTMC Attribute
---
We annotate 23 attributes for DukeMTMC-reID, which is a subset of the DukeMTMC. The original dataset contains 702 identities for training and 1110 identities for testing. The attributes are annotated in the identity level, thus the file contains 24 x 702 attributes for training and 24 x 1110 for test.

| attribute | representation in file | label |
| :----: | :----: | :----: |
| gender | gender | male(1), female(2) |
| length of upper-body clothing | top | short upper body clothing(1), long(2)    |
| wearing boots| boots| no(1), yes(2)    |
| wearing hat| hat | no(1), yes(2) |
| carrying backpack| backpack | no(1), yes(2) |
| carrying bag| bag | no(1), yes(2) |
| carrying handbag| handbag | no(1), yes(2) |
| color of shoes| shoes | dark(1), light(2) |
| 8 color of upper-body clothing| upblack, upwhite, upred, uppurple, upgray, upblue, upgreen, upbrown | no(1), yes(2) |
| 7 color of lower-body clothing| downblack, downwhite, downred, downgray, downblue, downgreen, downbrown | no(1), yes(2) |

**References**:
- https://github.com/vana77/DukeMTMC-attribute

    
## MARS-Attribute
---
We labeled 32 attributes for MARS, the definition of the attributes is from the MARKET-1501_Attribute, the main difference between these two attributes dataset is that MARKET-1501_Attribute is instance-level, while ours is trackets-level.

**References**:
- https://github.com/yuange250/MARS-Attribute


## HAT, Human Attributes
---
Our database contains 9344 images, with annotations for 27 attributes.

**References**:
- https://jurie.users.greyc.fr/datasets/hat.html
- [2011 BMVC] Learning discriminative spatial representation for image classification


## WIDERAttribute
---
**References**:
- http://mmlab.ie.cuhk.edu.hk/projects/WIDERAttribute.html
- [2016 ECCV] Human Attribute Recognition by Deep Hierarchical Contexts


## Berkeley Attributes of People
---
**References**:
- https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/shape/poselets/
- [2009 ICCV] Poselets_ Body Part Detectors Trained Using 3D Human Pose Annotations


## Parse27k
---
- Gender (male, female, ?)
- Posture (standing, walking, (sitting), ?)
- Orientation (4 discretizations + ?)
- Orientation8 (8 discretizations + ?)
- Bag on Left Shoulder (yes, no, ?)
- Bag on Right Shoulder (yes, no, ?)
- Bag in Left Hand (yes, no, ?)
- Bag in Right Hand (yes, no, ?)
- Backpack (yes, no, ?)
- isPushing (yes, no, ?) -- child-strollers, etc.

**References**:
- [2015 ICCVW] Person Attribute Recognition with a Jointly-trained Holistic CNN Model
- https://www.vision.rwth-aachen.de/page/parse27k


## RAP
---
**References**:
- **RAPv1**: [2016] A richly annotated dataset for pedestrian attribute recognition
- **RAPv2**: [2018 TIP] A richly annotated pedestrian dataset for person retrieval in real surveillance scenarios


## PA100k
----
**References**:
- [2017] Hydraplus-net_ Attentive deep features for pedestrian analysis


## APiS
----
**References**:
- [2013 ICCVW] Pedestrian attribute classification in surveillance: Database and evaluation


## Safety-Helmet-Wearing
---
**References**:
- https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset


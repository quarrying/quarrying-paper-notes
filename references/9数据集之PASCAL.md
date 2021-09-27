# PASCAL VOC
PASCAL VOC 系 PASCAL Visual Object Classes Challenge 的简称.

The PASCAL VOC challenge has been held since 2006. Among these PASCAL VOC datasets, VOC2007 and VOC2012 are widely used.

**References**:
- http://pascallin.ecs.soton.ac.uk/challenges/VOC/
- http://host.robots.ox.ac.uk/pascal/VOC/index.html
- [2015 IJCV] The pascal visual object classes challenge: A retrospective
- https://paperswithcode.com/sota/object-detection-on-pascal-voc-2007


## 类名 (20 类)

class name   | class type | 中文
-------------|------------|------
person       | Person     | 人
|
aeroplane    | Vehicle    | 飞机
bicycle      | Vehicle    | 自行车
boat         | Vehicle    | 船
bus          | Vehicle    | 公交车
car          | Vehicle    | 轿车
motorbike    | Vehicle    | 摩托车
train        | Vehicle    | 火车
|
bird         | Animal     | 鸟
cat          | Animal     | 猫
cow          | Animal     | 牛
dog          | Animal     | 狗
horse        | Animal     | 马
sheep        | Animal     | 羊
|
bottle       | Indoor     | 瓶子
chair        | Indoor     | 椅子
dining table | Indoor     | 餐桌
potted plant | Indoor     | 盆栽
sofa         | Indoor     | 沙发
tv/monitor   | Indoor     | 电子/显示器


## PASCAL VOC 2007
PASCAL VOC 2007 dataset which contains 9,963 images of 24,640 annotated objects in training/validation and testing sets. 
PASCAL VOC 2007 consists of about 5k trainval images and 5k test images over 20 object categories.

    voc_2007_train
    voc_2007_val
    voc_2007_trainval
    voc_2007_test

**References**:
- http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
- http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar
- http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCdevkit_08-Jun-2007.tar


## PASCAL VOC 2012
    voc_2012_train
    voc_2012_val
    voc_2012_trainval
    voc_2012_test
    
**References**:
- http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar


## VOCaug
**References**:
- http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/semantic_contours/benchmark.tgz

    
## PASCAL Context
This dataset is a set of additional annotations for PASCAL VOC 2010. 
It goes beyond the original PASCAL semantic segmentation task by providing annotations for the whole scene. 

**References**:
- https://cs.stanford.edu/~roozbeh/pascal-context/


## 常见用法
- 用法一
    - train: VOC2007 trainval and VOC2012 trainval 
    - test: VOC2007 test
- 用法二
    - train: VOC2007 trainvaltest and VOC2012 trainval 
    - test: VOC2012 test





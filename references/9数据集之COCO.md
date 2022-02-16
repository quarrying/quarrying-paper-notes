# MS-COCO, Microsoft Common Objects in COntext

> The MS COCO (Microsoft Common Objects in Context) dataset is a large-scale object detection, segmentation, key-point detection, and captioning dataset. The dataset consists of 328K images.
> 
> Splits: The first version of MS COCO dataset was released in 2014. It contains 164K images split into training (83K), validation (41K) and test (41K) sets. In 2015 additional test set of 81K images was released, including all the previous test images and 40K new images.
> 
> Based on community feedback, in 2017 the training/validation split was changed from 83K/41K to 118K/5K. The new split uses the same images and annotations. The 2017 test set is a subset of 41K images of the 2015 test set. Additionally, the 2017 release contains a new unannotated dataset of 123K images.
>> https://paperswithcode.com/dataset/coco

**References**
- [2014 ICCV] Microsoft COCO_ Common objects in context
- http://mscoco.org/home/
- http://cocodataset.org/
- https://github.com/cocodataset/cocoapi
- https://paperswithcode.com/sota/object-detection-on-coco
- https://paperswithcode.com/sota/object-detection-on-coco-minival


## MS-COCO 2014

    coco_2014_train
    coco_2014_val
    coco_2014_minival
    coco_2014_valminusminival


### 下载链接
- train2014 images (13GB)
    - http://images.cocodataset.org/zips/train2014.zip
    - http://msvocds.blob.core.windows.net/coco2014/train2014.zip
- val2014 images (6GB)
    - http://images.cocodataset.org/zips/val2014.zip
    - http://msvocds.blob.core.windows.net/coco2014/val2014.zip
- train2014/val2014 annotations (241MB)
    - http://images.cocodataset.org/annotations/annotations_trainval2014.zip
- test2014 images (12GB)
    - http://images.cocodataset.org/zips/test2014.zip


## MS-COCO 2015

    coco_2015_test
    coco_2015_test-dev
    
    
## MS-COCO 2017
MS-COCO 2017 dataset to evaluate the performance of
the proposed detection networks, which is a set of learning 
datasets for object detection, instance segmentation, semantic 
segmentation, panoptic segmentation, key-point estimation, 
and caption generation tasks according to the desired output 
type to be inferred.

### 下载链接
- train2017 images (18GB)
    - http://images.cocodataset.org/zips/train2017.zip
- val2017 images (1GB)
    - http://images.cocodataset.org/zips/val2017.zip
- test2017 images (6GB)
    - http://images.cocodataset.org/zips/test2017.zip
- train2017/val2017 annotations (241MB)
    - http://images.cocodataset.org/annotations/annotations_trainval2017.zip
- stuff train2017/val2017 annotations (1.1GB)
    - http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip
- image_info_test2017
    - http://images.cocodataset.org/annotations/image_info_test2017.zip 
- Panoptic train2017/val2017 annotations (821MB)
    - http://images.cocodataset.org/annotations/panoptic_annotations_trainval2017.zip
- Unlabeled2017 images (19GB)
    - http://images.cocodataset.org/zips/unlabeled2017.zip


## 常见用法 (MS-COCO 2017)

split       | num_images
------------|--------
trainval35k | 118K 
minival     | 5K 
test-dev    | 20K 

An ablation study is performed using the validation set, and a system-level comparison is reported on test-dev.

## COCO-Things 类名
原来有 91 类, 去掉 11 类, 还剩下 80 类.

class name       | class type | In Pascal VOC | Removed | 中文
-----------------|------------|---------------|---------|---------
person           | Person     | YES           |         | 人
| 
bicycle          | Vehicle    | YES           |         | 自行车
car              | Vehicle    | YES           |         | 轿车
motorcycle       | Vehicle    | YES           |         | 摩托车
airplane         | Vehicle    | YES           |         | 飞机
bus              | Vehicle    | YES           |         | 公交车
train            | Vehicle    | YES           |         | 火车
truck            | Vehicle    |               |         | 卡车
boat             | Vehicle    | YES           |         | 船
| 
traffic light    | Outdoor    |               |         | 交通信号灯
fire hydrant     | Outdoor    |               |         | 消防栓
street sign      | Outdoor    |               | YEAH    | 路标
stop sign        | Outdoor    |               |         | 停止标志
parking meter    | Outdoor    |               |         | 停车收费器
bench            | Outdoor    |               |         | 长凳
| 
bird             | Animal     | YES           |         | 鸟
cat              | Animal     | YES           |         | 猫
dog              | Animal     | YES           |         | 狗
horse            | Animal     | YES           |         | 马
sheep            | Animal     | YES           |         | 羊
cow              | Animal     | YES           |         | 牛
elephant         | Animal     |               |         | 象
bear             | Animal     |               |         | 熊
zebra            | Animal     |               |         | 斑马
giraffe          | Animal     |               |         | 长颈鹿
| 
hat              | Accessory  |               | YEAH    | 帽子
backpack         | Accessory  |               |         | 背包
umbrella         | Accessory  |               |         | 雨伞
shoe             | Accessory  |               | YEAH    | 鞋子
eye glasses      | Accessory  |               | YEAH    | 眼镜
handbag          | Accessory  |               |         | 小手提包
tie              | Accessory  |               |         | 领带
suitcase         | Accessory  |               |         | 手提箱
| 
frisbee          | Sports     |               |         | 飞盘
skis             | Sports     |               |         | 滑雪板?
snowboard        | Sports     |               |         | 滑雪板?
sports ball      | Sports     |               |         | 运动球?
kite             | Sports     |               |         | 风筝
baseball bat     | Sports     |               |         | 棒球棒
baseball glove   | Sports     |               |         | 棒球手套
skateboard       | Sports     |               |         | 滑板
surfboard        | Sports     |               |         | 冲浪板
tennis racket    | Sports     |               |         | 网球拍
| 
bottle           | Kitchen    | YES           |         | 瓶子
plate            | Kitchen    |               | YEAH    | 盘子
wine glass       | Kitchen    |               |         | 玻璃酒杯
cup              | Kitchen    |               |         | 杯子
fork             | Kitchen    |               |         | 叉子
knife            | Kitchen    |               |         | 刀
spoon            | Kitchen    |               |         | 勺
bowl             | Kitchen    |               |         | 碗
| 
banana           | Food       |               |         | 香蕉
apple            | Food       |               |         | 苹果
sandwich         | Food       |               |         | 三明治
orange           | Food       |               |         | 橘子
broccoli         | Food       |               |         | 西兰花
carrot           | Food       |               |         | 胡萝卜
hot dog          | Food       |               |         | 热狗
pizza            | Food       |               |         | 披萨
donut            | Food       |               |         | 油炸圈饼
cake             | Food       |               |         | 蛋糕
| 
chair            | Furniture  | YES           |         | 椅子
couch            | Furniture  | YES           |         | 沙发
potted plant     | Furniture  | YES           |         | 盆栽植物
bed              | Furniture  |               |         | 床
mirror           | Furniture  |               | YEAH    | 镜子
dining table     | Furniture  | YES           |         | 餐桌
window           | Furniture  |               | YEAH    | 窗户
desk             | Furniture  |               | YEAH    | 书桌
toilet           | Furniture  |               |         | 厕所
door             | Furniture  |               | YEAH    | 门
|
tv               | Electronic | YES           |         | 电视
laptop           | Electronic |               |         | 笔记本电脑
mouse            | Electronic |               |         | 鼠标
remote           | Electronic |               |         | ?
keyboard         | Electronic |               |         | 键盘
cell phone       | Electronic |               |         | 手机
|
microwave        | Appliance  |               |         | 微波炉
oven             | Appliance  |               |         | 烤箱
toaster          | Appliance  |               |         | 烤面包片器
sink             | Appliance  |               |         | 洗碗槽
refrigerator     | Appliance  |               |         | 冰箱
blender          | Appliance  |               | YEAH    | 食物搅拌器
|
book             | Indoor     |               |         | 书
clock            | Indoor     |               |         | 钟表
vase             | Indoor     |               |         | 花瓶
scissors         | Indoor     |               |         | 剪刀
teddy bear       | Indoor     |               |         | 玩具熊
hair drier       | Indoor     |               |         | 吹风机
toothbrush       | Indoor     |               |         | 牙刷
hair brush       | Indoor     |               | YEAH    | 毛刷


**Notes**:
PASCAL 和 COCO 中有几例类相同, 但类名不同的情况, 如下:
- motorcycle == motorbike
- couch == sofa
- airplane == aeroplane
- tv == tv/monitor

**References**:
- https://github.com/nightrome/cocostuff/blob/master/labels.md


## COCO 标注格式
COCO has five annotation types: for object detection, keypoint detection, stuff segmentation, panoptic segmentation, and image captioning. The annotations are stored using JSON. Please note that the COCO API described on the download page can be used to access and manipulate all anotations. All annotations share the same basic data structure below:
The data structures specific to the various annotation types are described below.

**References**:
- http://cocodataset.org/#detection-2018
- http://cocodataset.org/#keypoints-2018
- http://cocodataset.org/#stuff-2018
- http://cocodataset.org/#panoptic-2018
- http://cocodataset.org/#captions-2015
- https://blog.csdn.net/chengyq116/article/details/80480709
- https://www.immersivelimit.com/tutorials/create-coco-annotations-from-scratch


## pycocotools

### 测试代码:
```python
import pycocotools
from pycocotools.coco import COCO

if __name__ == '__main__':
    filename = '/data/bitahub/MSCOCO/2014/annotations/instances_train2014.json'
    coco_train = COCO(filename)
    print(len(coco_train.dataset['categories']))
    print(len(coco_train.dataset['images']))
    print(len(coco_train.dataset['annotations']))
```

**References**:
- https://github.com/cocodataset/cocoapi
- https://pypi.org/project/pycocotools


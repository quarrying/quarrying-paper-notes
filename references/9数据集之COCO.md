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
> MS-COCO 2017 dataset to evaluate the performance of the proposed detection networks, which is a set of learning datasets for object detection, instance segmentation, semantic segmentation, panoptic segmentation, key-point estimation, and caption generation tasks according to the desired output type to be inferred.


### MS-COCO 2017下载链接
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


### MS-COCO 2017 数据规模

split       | num_images
------------|--------
train       | 118,287 
val         | 5,000
test        | 40,670
unlabeled   | 123,403


## COCO-Things 类名
注意: COCO 中 Things 和 Stuffs 之间的区别.

原来有 91 类, 去掉 11 类, 还剩下 80 类. (在 `instances_train2017.json` 或 `instances_val2017.json` 文件内容中的 `categories `字段可以看到有哪些类别及其 ID) 


id  | class name       | Supercategory | In Pascal VOC | Removed | 中文
----|------------------|---------------|---------------|---------|---------
1   | person           | Person        | YES           |         | 人
| 
2   | bicycle          | Vehicle       | YES           |         | 自行车
3   | car              | Vehicle       | YES           |         | 轿车
4   | motorcycle       | Vehicle       | YES           |         | 摩托车
5   | airplane         | Vehicle       | YES           |         | 飞机
6   | bus              | Vehicle       | YES           |         | 公交车
7   | train            | Vehicle       | YES           |         | 火车
8   | truck            | Vehicle       |               |         | 卡车
9   | boat             | Vehicle       | YES           |         | 船
| 
10  | traffic light    | Outdoor       |               |         | 交通信号灯
11  | fire hydrant     | Outdoor       |               |         | 消防栓
12  | street sign      | Outdoor       |               | YEAH    | 路标
13  | stop sign        | Outdoor       |               |         | 停止标志
14  | parking meter    | Outdoor       |               |         | 停车收费器
15  | bench            | Outdoor       |               |         | 长凳
| 
16  | bird             | Animal        | YES           |         | 鸟
17  | cat              | Animal        | YES           |         | 猫
18  | dog              | Animal        | YES           |         | 狗
19  | horse            | Animal        | YES           |         | 马
20  | sheep            | Animal        | YES           |         | 羊
21  | cow              | Animal        | YES           |         | 牛
22  | elephant         | Animal        |               |         | 象
23  | bear             | Animal        |               |         | 熊
24  | zebra            | Animal        |               |         | 斑马
25  | giraffe          | Animal        |               |         | 长颈鹿
| 
26  | hat              | Accessory     |               | YEAH    | 帽子
27  | backpack         | Accessory     |               |         | 背包
28  | umbrella         | Accessory     |               |         | 雨伞
29  | shoe             | Accessory     |               | YEAH    | 鞋子
30  | eye glasses      | Accessory     |               | YEAH    | 眼镜
31  | handbag          | Accessory     |               |         | 小手提包
31  | tie              | Accessory     |               |         | 领带
33  | suitcase         | Accessory     |               |         | 手提箱
| 
34  | frisbee          | Sports        |               |         | 飞盘
35  | skis             | Sports        |               |         | 滑雪板?
36  | snowboard        | Sports        |               |         | 滑雪板?
37  | sports ball      | Sports        |               |         | 运动球?
38  | kite             | Sports        |               |         | 风筝
39  | baseball bat     | Sports        |               |         | 棒球棒
40  | baseball glove   | Sports        |               |         | 棒球手套
41  | skateboard       | Sports        |               |         | 滑板
42  | surfboard        | Sports        |               |         | 冲浪板
43  | tennis racket    | Sports        |               |         | 网球拍
| 
44  | bottle           | Kitchen       | YES           |         | 瓶子
45  | plate            | Kitchen       |               | YEAH    | 盘子
46  | wine glass       | Kitchen       |               |         | 玻璃酒杯
47  | cup              | Kitchen       |               |         | 杯子
48  | fork             | Kitchen       |               |         | 叉子
49  | knife            | Kitchen       |               |         | 刀
50  | spoon            | Kitchen       |               |         | 勺
51  | bowl             | Kitchen       |               |         | 碗
| 
52  | banana           | Food          |               |         | 香蕉
53  | apple            | Food          |               |         | 苹果
54  | sandwich         | Food          |               |         | 三明治
55  | orange           | Food          |               |         | 橘子
56  | broccoli         | Food          |               |         | 西兰花
57  | carrot           | Food          |               |         | 胡萝卜
58  | hot dog          | Food          |               |         | 热狗
59  | pizza            | Food          |               |         | 披萨
60  | donut            | Food          |               |         | 油炸圈饼
61  | cake             | Food          |               |         | 蛋糕
| 
62  | chair            | Furniture     | YES           |         | 椅子
63  | couch            | Furniture     | YES           |         | 沙发
64  | potted plant     | Furniture     | YES           |         | 盆栽植物
65  | bed              | Furniture     |               |         | 床
66  | mirror           | Furniture     |               | YEAH    | 镜子
67  | dining table     | Furniture     | YES           |         | 餐桌
68  | window           | Furniture     |               | YEAH    | 窗户
69  | desk             | Furniture     |               | YEAH    | 书桌
70  | toilet           | Furniture     |               |         | 厕所
71  | door             | Furniture     |               | YEAH    | 门
|
72  | tv               | Electronic    | YES           |         | 电视
73  | laptop           | Electronic    |               |         | 笔记本电脑
74  | mouse            | Electronic    |               |         | 鼠标
75  | remote           | Electronic    |               |         | ?
76  | keyboard         | Electronic    |               |         | 键盘
77  | cell phone       | Electronic    |               |         | 手机
|
78  | microwave        | Appliance     |               |         | 微波炉
79  | oven             | Appliance     |               |         | 烤箱
80  | toaster          | Appliance     |               |         | 烤面包片器
81  | sink             | Appliance     |               |         | 洗碗槽
82  | refrigerator     | Appliance     |               |         | 冰箱
83  | blender          | Appliance     |               | YEAH    | 食物搅拌器
|
84  | book             | Indoor        |               |         | 书
85  | clock            | Indoor        |               |         | 钟表
86  | vase             | Indoor        |               |         | 花瓶
87  | scissors         | Indoor        |               |         | 剪刀
88  | teddy bear       | Indoor        |               |         | 玩具熊
89  | hair drier       | Indoor        |               |         | 吹风机
90  | toothbrush       | Indoor        |               |         | 牙刷
91  | hair brush       | Indoor        |               | YEAH    | 毛刷


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


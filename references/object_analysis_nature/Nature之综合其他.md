# Datasets

## Stanford Dogs
----
The Stanford Dogs dataset contains images of 120 breeds of dogs from around the world. This dataset has been built using images and annotation from **ImageNet** for the task of fine-grained image categorization. Contents of this dataset:

    Number of categories: 120
    Number of images: 20,580
    Annotations: Class labels, Bounding boxes

**References**:
- [2011 CVPRW] Novel dataset for fine-grained image categorization
- http://vision.stanford.edu/aditya86/ImageNetDogs/main.html
- https://www.kaggle.com/jessicali9530/stanford-dogs-dataset


## Oxford-IIIT Pet Dataset
---
We have created a 37 category pet dataset with roughly 200 images for each class. The images have a large variations in scale, pose and lighting. All images have an associated ground truth annotation of breed, head ROI, and pixel level trimap segmentation.

**References**:
- Parkhi, O.M., Vedaldi, A., Zisserman, A., Jawahar, C.V.: Cats and dogs. In: CVPR (2012)
- http://www.robots.ox.ac.uk/~vgg/data/pets/


## Raccoon Detector Dataset
---
This is a dataset that I collected to train my own Raccoon detector with TensorFlow's Object Detection API. Images are from Google and Pixabay. In total, there are 200 images (160 are used for training and 40 for validation).

**Remarks**: Raccoon 意即浣熊; 北美浣熊.

**References**:
- https://github.com/datitran/raccoon_dataset


## Datasets on Kaggle
---
**References**:
- https://www.kaggle.com/c/dog-breed-identification/overview
- https://www.kaggle.com/alessiocorrado99/animals10
- https://www.kaggle.com/slothkong/10-monkey-species
- https://www.kaggle.com/antoreepjana/animals-detection-images-dataset

## WebFG 5000
---
数据集是从网络上收集的图片数据，jpg 格式。数据集中包含的类别包括各种动物和植物。
- 训练数据集: 5000类共557169张图片，含标注信息（内含标签噪声）。数据被归为5000个文件夹，每个文件夹内包含该类的数据。
- 测试数据集: 5000类共100000张图片，不含标注信息。

**Remarks**:
该数据集非常脏.

**References**:
- https://www.cvmart.net/race/9917/base
- ACCV2020细粒度比赛记录-数据处理和Baseline结果分享
    - https://blog.csdn.net/u013347145/article/details/109250455
- [2020 ACCV] Webly-Supervised Fine-Grained Recognition Challenge


## iNat2017
---
Super-Class             | Class | Train   | Val    | BBoxes
------------------------|-------|---------|--------|--------
Plantae 植物界          | 2,101 | 158,407 | 38,206 | -
Insecta 昆虫纲          | 1,021 | 100,479 | 18,076 | 125,679
Aves 鸟纲               |   964 | 214,295 | 21,226 | 311,669
Reptilia 爬行纲         |   289 |  35,201 |  5,680 |  42,351
Mammalia 哺乳纲         |   186 |  29,333 |  3,490 |  35,222
Fungi 真菌              |   121 |   5,826 |  1,780 | -
Amphibia 两栖纲         |   115 |  15,318 |  2,385 |  18,281
Mollusca 软体动物门     |    93 |   7,536 |  1,841 |  10,821
Animalia 动物界         |    77 |   5,228 |  1,362 |   8,536
Arachnida 蛛形纲        |    56 |   4,873 |  1,086 |   5,826
Actinopterygii 辐鳍鱼纲 |    53 |   1,982 |    637 |   3,382
Chromista 假菌界        |     9 |     398 |    144 | -
Protozoa 原生动物门     |     4 |     308 |     73 | -
Total                   | 5,089 | 579,184 | 95,986 | 561,767

**References**:
- [2018] The iNaturalist Species Classification and Detection Dataset
- https://github.com/visipedia/inat_comp/tree/master/2017
- 

## AwA2, Animals with Attributes v2
----
It consists of 37322 images of 50 animals classes with pre-extracted feature representations for each image. 
**References**:
- https://cvml.ist.ac.at/AwA2/


## NDD20, Northumberland Dolphin Dataset 2020
----
Northumberland Dolphin Dataset 2020 (NDD20) is a challenging image dataset annotated for both coarse and fine-grained instance segmentation and categorisation. This dataset, the first release of the NDD, was created in response to the rapid expansion of computer vision into conservation research and the production of field-deployable systems suited to extreme environmental conditions -- an area with few open source datasets. NDD20 contains a large collection of above and below water images of two different dolphin species for traditional coarse and fine-grained segmentation.

**References**:
- https://www.paperswithcode.com/dataset/ndd20

## AFHQ, Animal faces
---
Animal faces (AFHQ) includes ∼5k closeups per category for dogs, cats, and wild life.

**References**:
- [2020 CVPR] StarGAN v2: Diverse image synthesis for multiple domains


# Products
- 生物记
    - http://nol.especies.cn/
    - https://ai.baidu.com/customer/shengwuji
    

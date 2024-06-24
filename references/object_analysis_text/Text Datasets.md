## Overview
----
**References**:
- OCR_DataSet: https://github.com/WenmuZhou/OCR_DataSet


## MNIST
---
**References**:
- http://yann.lecun.com/exdb/mnist/


## SVT, Street View Text
---
**References**:
- http://vision.ucsd.edu/~kai/svt/
- [2010 ECCV] Word Spotting in the Wild
- [2011 ICCV] End-to-end Scene Text Recognition


## SVHN, Street View House Numbers
---
> SVHN is a real-world image dataset for developing machine learning and object recognition algorithms with minimal requirement on data preprocessing and formatting. It can be seen as similar in flavor to MNIST (e.g., the images are of small cropped digits), but incorporates an order of magnitude more labeled data (over 600,000 digit images) and comes from a significantly harder, unsolved, real world problem (recognizing digits and numbers in natural scene images). SVHN is obtained from house numbers in Google Street View images. 

There are 73,257 images in the training set, 26,032 images in the test set, and 531,131 images for additional training. 

**References**:
- http://ufldl.stanford.edu/housenumbers/
- [2011 NIPSW] Reading Digits in Natural Images with Unsupervised Feature Learning


## CISIA-HWDB, HWDB1.0
---
**References**:
- http://www.nlpr.ia.ac.cn/databases/handwriting/download.html


## HCL2000
---
- [2009] HCL2000 - A Large-scale Handwritten Chinese Character Database for Handwritten Character Recognition


## Chars74K
---
**References**:
- http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/
- [2009] Character recognition in natural images


## ICDAR 2003
---
**References**:
- [2003 ICDAR] ICDAR 2003 robust reading competitions


## ICDAR 2011
---
The ICDAR 2011 dataset includes 229 and 255 images for training and testing.

**References**:
- Snoopertext: A multiresolution system for text detection in complex visual scenes


## ICDAR 2013
---
The ICDAR 2013 dataset consists of 229 training images and 233 testing images in different resolutions. This dataset contains only horizontal or nearly horizontal text.

**References**:
- ICDAR 2013 robust reading competition (2013)


## ICDAR 2015
---
ICDAR2015 contains natural images that are captured by Google Glasses casually, and most of them are severely distorted or blurred. There are 1000 training images and 500 testing images, which are annotated with quadrilaterals.

**References**:
- ICDAR 2015 competition on robust reading (2015)

### ICDAR 2015 Competition Challenge 4: Incidental Scene Text


## ICDAR 2017
---
**References**:
- http://u-pat.org/ICDAR2017/index.php
- http://u-pat.org/ICDAR2017/program_competitions.php

### ICDAR2017-RCTW, RCTW-17, ICDAR2017 Competition on Reading Chinese Text in the Wild
共包含 12,000+ 图像, 大部分图片是通过手机摄像头在野外采集的. 有些是截图. 这些图片展示了各种各样的场景, 包括街景, 海报, 菜单, 室内场景和手机应用程序的截图. 

**References**:
- http://rctw.vlrlab.net/result/
- [2017] Icdar2017 competition on reading chinese text in the wild (rctw-17)

### ICDAR2017 Robust Reading Challenge on COCO-Text
**References**:
- https://rrc.cvc.uab.es/?ch=5&com=introduction
- [2017] ICDAR2017 Robust Reading Challenge on COCO-Text

### ICDAR2017-MLT
ICDAR 2017 MLT (IC17-MLT) is a large scale multi-lingual text dataset, which includes 7200 training images, 1800 validation images and 9000 testing images. The dataset is composed of complete scene images which come from 9 languages. Similarly with ICDAR 2015, the text regions in ICDAR 2017 MLT are also annotated by 4 vertices of the quadrangle.

**References**:
- [2017] ICDAR2017 robust reading challenge on multi-lingual scene text detection and script identification-rrc-mlt


## ICDAR 2019
---
**References**:
- http://icdar2019.org/

### ICDAR2019-LSVT, ICDAR 2019 Robust Reading Challenge on Large-scale Street View Text with Partial Labeling
共 45w 中文街景图像, 包含 5w (2w 测试 + 3w 训练) 全标注数据 (文本坐标 + 文本内容), 40w 弱标注数据 (仅文本内容). 

**References**:
- https://ai.baidu.com/broad/download?dataset=lsvt

### ICDAR2019-ArT, ICDAR 2019 Robust Reading Challenge on Arbitrary-Shaped Text
共包含 10,166 张图像, 训练集 5603 图, 测试集 4563 图. 由 Total-Text, SCUT-CTW1500, Baidu Curved Scene Text 三部分组成, 包含水平, 多方向和弯曲等多种形状的文本. 

**References**:
- https://ai.baidu.com/broad/download?dataset=art

### ICDAR2019-ReCTS, ICDAR 2019 Robust Reading Challenge on Reading Chinese Text on Signboard
> We collect and construct a practical and challenging multi-orientation natural scene text dataset (ReCTS) with 25,000 images, which consist of lots of signboards. In the dataset, all text lines and characters are labeled with locations and character codes. Besides, four tasks are presents for this competition: (1) end-to-end recognition on the signboards, (2) text line localization on the signboards, (3) character recognition on the signboards, (4) text line recognition on the signboards.

**References**:
- https://rrc.cvc.uab.es/?ch=12


## ICDAR 2021
---
**References**:
- https://icdar2021.org/


## DDI-100
---
**References**:
- [2019] DDI-100_ Dataset for Text Detection and Recognition


## CTW-1500, SCUT-CTW1500
---
CTW1500 is a curved English text dataset that consists of 1000 training images and 500 testing images. All the text instances are annotated with 14 vertices.

**References**:
- [2017] Detecting curve text in the wild_ New dataset and new solution
- https://github.com/Yuliang-Liu/Curve-Text-Detector


## Total-Text
---
Total-Text is a word-level based English text dataset. It consists of 1255 training images and 300 testing images, which contain horizontal texts, multi-oriented texts, and curved texts.

**References**:
- [2017 ICDAR] Total-text_ A comprehensive dataset for scene text detection and recognition
- https://github.com/cs-chan/Total-Text-Dataset


## SynthText
---
The SynthText dataset contains 800k synthesized text images, created via blending rendered words with natural images. As the location and transform of text are carefully chosen with a learning algorithm, the synthesized images look realistic.

**References**:
- [2016 CVPR] Synthetic data for text localisation in natural images


## COCO-Text
---
It reuses the images from MS-COCO dataset.  Word regions are annotated in the form of axis-aligned bounding box (AABB)

The COCO-Text dataset is currently the largest dataset for scene text detection and recognition. It contains 43686 training images and 20000 images for validation/testing.

**References**:
- [2016] Coco-text_ Dataset and benchmark for text detection and recognition in natural images


## CUTE80
---
CUTE80: Curve Text Dataset

**References**:
- http://cs-chan.com/downloads_CUTE80_dataset.html
- [2014] A Robust Arbitrary Text Detection System for Natural Scene Images


## MSRA-TD500, MSRA Text Detection 500
---
>The MSRA Text Detection 500 Database (MSRA-TD500) contains 500 natural images, which are taken from indoor (office and mall) and outdoor (street) scenes using a pocket camera. MSRA-TD500 is a multi-lingual long text dataset for Chinese and English. It includes 300 training images and 200 testing images with arbitrary orientations.

**References**:
- [2012 CVPR] Detecting texts of arbitrary orientations in natural images
- [2018 ACM MM] Arbitrary-Oriented Scene Text Detection via Rotation Proposals
- http://www.iapr-tc11.org/mediawiki/index.php/MSRA_Text_Detection_500_Database_%28MSRA-TD500%29


## HUST-TR400
---
**References**:
- [2014 TIP] A unified framework for multi-oriented text detection and recognition


## MLT-2017
---
MLT-2017 dataset is a multi-language dataset. It includes 9 languages representing 6 different scripts. There are 7,200 training images, 1,800 validation images and 9,000 testing images in this dataset.

**References**:
- https://rrc.cvc.uab.es/?ch=8


## CTW
---
- 32,285 high resolution images
- 1,018,402 character instances
- 3,850 character categories
- 6 kinds of attributes

**References**:
- [2019] A Large Chinese Text Dataset in the Wild
- https://ctwdataset.github.io/
- https://github.com/yuantailing/ctw-baseline


## Chinese Calligraphy Styles by Calligraphers
---
- https://www.kaggle.com/datasets/yuanhaowang486/chinese-calligraphy-styles-by-calligraphers

## 其他: 中文街景文字识别
---
共包括29万张图片, 其中21万张图片作为训练集 (带标注) , 8万张作为测试集 (无标注) . 数据集采自中国街景, 并由街景图片中的文字行区域 (例如店铺标牌, 地标等等) 截取出来而形成. 所有图像都经过一些预处理, 将文字区域利用仿射变化, 等比映射为一张高为48像素的图片. 

**References**:
- https://aistudio.baidu.com/aistudio/competition/detail/8


## 其他: 中文文档文字识别
---
共约364万张图片, 按照99:1划分成训练集和验证集. 数据利用中文语料库 (新闻 + 文言文) , 通过字体, 大小, 灰度, 模糊, 透视, 拉伸等变化随机生成.

**References**:
- https://github.com/YCG09/chinese_ocr


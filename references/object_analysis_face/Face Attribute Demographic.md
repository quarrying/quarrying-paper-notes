# Papers about Demographic (Gender Age and Race)
- [2013 TPAMI] Facial age estimation by learning from label distributions
- [2015 ICCVW] AgeNet_ Deeply Learned Regressor and Classifier for Robust Apparent Age Estimation
- LDL
    - [2017 TIP] Deep Label Distribution Learning with Label Ambiguity
    - [2015 ICCVW] Deep Label Distrubution Learning for Appearent Age Estimation
- DEX
    - [2015 ICCVW] DEX_ Deep EXpectation of apparent age from a single image
    - [2016 IJCV] Deep expectation of real and apparent age from a single image without facial landmarks
- [2016] A Cascaded Convolutional Neural Network for Age Estimation of Unconstrained Faces
- [2016 CVPRW] Apparent Age Estimation from Face Images Combining General and Children-Specialized Deep Learning Models
- [2017 CVPR] Using Ranking-CNN for Age Estimation
- SSR
    - [2018 IJCAI] SSR-Net_ A compact soft stagewise regression network for age estimation
    - https://github.com/shamangary/SSR-Net
    - https://github.com/oukohou/SSR_Net_Pytorch
- MV
    - [2018 CVPR] Mean-variance loss for deep age estimation from a face
- C3AE
    - [2019 CVPR] C3AE_ Exploring the Limits of Compact Model for Age Estimation
- FairFace
    - [2019] FairFace_ Face Attribute Dataset for Balanced Race, Gender, and Age


# Challenges & Datasets

## FairFace
---
containing 108,501 images, with an emphasis of balanced race composition in the dataset. We define 7 race groups: White, Black, Indian, East Asian, Southeast Asian, Middle East, and Latino. Images were collected from the YFCC-100M Flickr dataset and labeled with race, gender, and age groups. 

**References**:
- [2019] FairFace_ Face Attribute Dataset for Balanced Race, Gender, and Age


## IMBD-WIKI
---
目前最大的人脸年龄数据集. 数据集规模: IMDB 上 20284 个名人, 共 460723 张图像; WIKI 上 62328 张图像. 给了年龄和性别标签, 但性别标签噪声比较大.

**References**:
- https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/

    
## FG-Net
---
FGNet dataset is a face aging dataset, with 1002 images from 82 identities. Each identity has multiple face images at different ages (ranging from 0 to 69).

**References**:
- http://www-prima.inrialpes.fr/FGnet/html/benchmarks.html
- http://www.fgnet.rsunit.com/
- http://yanweifu.github.io/FG_NET_data/FGNET.zip


## UTKFace
---
UTKFace dataset is a large-scale face dataset with long age span (range from 0 to 116 years old). The dataset consists of over 20,000 face images with annotations of age, gender, and ethnicity. 

**References**:
- https://susanqq.github.io/UTKFace/
- [2017 CVPR] Age Progression/Regression by Conditional Adversarial Autoencoder


## AFAD, Asian Face Age Dataset
---
The Asian Face Age Dataset (AFAD) is a new dataset proposed for evaluating the performance of age estimation, which contains more than 160K facial images and the corresponding age and gender labels. This dataset is oriented to age estimation on Asian faces, so all the facial images are for Asian faces. It is noted that the AFAD is the biggest dataset for age estimation to date.

**References**:
- https://github.com/afad-dataset/tarball


## ICCV2015 Looking at People Challenge - Track 1 Apparent Age Estimation
---
**References**:
- [2015 ICCV] Chalearn looking at people 2015_ Apparent age and cultural event recognition datasets and results


## AgeDB, Age Database
---
**References**:
- [2017 CVPRW] Agedb: The first manually collected in-the-wild age database


## AAF, All-Age-Faces
---
The All-Age-Faces (AAF) Dataset contains 13'322 face images (mostly Asian) distributed across all ages (from 2 to 80), including 7381 females and 5941 males.

**References**:
- https://github.com/JingchunCheng/All-Age-Faces-Dataset
- [2019] Exploiting effective facial patches for robust gender recognition

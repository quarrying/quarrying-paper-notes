# 2D Natural

## WebFace260M, WebFace42M
---
- WebFace260M : 4M identities / 260M faces
- WebFace42M:   2M identities / 42M faces

> Face number of WebFace42M in each identity varies from 3 to more than 300, and the average face number is 21 per identity.

**References**:
- [2021 CVPR] WebFace260M: A Benchmark Unveiling the Power of Million-Scale Deep Face Recognition
- https://www.face-benchmark.org/index.html


## Glint360K
---
> Furthermore, we clean Celeb-500k and add more celebrities to merge into a new training set, which we call Glint360K. The released dataset contains 18 million images of 360K individuals, which is the largest and cleanest training set by far in academia.

**References**:
- [2020] Partial FC_ Training 10 Million Identities on a Single Machine
- https://github.com/deepinsight/insightface/tree/master/recognition/partial_fc#glint360k


## Celeb-500k / Celeb-500K-2R
---
> In this paper, we propose a large training dataset named Celeb-500K for face recognition, which contains 50M images from 500K persons. To better facilitate academic research, we clean Celeb-500K to obtain Celeb-500K-2R, which contains 25M aligned face images from 365K persons. Based on the developed dataset, we achieve state-of-the-art face recognition performance and reveal two important observations on face recognition study. First, metric learning methods have limited performance gain when the training dataset contains a large number of identities. Second, in order to develop an efficient training dataset, the number of identities is more important than the average image number of each identity from the perspective of face recognition performance. Extensive experimental results show the superiority of Celeb-500K and provide a strong support to the two observations.

**Remarks**: 该数据集只提供下载链接, 另外该数据集比较脏.

**References**:
- https://github.com/JiajiongCao/CELEB-500K
- [2018 ICIP] Celeb-500K_ A Large Training Dataset for Face Recognition
- [CELEB-500K数据](https://github.com/deepinsight/insightface/issues/482)


## RFW, Racial Faces in-the-Wild
---
**References**:
- http://whdeng.cn/RFW/index.html
- [2019 ICCV] Racial Faces in the Wild_ Reducing Racial Bias by Information Maximization Adaptation Network


## LFW, Labeled Faces in the Wild
---
LFW 系 Labeled Faces in the Wild 的简称. 常用于 1:1 比对测试.

Though LFW contains 5749 people, only 85 have more than 15 images, and 4069 people have only one image.
remove all the subjects who have only a single image, leaving 1507 subjects with 2 or more images.
The number of images varies from 1 to 530 for one subject.

LFW dataset contains 13,233 web-collected images from 5749 different identities, with large variations in pose, expression and illuminations.

The LFW dataset consists of 13,323 web photos of 5,749 celebrities which are divided into 6,000 face pairs in 10 splits. Performance is measured by mean recognition ac- curacy using A) the restricted protocol, in which only same and not same labels are available in training; B) the unrestricted protocol, where additional training pairs are acces- sible in training; and C) an unsupervised setting in which no training whatsoever is performed on LFW images.

The only constraint on these images is that faces could be detected by the Viola-Jones face detector.
These images exhibit limited variations in pose, illumination, and expression, since only faces that could be detected by the Viola-Jones face detector were included in the dataset.


**References**:
- http://vis-www.cs.umass.edu/lfw/
- [LFW leaderboard](http://vis-www.cs.umass.edu/lfw/results.html)
- [2007] Labeled faces in the wild: A database for studying face recognition in unconstrained environments
- [2014] Labeled faces in the wild: Updates and newreporting procedures
- [2008] Labeled faces in the wild: A database for studying face recognition in unconstrained environments


### Standard LFW protocol
According to the standard LFW protocol, the performance measurement should be the mean accuracy over 10-fold face verification task with each fold containing 300 inter-class and 300 intra-class face pairs.

The LFW protocol consists of face verification based on ten-fold cross-validation, each fold containing 300 “‘same face” and 300 “not-same face” image pairs.


### Best-Rowden protocol
是利用 LFW 构造的 1:N 测试集.

> For the probe-gallery identification testing, there are two new protocols called the close set and open set identification tasks. 1) For the close set task, the gallery contains 4,249 identities, each with only a single face image, and the probe set contains 3,143 face images belonging to the same set of identities. The performance is measured by Rank-1 identification accuracy. 2) For the open set task, the gallery set includes 3,143 images of 596 identities. The probe set includes 10,090 images which are constructed by 596 genuine probes and 9,494 impostor ones. The accuracy is evaluated by the Rank-1 Detection and Identification Rate (DIR), which is genuine probes matched in Rank-1 at a 1% False Alarm Rate (FAR) of impostor ones that are not rejected.

**References**:
- [2014 TIFS] Unconstrained face recognition: Identifying a person of interest from a media collection


### BLUFR protocol
> The Benchmark of Large-scale Unconstrained Face Recognition (BLUFR) is a new benchmark for LFW evaluations, which contains both verification and open- set identification. There are 10-fold experiments, with each fold containing about 156,915 genuine matching and 46,960,863 impostor matching on average for performance evaluation. It is more challenging and generalized for LFW.

**References**:
- [2014 IJCB] A benchmark study of large-scale unconstrained face recognition


### 衍生数据集之 CPLFW
**References**:
- [2018] Cross-pose lfw_ A database for studying cross-pose face recognition in unconstrained environments
- http://whdeng.cn/CPLFW


### 衍生数据集之 CALFW
**References**:
- [2017] Cross-age lfw_ A database for studying cross-age face recognition in unconstrained environments
- http://whdeng.cn/CALFW


### 衍生数据集之 SLLFW
**References**:
- http://whdeng.cn/SLLFW/
- [2017] Fine-grained face verification: FGLFW database, baselines, and human-DCMN partnership
- [2016 ICB] Fine-grained LFW database

### 衍生数据集之 LFWA
LFWA is another unconstrained face attributes database with face images from the LFW database (13, 233 images of 5, 749 subjects), and the same 40 attribute annotations as in the CelebA database.

**References**:
- [2015 ICCV] Deep learning face attributes in the wild


## IJB, IARPA Janus Benchmark

### IJB-A Dataset

IJB-A IARPA Janus Benchmark-A (IJB-A) contains 500 subjects with a total of 25, 813 images (5, 399 still images and 20, 414 video frames). 

The IJB-A dataset was released in 2015 in an attempt to push the frontiers of unconstrained face recognition. Given that recognition performance on the LFW dataset has saturated under the standard protocol, the IJB-A dataset contains more challenging face images and specifies both verification and identification (open and close sets) protocols.

Some key features of the IJB-A dataset include: full pose variation, a mix of images and videos, and a wider demographic variation of subjects than is available in the LFW dataset. The dataset was developed using 1,501,267 crowd sourced annotations.

**JANUS Challenge Set 2 (JANUS CS2)**
The IJB-A dataset includes real-world unconstrained faces of 500 subjects with significant pose and illumination variations which are much harder than the Labeled Faces in the Wild (LFW) and Youtube Face (YTF) datasets. JANUS CS2 is the extended version of IJB-A which contains not only all the images/frames of IJB-A but also includes the original videos for evaluating the video-based face verification system. 
The dataset includes 25,800 images of 500 subjects.

**Janus Challenge Set 3 (Janus CS3)**
the extended version of IJB-A, Janus Challenge Set 3 (Janus CS3), which is a superset of IJB-A and is much more challenging. Janus CS3 contains 1,871 subjects with 11,876 still images and 55,372 video frames sampled from 7,094 videos.

**References**:
- https://www.nist.gov/itl/iad/image-group/ijba-dataset-request-form
- [2015 CVPR] Pushing the frontiers of unconstrained face detection and recognition: Iarpa janus benchmark


### IJB-B
IARPA Janus Benchmark-B (IJB-B) dataset consists of 1,845 subjects with a total of 76,824 images (21,798 still images and 55,026 video frames from 7,011 videos), an average of 41 images per subject. Images in this dataset are labeled with ground truth bounding boxes and other covariate meta-data such as occlusions, facial hair and skin tone.

**References**:
- [2017 CVPRW] Iarpa janus benchmark-b face dataset
    
    
### IJB-C


## Face-Disguise-Dataset
---
> The dataset contains 4000 images (2000 images each corresponding to simple and complex backgrounds dataset) recorded with male and female subjects aged from 18 years to 30 years. The dataset was collected in 8 different backgrounds,25 subjects and 10 different disguises.

**References**:
- https://github.com/DevendraPatil/Face-Disguise-Dataset
- [2017 ICCVW] Disguised Face Identification (DFI) with Facial KeyPoints using Spatial Fusion Convolutional Network


## DFW, Disguised Faces in the Wild
---
**References**:
- [2018 CVPR] Disguised Faces in the Wild
- http://iab-rubric.org/DFW/index.html


## UHDB31
---
**References**:
- [2017 ICCVW] UHDB31: A dataset for better understanding face recognition across pose and illumination variation


## Trillion Pairs
---
**References**:
- http://trillionpairs.deepglint.com/overview


## LFR 2019
---
**References**:
- https://ibug.doc.ic.ac.uk/resources/lightweight-face-recognition-challenge-workshop/


## VGGFace
---
该数据集可以用于训练. 由于版权问题, 官方只提供了图像的下载链接. 有 2622 人, 共 260 万张图像, 平均每人 1000 张.

> The dataset consists of the crawled images of celebrities on the Web. There are 2622 celebrities in the dataset and the dataset is designed to have no overlap with the popular face recognition benchmarks such as Labeled Faces in the Wild (LFW), YouTube Faces Dataset and IARPA Janus Benchmark A (IJB-A).

VGG-Face dataset which has about 2.6 million images of 2,622 subjects (about 1000 images per subject). 

**References**:
- [2015 BMVC] Deep Face Recognition


## VGGFace2
---
> The dataset contains 3.31 million images of 9131 subjects, with an average of 362.6 images for each subject. Images are downloaded from Google Image Search and have large variations in pose, age, illumination, ethnicity and profession (e.g. actors, athletes, politicians). The dataset is approximately gender-balanced, with 59.7% males, varying between 87 and 843 images for each identity, with 362.6 images on average. 

**References**:
- [2017] VGGFace2_ A dataset for recognising faces across pose and age


## CASIA WebFace
---
After being cleaned, CASIA-WebFace finally has 10,575 subjects and 494,414 face images. Because the scale of dataset is too large, we can’t promise all faces are detected and annotated correctly. A small amount of miss classified samples don’t affect the training process and may be able to improve the robustness of the model.

CASIA WebFace consists of 494,414 images of 10,575 subjects and it is widely used to train DNNs. In the original dataset, there are some annotation errors. A corrected version of CASIA Webface was later released, which has 455,594 images of 10,575 subjects.

The CASIA-WebFace dataset contains 494,414 face images of 10,575 subjects, with 46 face images per subject on average. 

There are 22 overlapping subjects between the CASIA WebFace and IJB-A datasets.

该数据集中有一些标注错误. CASIA-WebFace 与 LFW 和 YTF 中的人没有重叠, 常用做训练集. 官方提供的原始图像的尺寸好像是 250x250.

**References**:
- http://www.cbsr.ia.ac.cn/english/CASIA-WebFace-Database.html
- [2014] Learning face representation from scratch


## MS-Celeb-1M, MS1M
---
从 1M 个名人中, 根据受欢迎程度选择 100K 个. 然后利用搜索引擎, 给 100K 个人, 每人搜大概 100 张图片. 共 `100K*100=10M` 张图片. 测试集包括 1000 个名人, 这 1000 个名人来自于 1M 个明星中随机挑选, 而且经过微软标注, 每个名人大概有 20 张图片. 

该数据集的噪声比较大. According to `[2018 ECCV] The devil of face recognition is in the noise`, there are more than 50% noises in MS1M.

**References**:
- http://www.msceleb.org/
- https://megapixels.cc/msceleb/
- https://www.microsoft.com/en-us/research/project/ms-celeb-1m-challenge-recognizing-one-million-celebrities-real-world/
- [2016] MS-Celeb-1M: A Dataset and Benchmark for Large-Scale Face Recognition


### MS1M-IBUG
---
85K ids/3.8M images

**References**:
- https://pan.baidu.com/s/1nxmSCch

### MS1M-ArcFace (推荐采用)
---
85K ids/5.8M images

**References**:
- https://pan.baidu.com/s/1S6LJZGdqcZRle1vlcMzHOQ

### MS1MV2
---
**References**:
- [2019 CVPR] Arcface_ Additive angular margin loss for deep face recognition.


## MegaFace
---
It is a very challenging dataset and aims to evaluate the performance of face recognition algorithms at the million scale of distractors (people who are not in the testing set). MegaFace datasets include gallery set and probe set. The gallery set consists of more than 1 million images from 690K different individuals, as a subset of Flickr photos from Yahoo. The probe set using in this challenge are two existing databases: Facescrub and FGNet. 

**References**:
- http://megaface.cs.washington.edu/
- [2016 CVPR] The MegaFace Benchmark: 1 Million Faces for Recognition at Scale


### MF2 Training Dataset
---
The MF2 training dataset is the largest (in number of identities) publicly available facial recognition dataset with a 4.7 million faces, 672K identities, and their respective bounding boxes. All images obtained from Flickr (Yahoo's dataset) and licensed under Creative Commons.

**References**:
- [2017]  Level Playing Field for Million Scale Face Recognition
- http://megaface.cs.washington.edu/dataset/download_training.html


## NIST FRVT, NIST Face Recognition Vendor Tests
---
FRVT 系 Face Recognition Vendor Test 的简称.

Of particular note is the Face Recognition Vendor Tests (FRVT) , which were a set of independent evaluations of commercially available and prototype face recognition technologies conducted by the US government in the years 2000, 2002 and 2006. The FRVT is considered to be a very important milestone in face recognition evaluations; it also includes three previous face recognition evaluations – the FERET evaluations of 1994, 1995 and 1996. 

### Ongoing FRVT Activities
---
- FRVT: FACE MASK EFFECTS
- FRVT: DEMOGRAPHIC EFFECTS
- FRVT 1:1 VERIFICATION
- FRVT 1:N 2018
- FRVT MORPH
- FRVT QUALITY

**References**:
- https://www.nist.gov/programs-projects/face-recognition-vendor-test-frvt
- https://www.nist.gov/programs-projects/face-recognition-vendor-test-frvt-ongoing
- https://github.com/usnistgov/frvt


## IMDb-Face
---
IMDb-Face is a new large-scale noise-controlled dataset for face recognition research. The dataset contains about 1.7 million faces, 59k identities, which is manually cleaned from 2.0 million raw images. All images are obtained from the IMDb website. 

**References**:
- [2018 ECCV] The Devil of Face Recognition is in the Noise
- https://github.com/fwang91/IMDb-Face


## DiF, Diversity in Faces
---
**References**:
- https://www.research.ibm.com/artificial-intelligence/trusted-ai/diversity-in-faces/


## Public-IvS
---
An IvS test dataset from BaiduBaike and official pages, containing 1,262 identities and 5,503 images. 

**References**:
- [2018] Large-scale Bisample Learning on ID versus Spot Face Recognition
- http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/LBL/main.htm


## UMDFaces
---
- UMDFaces is a face dataset divided into two parts: 
    - Still Images: 367,888 face annotations for 8,277 subjects.
    - Video Frames: Over 3.7 million annotated video frames from over 22,000 videos of 3100 subjects.

**References**:
- [2016] Umdfaces_ An annotated face dataset for training deep networks
- [2017] The do's and don'ts for cnn-based face verification
- https://www.umdfaces.io/


## CelebFaces+
---
The CelebFaces+ dataset was released In 2014, with 202,599 images of 10,177 celebrities.

**References**:
- [2014 CVPR] Deep learning face representation from predicting 10,000 classes
- [2014 CVPR] Deep learning face representation by joint identification-verification


## MSRA-CFW
---
> In this paper, we present a face annotation system to automatically collect and label celebrity faces from the web. With the proposed system, we have constructed a large-scale dataset called “Celebrities on the Web,” which contains 2.45 million distinct images of 421436 celebrities and is orders of magnitude larger than previous datasets. 

**References**:
- https://www.microsoft.com/en-us/research/project/msra-cfw-data-set-of-celebrity-faces-on-the-web/
- [2012 TMM] Finding celebrities in billions of web images


## PaSC, Point and Shoot Challenge
---
> The PaSC dataset is a collection of videos acquired at the University of Notre Dame over seven weeks in the Spring semester of 2011. The human subjects in each video clip performed different pre-determined action each week. The actions were captured using two cameras (handeld and tripod mounted) simultaneously. The handheld videos were acquired with five different cameras, while tripod mounted videos were shot with the same camera. The dataset contains 1,401 videos from handheld cameras and 1,401 videos from the tripod mounted camera. A small training set of 280 videos is also available with the dataset.

**References**:
- [2016 BTAS] Report on the BTAS 2016 Video Person Recognition Evaluation


## YTF, YouTube Faces Database
---
YTF dataset consists of 3,425 videos of 1,595 different people, with an average of 2.15 videos per person. The clip durations vary from 48 frames to 6,070 frames, with an average length of 181.3 frames.

These videos are divided into 5,000 video pairs and 10 splits and used to evaluate the video-level face verification.

It contains 3,425 videos of 1,595 people collected from YouTube, with an average of 2 videos per identity, and is a standard benchmark for face verification in video.

**References**:
- http://www.cs.tau.ac.il/~wolf/ytfaces/
- [2011 CVPR] Face Recognition in Unconstrained Videos with Matched Background Similarity

    
## CACD, Cross-Age Celebrity Dataset 或称 CACD 2000
---
CACD is built for studying cross-age face recognition, but only 10% of the subjects in CACD are manually annotated.

CACD is a large dataset collected for cross-age face recognition in 2014, which include 2,000 subjects and 163,446 images. The scale of CACD is large enough to train deep models but the dataset contains much noise and incorrect identity labels. The reason is that the images are crawled by Google Image search engine, and just a small subset (200 subjects) is checked by manual.

**References**:
- [2014 ECCV] Cross-age reference coding for ageinvariant face recognition and retrieval
- [2015 TMM] Face recognition and retrieval using cross-age reference coding with cross-age celebrity dataset
- http://bcsiriuschen.github.io/CARC/


## CFP, Celebrities in Frontal Profile
---
CFP dataset consists of 500 subjects, each with 10 frontal and 4 profile images. The evaluation protocol includes frontal-frontal (FF) and frontal-profile (FP) face verification, each having 10 folders with 350 sameperson pairs and 350 different-person pairs.

**References**:
- [2016 WACV] Frontal to profile face verification in the wild

    
## CMU Multi-PIE
---
The CMU Multi-PIE database contains more than 750000 images with variations in pose, illumination and expression of 337 people. Each subject depicts various facial expressions (Smile, surprise, squint, disgust and scream), and 15 poses under 19 illuminations

**References**:
- [2010] Multi-pie

    
## FaceScrub
---
All the identities in the FaceScrub dataset are celebrities.

It comprises a total of 106,863 face images of male and female 530 celebrities, with about 200 images per person. The original release of FaceScrub contained slightly more face images (107,818) but included a number of duplicates as well as a few mislabeled and morphed faces. These have been removed from the database with effect from 9-Mar-2016.

Facescrub dataset is publicly available dataset, containing 100K photos of 530 unique individuals (55,742 images of males and 52,076 images of females).

**References**:
- http://vintage.winklerbros.net/facescrub.html
- [2014 ICIP] A data-driven approach to cleaning large face datasets

    
## FG-NET
---
FGNet dataset is a face aging dataset, with 1002 images from 82 identities. Each identity has multiple face images at different ages (ranging from 0 to 69)

**References**:
- http://www-prima.inrialpes.fr/FGnet/html/benchmarks.html


## FERET, The Face Recognition Technology
---
ColorFeret consists of 14.1k images of 1.2k different individuals with different poses under controlled conditions. The dataset includes a variety of face poses, facial expressions, and lighting conditions. Each images contains labels of the individual’s gender, ethnicity, head pose, age, glasses, and beard. In total, ColorFeret provides around 183k soft-biometric labels.

**References**: 
- http://www.itl.nist.gov/iad/humanid/feret/
- [2000 TPAMI] The feret evaluation methodology for face-recognition algorithms


## FRGC, Face Recognition Grand Challenge
---
**References**:
- http://face.nist.gov/frgc/
- [2005 CVPR] Overview of the face recognition grand challenge


## Caltech 10,000 Web Faces
---
**References**:
- http://www.vision.caltech.edu/Image_Datasets/Caltech_10K_WebFaces/


## CAS-PEAL, CAS-PEAL-R1
---
**References**:
- http://www.jdl.ac.cn/peal/index.html
- [2008] The cas-peal large-scale chinese face database and baseline evaluations


## WDRef, Wide and Deep Reference dataset
---
The WDRef database contains 99,773 images of 2,995 subjects. Over 2,000 subjects have more than 15 images. They are collected from the Internet with large variations in pose, expression and lighting.

**References**:
- Bayesian Face Revisited_ A Joint Formulation
- Broken!: http://home.ustc.edu.cn/~chendong/JointBayesian/
- https://stackoverflow.com/questions/29648555/where-to-find-wdref-dataset


## PubFig, Public Figures Face Database
---
The PubFig database is a large, real-world face dataset consisting of 58,797 images of 200 people collected from the internet.

**References**:
- http://www.cs.columbia.edu/CAVE/databases/pubfig/
- [2009 ICCV] Attribute and Simile Classifiers for Face Verification


## PubFig83
---
This is a downloadable dataset of 8300 cropped facial images, made up of 100 images for each of 83 public figures. It was derived from the list of URLs compiled by Neeraj Kumar et al and has been screened to remove near-duplicate images. It can be used as a proxy for the problem of recognizing identities from near-frontal faces in personal photo collections.

**References**:
- http://vision.seas.harvard.edu/pubfig83/
- [2011 CVPR] Scaling Up Biologically-Inspired Computer Vision: A Case Study in Unconstrained Face Recognition on Facebook


## AR Face Database
---
The AR database contains more than 4000 frontal images of 126 subjects with variation in expressions, illuminations and occlusions.

**References**:
- http://www2.ece.ohio-state.edu/~aleix/ARdatabase.html
- [1998] The ar face database

    
## The ORL Database of Faces, AT&T The Database of Faces
---
ORL 全称 Olivetti Research Laboratory.

There are ten different images of each of 40 distinct subjects. For some subjects, the images were taken at different times, varying the lighting, facial expressions (open / closed eyes, smiling / not smiling) and facial details (glasses / no glasses). All the images were taken against a dark homogeneous background with the subjects in an upright, frontal position (with tolerance for some side movement).

The files are in PGM format, and can conveniently be viewed on UNIX (TM) systems using the 'xv' program. The size of each image is 92x112 pixels, with 256 grey levels per pixel. The images are organised in 40 directories (one for each subject), which have names of the form sX, where X indicates the subject number (between 1 and 40). In each of these directories, there are ten different images of that subject, which have names of the form Y.pgm, where Y is the image number for that subject (between 1 and 10).

**References**:
- [1994] Parameterisation of a stochastic model for human face identification
- http://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html
- http://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html


## Yale Face Database
---
The Yale Face Database (size 6.4MB) contains 165 grayscale images in GIF format of 15 individuals. There are 11 images per subject, one per different facial expression or configuration: center-light, w/glasses, happy, left-light, w/no glasses, normal, right-light, sad, sleepy, surprised, and wink.


## Yale Face Database B
---
Yale Face Database B contains 5760 single light source images of 10 subjects each seen under 576 viewing conditions (9 poses x 64 illumination conditions).  For every subject in a particular pose, an image with ambient (background) illumination was also captured. Hence, the total number of images is in fact 5760+90=5850. The total size of the compressed database is about 1GB.

The extended Yale Face Database B contains 16128 images of 28 human subjects under 9 poses and 64 illumination conditions. 

**References**:
- http://vision.ucsd.edu/~leekc/ExtYaleDatabase/ExtYaleB.html
- [2005 TPAMI] Acquiring linear subspaces for face recognition under variable lighting
- http://vision.ucsd.edu/content/yale-face-database
- http://vision.ucsd.edu/~leekc/ExtYaleDatabase/ExtYaleB.html
- http://cvc.yale.edu/projects/yalefacesB/yalefacesB.html

    
# Infrared Face Datasets

## CASIA NIR / CASIA NIR-VIS2.0
---
**References**:
- http://vcipl-okstate.org/pbvs/bench/Data/07/download.html

## PolyU NIR
---
**References**:
- http://www4.comp.polyu.edu.hk/~biometrics/polyudb_face.htm

## IIT Delhi NIR, IIT Delhi Near IR Face Database (Version 2.0)
---
**References**:
- http://www4.comp.polyu.edu.hk/~csajaykr/IITD/FaceIR.htm

## LAMP-HQ
---
**References**:
- [2019] LAMP-HQ: A Large-Scale Multi-Pose High-Quality Database for NIR-VIS Face Recognition


# Multi-modal Face Datasets

## Tufts Face Database
---
Tufts Face Database is the most comprehensive, large-scale face dataset that contains 7 image modalities: visible, near-infrared, thermal, computerised sketch, LYTRO, recorded video, and 3D images. 

Size: The dataset contains over 10,000 images, where 74 females and 38 males from more than 15 countries with an age range between 4 to 70 years old are included. 

Projects: This database will be available to researchers worldwide in order to benchmark facial recognition algorithms for sketches, thermal, NIR, 3D face recognition and heterogamous face recognition.

**References**:
- https://www.kaggle.com/kpvisionlab/tufts-face-database


# Hyperspectral Face Datasets

## The Hong Kong Polytechnic University Hyperspectral Face Database (PolyU-HSFD)
---
**References**:
- http://www4.comp.polyu.edu.hk/~biometrics/hsi/hyper_face.htm


# Surveillance Scene Face Datasets

## QMUL-SurvFace
---
Surveillance Face Recognition Challenge

**References**:
- [2018] Surveillance Face Recognition Challenge
- https://qmul-survface.github.io/benchmark.html

    
## SCface
---
**References**:
- [2011] SCface_ surveillance cameras face database
- http://www.scface.org/


## UCCS, UnConstrained College Students
---
**References**:
- [2017 IJCB] Unconstrained Face Detection and Open-Set Face Recognition Challenge
- http://vast.uccs.edu/Opensetface/



# 3D Face Datasets

## Lock3DFace
---
**References**:
- http://irip.buaa.edu.cn/lock3dface/index.html
- [2019 CVPR] Led3D_ A Lightweight and Efficient Deep Approach to Recognizing Low-quality 3D Faces
- [2016 ICB] Lock3DFace_ A Large-Scale Database of Low-Cost Kinect 3D Faces

## IAS-Lab RGB-D Face Dataset
---
**References**:
- http://robotics.dei.unipd.it/reid/index.php/8-dataset/9-overview-face


## Bosphorus
---
**References**:
- [2008] Bosphorus database for 3D face analysis


## BU-3DFE
---
**References**:
- [2006] A 3D facial expression database for facial behavior research
- [2008] A high-resolution 3d dynamic facial expression database


## 3D-TEC (twins)
---
**References**:
- [2011 IJCB] Twins 3D face recognition challenge


## FRGCv2
---
FRGCv2 by far still remains the largest 3D face recognition benchmark dataset with 446 identities.

**References**:
- [2005 CVPR] Overview of the face recognition grand challenge


## ND-2006
---
ND-2006 (a superset of FRGCv2) has only 13,540 scans of 888 unique identities and took over two years to collect.

**References**:
- [2007] Using a multi-instance enrollment representation to improve 3D face recognition


## GavabDB
---
The GavabDB database contains 427 scans, with seven scans per ID, three
neutral and four expressions. The expressions in this dataset
vary considerably, including sticking out the tongue and
strong facial distortions. Additionally it has strong artifacts
due to facial hair, motion and the bad scanner quality. This
dataset is typical for a non-cooperative environment.

**References**:
- [2004] Gavabdb_ a 3D face database


## Texes FRD
---
**References**:
- [2010 IJCV] Anthropometric 3D face recognition


## CASIA 3D
---
The Casia 3D database contains 4,624 scans of 123 subjects. Each subject was captured with different expressions and poses.

**References**:
- [2006 ECCV] Learning effective intrinsic features to boost 3D-based face recognition


## UMB-DB
---
**References**:
- [2011 ICCVW] UMB-DB_ A database of partially occluded 3D faces


## USF Human ID 3D
---
**References**:
- [1999] A morphable model for the synthesis of 3D faces


## UND
---
The UND database was used in the face recognition grand challenge and consists of 953 scans, with one to eight scans
per ID. It is of better quality and contains only slight expression variations. It represents a cooperative scenari

**References**:
- [2005] An evaluation of multimodal 2D+3D face biometrics


## Florence 2D/3D hybrid face dataset (MICC)
---
**References**:
- [2011] The Florence 2D/3D Hybrid Face Dataset


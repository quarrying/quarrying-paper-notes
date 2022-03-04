## MAAD-Face
---
MAAD-Face is build on the VGGFace2 database and thus, consists of **3.3M faces of over 9k individuals**. Using a novel annotation transfer-pipeline that allows an accurate label-transfer from multiple source-datasets to a target-dataset, MAAD-Face consists of 123.9M attribute annotations of 47 different binary attributes. Consequently, it provides 15 and 137 times more attribute labels than CelebA and LFW.

**References**:
- [202012] MAAD-Face_ A Massively Annotated Attribute Dataset for Face Images
- https://github.com/pterhoer/MAAD-Face


## CelebA, CelebFaces Attributes
---
CelebA 系 CelebFaces Attributes 的简称. CelebA 包含 200K 张图像, 40 个属性. CelebA 和 LFW 之间没有身份重叠.

CelebFaces Attributes Dataset (CelebA) is a large-scale face attributes dataset with more than 200K celebrity images, each with 40 attribute annotations.

**References**:
- http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html
- [2015 ICCV] Deep Learning Face Attributes in the Wild


## LFWA, LFW Attributes
---
LFWA is another unconstrained face attributes database with face images from the LFW database (13,233 images of 5,749 subjects), and the same 40 attribute annotations as in the CelebA database.

**References**:
- [2015 ICCV] Deep Learning Face Attributes in the Wild


## Adience
---
Adience 数据集来源为 Flickr 相册, 由用户使用 iPhone 或者其它智能手机设备拍摄. 该数据集主要用于进行年龄和性别的未经过滤的面孔估计. 同时里面还进行了相应的 landmark 的标注, 其中包含 2284 个类别和 26580 张图片. 年龄标签是年龄段, 为 (0-2, 4-6, 8-13, 15-20, 25-32, 38-43, 48-53, 60+). 

**References**:
- http://www.openu.ac.il/home/hassner/Adience/data.html


## UMDFaces
---
UMDFaces is a face dataset divided into two parts: 
- Still Images: 367,888 face annotations for 8,277 subjects.
- Video Frames: Over 3.7 million annotated video frames from over 22,000 videos of 3100 subjects.

**References**:
- http://www.umdfaces.io/
- [2017] The do’s and don’ts for cnn-based face verification
- [2016] Umdfaces: An annotated face dataset for training deep networks

    
## USTC CoarseData / FineData
---
This dataset contains [CoarseData](https://drive.google.com/open?id=0B0A9UsiwtVTHY0p4em5qUzRISW8) and [FineData](https://drive.google.com/open?id=0B6B08IBRi1PFbzhJeF9vNmVrUjA) augmented from 3131 images of [300-W](https://ibug.doc.ic.ac.uk/resources/300-W/) with the method described in the paper [3DFaceNet: Real-time Dense Face Reconstruction via Synthesizing Photo-realistic Face Images](https://arxiv.org/abs/1708.00980). CoarseData is constructed by varying poses and expressions of the original images. FineData is constructed by transferring details from other images to the original images. We augment each image 30 times for both CoarseData and FineData.

**References**:
- https://github.com/Juyong/3DFace
    

## MTFL, Multi-Task Facial Landmark
---
Multi-Task Facial Landmark (MTFL) dataset contains annotations of five facial landmarks and attributes of gender, head pose, etc. Consisting of 10,000 outdoor face images from the web. Each image is annotated with bounding box and five landmarks, i.e. centers of the eyes, nose, corners of the mouth.

**References**:
- [2013 CVPR] Deep Convolutional Network Cascade for Facial Point Detection
- [2014 ECCV] Facial landmark detection by deep multi-task learning
- http://mmlab.ie.cuhk.edu.hk/projects/TCDCN/data/MTFL.zip


## CEW, Closed Eyes In The Wild
---
Eye closeness detection is a challenging task in the unconstrained real-world application scenario which is full of challenging variations caused by individual difference and kinds of environment changes including lighting, blur, occlusion, and disguise. To investigate the performance of eye closeness detection in these conditions, we collected a dataset for eye closeness detection in the Wild. In particular, this dataset contains 2423 subjects, among which 1192 subjects with both eyes closed are collected directly from Internet, and 1231 subjects with eyes open are selected from the Labeled Face in the Wild database. 

**References**:
- http://parnec.nuaa.edu.cn/xtan/data/ClosedEyeDatabases.html
- [2014 PR] Eyes Closeness Detection from Still Images with Multi-scale Histograms of Principal Oriented Gradients

    
## YawDD
---
**References**:
- [2014] YawDD_ A Yawning Detection Dataset
    
    
## HUST-LEBW
---
**References**:
- [2019] Towards Real-time Eyeblink Detection in The Wild: Dataset, Theory and Practices


# Face Demographic Attribute
---

## FairFace
---
containing 108,501 images, with an emphasis of balanced race composition in the dataset. We define 7 race groups: White, Black, Indian, East Asian, Southeast Asian, Middle East, and Latino. Images were collected from the **YFCC-100M Flickr** dataset and labeled with race, gender, and age groups. 

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


# Face Expression Attribute
----

# Datasets & Challenges

## Google Facial Expression Comparison Dataset
---
This dataset by Google is a large-scale facial expression dataset that consists of face image triplets along with human annotations that specify, which two faces in each triplet form the most similar pair in terms of facial expression. 

Size: The size of the dataset is 200MB, which includes 500K triplets and 156K face images.

Projects: The dataset is intended to aid researchers working on topics related to facial expression analysis such as expression-based image retrieval, expression-based photo album summarisation, emotion classification, expression synthesis, etc.

**References**:
- https://research.google/tools/datasets/google-facial-expression/
  

## RAF-DB, Real-world Affective Faces Database
---
Real-world Affective Faces Database (RAF-DB) is a large-scale facial expression database with around 30K great-diverse facial images downloaded from the Internet. Based on the crowdsourcing annotation, each image has been independently labeled by about 40 annotators. Images in this database are of great variability in subjects' age, gender and ethnicity, head poses, lighting conditions, occlusions, (e.g. glasses, facial hair or self-occlusion), post-processing operations (e.g. various filters and special effects), etc.

**References**:
- http://www.whdeng.cn/raf/model1.html
- [2017 CVPR] Reliable Crowdsourcing and Deep Locality-Preserving Learning for Expression Recognition in the Wild
- [2019 TIP] Reliable Crowdsourcing and Deep Locality-Preserving Learning for Unconstrained Facial Expression Recognition

    
## RAF-ML, Real-world Affective Faces Multi Label
---
**References**:
- http://whdeng.cn/RAF/model2.html
- [2019 IJCV] Blended Emotion in-the-Wild: Multi-label Facial Expression Recognition Using Crowdsourced Annotations and Deep Locality Feature Learning

    
## BNU-LSVED, BNU Large-scale Spontaneous Visual Expression Database
---
**References**:
- [2016] BNU-LSVED: a multimodal spontaneous expression database in educational environment


## FERPlus
---


## AffectNet
---


## FER 2013
---
The Facial Expression Recognition 2013 (FER-2013) database was introduced in the ICML 2013 Challenges in Representation Learning. The database was created using the Google image search API and faces have been automatically registered. Faces are labeled as any of the six basic expressions as well as the neutral. The resulting database contains 35,887 images most of them in wild settings.

the FER2013 database (one of the largest recently released FER databases) contains 35,887 images of different subjects yet only 547 of the images portray disgust.

The FER 2013 challenge was created using Google image search API with 184 emotion related keywords, like blissful, enraged. Keywords were combined with phrases for gender, age and ethnicity in order to obtain up to 600 different search queries. Image data was collected for the first 1000 images for each query. Collected images were passed through post-processing, that involved face region cropping and image alignment. Images were then grouped into the corresponding fine-grained emotion classes, rejecting wrongfully labeled frames and adjusting cropped regions. The resulting data contains nearly 36,000 images, divided into 8 classes (7 effective expressions and a neutral class), with each emotion class containing a few thousand images (disgust being the exception with only 547 frames).

**References**:
- http://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge


## GENKI-4K
---
The GENKI-4K dataset contains 4,000 face images spanning a wide range of subjects, facial appearance, illumination, geographical locations, imaging conditions, and camera models. All images are labeled for both Smile content (1=smile, 0=non-smile) and Head Pose (yaw, pitch, and roll parameters, in radians).

Among these pictures, 2162 images are labeled as smile and 1838 im- ages are labeled as non-smile. 


## JAFFE, The Japanese Female Facial Expression Database
---
The database contains 213 images of 7 facial expressions (6 basic facial expressions + 1 neutral) posed by 10 Japanese female models. Each image has been rated on 6 emotion adjectives by 60 Japanese subjects. The database was planned and assembled by Michael Lyons, Miyuki Kamachi, and Jiro Gyoba. We thank Reiko Kubota for her help as a research assistant. The photos were taken at the Psychology Department in Kyushu University.

**References**:
- http://www.kasrl.org/jaffe.html
- http://www.kasrl.org/jaffeimages.zip

    
## CK, CK+, Cohn-Kanade AU-Coded Expression Database
---
The Extended Cohn-Kanade database (CK+) includes 593 video sequences recorded from 123 subjects ranging from 18 to 30 years old. Subjects displayed different expressions starting from the neutral for all sequences, and some sequences are labeled with basic expressions.

**References**:
- [2010 CVPRW] The extended cohn-kanade dataset (ck+): a complete dataset for action unit and emotion-specified expression
- http://www.consortium.ri.cmu.edu/ckagree/

    
## NovaEmotions
---
NovaEmotions, aim to represent facial expressions and emotional state as captured in a non-controlled environment. The data is collected in a crowd-sourcing manner, where subjects were put in front of a gaming device, which captured their response to scenes and challenges in the game itself. The game, in time, reacted to the player’s response as well. This allowed collecting spontaneous expressions from a large pool of variations. 
The NovaEmotions dataset consists of over 42,000 images taken from 40 different people. Majority of the participants were college students with ages ranges between 18 and 25. Data presents a variety of poses and illumination. 

**References**:
- [2013 ACMMM] Competitive affective gaming: Winning with a smile
- [2016 CVIU] Crowdsourcing facial expressions for affective-interaction

    
## EmotiW
---
EmotiW 2015; EmotiW 2016

**References**:
- [20015] Video and Image based Emotion Recognition Challenges in the Wild: EmotiW 2015


## AFEW / SFEW
---
Acted Facial Expressions In The Wild (AFEW) is a dynamic temporal facial expressions data corpus consisting of close to real world environment extracted from movies. Static Facial Expressions in the Wild (SFEW)  has been developed by selecting frames from AFEW. 

**References**:
- https://cs.anu.edu.au/few/AFEW.html

    
## MMI
---
**References**:
- http://mmifacedb.eu/ 
- http://ibug.doc.ic.ac.uk/research/mmi-database/


## USTC-NVIE
---
The Key Laboratory of Computing and Communication Software of Anhui Province(CCSL) has constructed the USTC-NVIE (Natural Visible and Infrared facial Expression) database under the sponsor of the 863 project. To date, most facial expression analysis has been based on visible and posed expression databases. Visible images, however, are easily affected by illumination variations, while posed expressions differ in appearance and timing from natural ones. We propose and establish a natural visible and infrared facial expression database, which contains both spontaneous and posed expressions of more than 100 subjects, recorded simultaneously by a visible and an infrared thermal camera, with illumination provided from three different directions. The posed database also includes expression image sequences with and without glasses.


## DISFA/DISFA+
---
**References**:
- http://mohammadmahoor.com/disfa/


## BP4D
---
**References**:
- http://www.cs.binghamton.edu/~lijun/Research/3DFE/3DFE_Analysis.html


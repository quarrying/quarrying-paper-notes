# 深度学习方法
---

## Sun et al. 
---
- [2013 CVPR] Deep convolutional network cascade for facial point detection
- https://github.com/mariolew/TF-FaceLandmarkDetection
- https://github.com/luoyetx/deep-landmark

## Zhou et al.
---
- [2013 ICCVW] Extensive facial landmark localization with coarse-to-fine convolutional network cascade

## TCDCN
---
- [2014 ECCV] Facial landmark detection by deep multi-task learning
- [2016 TPAMI] Learning Deep Representation for Face Alignment with Auxiliary Attributes
- https://github.com/flyingzhao/tfTCDCN

## CFAN
---
- [2014 ECCV] Coarse-to-fine autoencoder networks (CFAN) for real-time face alignment

## Liang et al
- [2015] Unconstrained facial landmark localization with backbone-branches fully-convolutional networks

## DAN
---
- [2017 CVPRW] Deep Alignment Network_ A convolutional neural network for robust face alignment

## FAN
---
- [2017 ICCV] How far are we from solving the 2D & 3D Face Alignment problem?
- https://github.com/1adrianb/face-alignment
- https://github.com/1adrianb/2D-and-3D-face-alignment

## Face++ Series
---
- [2013 @Face++] Extensive Facial Landmark Localization with Coarse-to-fine Convolutional Network Cascade
- [2015 @Face++] Coarse-to-fine Face Alignment with Multi-Scale Local Patch Regression
- [2016 @Face++] Approaching Human Level Facial Landmark Localization by Deep Learning
- [2017 @Face++] Delving Deep into Coarse-to-fine Framework for Facial Landmark Localization

## Wing Loss
---
- [2018 CVPR] Wing Loss for Robust Facial Landmark Localisation with Convolutional Neural Networks
- https://github.com/TropComplique/wing-loss

## DSRN
---
- [2018 CVPR] Direct shape regression networks for end-to-end face alignment
## LAB
---
- [2018 CVPR] Look at Boundary_ A Boundary-Aware Face Alignment Algorithm
- https://github.com/wywu/LAB

## RFLD
---
- [2018 CVPR] Robust facial landmark detection via a fully-convolutional local-global context network

## SAN
---
- [2018 CVPR] Style aggregated network for facial landmark detection

## TCNN
---
- [2018 TPAMI] Facial Landmark Detection with Tweaked Convolutional Neural Networks

## PFLD
---
- [2019] PFLD_ A Practical Facial Landmark Detector


# 传统方法
---

## ASM
---
- Active Shape Models-Their Training and Application
- Boosted Regression Active Shape Models

## AAM
---
- [1998 ECCV] Active appearance models
- [2004 IJCV] Active appearance models revisited
- [2011 BMVC] Accurate regression procedures for active appearance models
- [2007 ICCV] A nonlinear discriminative approach to aam fitting

## CRF
---
- [2012 CVPR] Real-time Facial Feature Detection using Conditional Regression Forests

## TSPM
---
- [2012 CVPR] Face detection, pose estimation, and landmark localization in the wild

## ESR, Explicit Shape Regression
---
- [2012 CVPR] Face alignment by explicit shape regression

## SDM, Supervised Descent Method
---
- [2013 CVPR] Supervised descent method and its applications to face alignment
- https://github.com/RoboPai/sdm

## CDM, cascaded deformable shape model
---
- [2013 ICCV] Pose-free facial landmark fitting via optimized part mixtures and cascaded deformable shape model

## LBF, Local Binary Features
---
- [2014 CVPR] Face Alignment at 3000 FPS via Regressing Local Binary Features
- https://github.com/jwyang/face-alignment

## RCPR, Robust Cascaded Pose Regression
---
- [2013 ICCV] Robust face landmark estimation under occlusion 

## ERT, Ensemble of Regression Trees
---
该方法在 Dlib 库中有实现.

- [2014 CVPR] One millisecond face alignment with an ensemble of regression trees


# Datasets & Challenges

## YouTube Faces Dataset with Facial Keypoints
---
This dataset is a processed version of the YouTube Faces Dataset, that basically contained short videos of celebrities that are publicly available and were downloaded from YouTube. There are multiple videos of each celebrity (up to 6 videos per celebrity).

Size: The size of the dataset is 10GB, and it includes approximately 1293 videos with consecutive frames of up to 240 frames for each original video. The overall single image frames are a total of 155,560 images. 

Projects: This dataset can be used to recognising faces in unconstrained videos.

**References**:
- https://www.kaggle.com/selfishgene/youtube-faces-with-facial-keypoints


## Kaggle Facial Keypoints Detection
---
**References**:
- https://www.kaggle.com/c/facial-keypoints-detection
- https://www.kaggle.com/drgilermo/face-images-with-marked-landmark-points


## 300-W
---
300-W (300 Faces in-the-Wild Challenge, 68 landmarks) is short for 300 Faces in-the-Wild. It is created from existing datasets, including LFPW, AFW, Helen, XM2VTS, and a new dataset called IBUG. It is created as a challenge and only provides training data.

300-W is currently the most widely-used inthe-wild dataset for 2D face alignment. Each image was re-annotated in a consistent manner using the 68
2D landmark configuration of Multi-PIE. The dataset contains in total ~4,000 near frontal facial images.

300W contains 3,148 training images and 689 testing images.

**References**:
- http://ibug.doc.ic.ac.uk/resources
- [2013 ICCVW] 300 faces in-the-wild challenge: The first facial landmark localization challenge


## 300-VW
---
> 300VW is designed as a benchmark for videos, containing 50 training videos and 64 testing videos. The testing set of 300VW is divided into three scenarios, i.e. category A: well-lit arbitrary expressions, category B: unconstrained illuminations and category C: arbitrary conditions. In this paper, these two datasets are combined in training.

**References**:
- [2015 ICCVW] The first facial landmark tracking in-the-wild challenge: Benchmark and results

    
## RWMB, Real-World Motion Blur
---
> It currently contains 20 videos with obvious real-world motion blur picked from YouTube, which include dancing, boxing, jumping, etc. There are 35,540 frames, which are all annotated with 98 landmarks following the protocol of WFLW.

**References**:
- [201910] FAB_ A Robust Facial Landmark Detection Framework for Motion-Blurred Videos


## WFLW
---
Wider Facial Landmarks in-the-wild (WFLW) contains 10000 faces (7500 for training and 2500 for testing) with 98 fully manual annotated landmarks. 
WFLW 数据集包含大量的遮挡, 光照, 侧脸, 夸张表情, 化妆和模糊的图像.

**References**:
- [2018 CVPR] Look at Boundary_ A Boundary-Aware Face Alignment Algorithm
- https://wywu.github.io/projects/LAB/WFLW.html

    
## AFLW, Annotated Facial Landmarks in the Wild
---
Annotated Facial Landmarks in the Wild (AFLW) provides a large-scale collection of annotated face images gathered from the web, exhibiting a large variety in appearance (e.g., pose, expression, ethnicity, age, gender) as well as general imaging and environmental conditions. In total about 25k faces are annotated with up to 21 landmarks per image.

AFLW is a facial key points detection benchmark which contains 24,386 faces with facial landmarks. This dataset is selected because it is more challenging than other datasets, such as LFPW. For example, AFLW has larger pose variations (39% of faces are non-frontal in our testing images) and severe partial occlusions. AFLW provides a large-scale collection of annotated face images with face location, gender and 21 facial landmarks.

**References**:
- https://www.tugraz.at/institute/icg/research/team-bischof/lrs/downloads/aflw/
- https://lrs.icg.tugraz.at/research/aflw/
- [2011 CVPRW] Annotated facial landmarks in the wild: A large-scale, real-world database for facial landmark localization


## COFW, Caltech Occluded Faces in the Wild
---
All images were hand annotated using the same 29 landmarks as in LFPW. 
COFW 数据集包含 507 张人脸图像, 该数据集中包含大量由物体遮挡的人脸图.

**References**:
- [2013 ICCV] Robust face landmark estimation under occlusion
- http://www.vision.caltech.edu/xpburgos/ICCV13/
    
    
## MUCT
---
The MUCT database consists of 3755 faces with 76 manual landmarks.

**References**:
- https://github.com/StephenMilborrow/muct
- http://www.milbo.org/muct


## Helen
---
Helen (194 landmarks) contains 2,300 high resolution web images.

**References**:
- http://www.ifp.illinois.edu/~vuongle2/helen/
- [2012 ECCV] Interactive facial feature localization


## AFW
---
**References**:
- [2012 CVPR] Face detection, pose estimation, and landmark localization in the wild


## BioID
---
This dataset consists of 1521 gray level images of resolution 384×286 for 23 different subjects. The dataset also includes 20 manually marked fiducial points on each face.

**References**:
- https://www.bioid.com/About/BioID-Face-Database


## LFPW, Labeled Face Parts in the Wild
---
LFPW (29 landmarks) is collected from the web. 

**References**:
- http://neerajkumar.org/databases/lfpw/
- [2011 CVPR] Localizing parts of faces using a consensus of exemplars


## MTFL, Multi-Task Facial Landmark
---
> Multi-Task Facial Landmark (MTFL) dataset contains annotations of five facial landmarks and attributes of gender, head pose, etc. consisting of 10,000 outdoor face images from the web. Each image is annotated with bounding box and five landmarks, i.e. centers of the eyes, nose, corners of the mouth.

> Multi-Task Facial Landmark (MTFL) dataset contains 12,995 face images annotated with 5 facial landmarks, namely, eye centers, nose tip and mouth corners. The images in the dataset contain various pose angles and occlusion, thus it is challenging to accurately localize facial landmarks.

**References**:
- [2013 CVPR] Deep Convolutional Network Cascade for Facial Point Detection
- [2014 ECCV] Facial landmark detection by deep multi-task learning
- http://mmlab.ie.cuhk.edu.hk/projects/TCDCN/data/MTFL.zip


## PUT
---
**References**:
- [2008] The put face database


## 300-W-LP, 300W-LP
---
> 300-W-LP, a synthetically expanded version of 300-W. 300-W-LP provides both 2D and 3D landmarks allowing for training models and conducting experiments using both types of annotations. 300-W-LP is a synthetically generated dataset obtained by rendering the faces of 300-W into larger poses, ranging from −900 to 900, using the profiling method. The dataset contains 61,225 images providing both 2D (300W-LP-2D) and 3D landmark annotations (300W-LP-3D).

300-W-LP 是 300-W across large poses 的简称. 该数据可以用做人脸关键点检测和人头姿态估计任务.

**References**:
- [2016 CVPR] Face alignment across large poses: A 3d solution


## XM2VTS
---
**References**:
- http://www.ee.surrey.ac.uk/CVSSP/xm2vtsdb/


## Menpo
---
The Menpo challenge dataset consists of semi-frontal and profile face image datasets. 
The dataset consists of training and testing subsets containing 6679 and 5335 images respectively. 
The training subset consists of images from the FDDB and AFLW datasets.
The image were annotated with the same set of 68 landmarks as the 300W competition data but no face detector bounding boxes. 
The annotations of the test subset have not been released.

**References**:
- [2017 CVPRW] The menpo facial landmark localisation challenge



## LFW
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
---
According to the standard LFW protocol, the performance measurement should be the mean accuracy over 10-fold face verification task with each fold containing 300 inter-class and 300 intra-class face pairs.

The LFW protocol consists of face verification based on ten-fold cross-validation, each fold containing 300 “‘same face” and 300 “not-same face” image pairs.


### Best-Rowden protocol (1:N 测试)
---
For the probe-gallery identification testing, there are two new protocols called the close set and open set identification tasks. 1) For the close set task, the gallery contains 4,249 identities, each with only a single face image, and the probe set contains 3,143 face images belonging to the same set of identities. The performance is measured by Rank-1 identification accuracy. 2) For the open set task, the gallery set includes 3,143 images of 596 identities. The probe set includes 10,090 images which are constructed by 596 genuine probes and 9,494 impostor ones. The accuracy is evaluated by the Rank-1 Detection and Identification Rate (DIR), which is genuine probes matched in Rank-1 at a 1% False Alarm Rate (FAR) of impostor ones that are not rejected.

**References**:
- [2014 TIFS] Unconstrained face recognition: Identifying a person of interest from a media collection


### BLUFR protocol
---
The Benchmark of Large-scale Unconstrained Face Recognition (BLUFR) is a new benchmark for LFW evaluations, which contains both verification and open- set identification. There are 10-fold experiments, with each fold containing about 156,915 genuine matching and 46,960,863 impostor matching on average for performance evaluation. It is more challenging and generalized for LFW.

**References**:
- [2014 IJCB] A benchmark study of large-scale unconstrained face recognition


## 衍生数据集

### CPLFW
---
**References**:
- [2018] Cross-pose lfw_ A database for studying cross-pose face recognition in unconstrained environments
- http://whdeng.cn/CPLFW


### CALFW
---
**References**:
- [2017] Cross-age lfw_ A database for studying cross-age face recognition in unconstrained environments
- http://whdeng.cn/CALFW


### SLLFW
---
**References**:
- http://whdeng.cn/SLLFW/
- [2017] Fine-grained face verification: FGLFW database, baselines, and human-DCMN partnership
- [2016 ICB] Fine-grained LFW database

### LFWA
---
LFWA is another unconstrained face attributes database with face images from the LFW database (13, 233 images of 5, 749 subjects), and the same 40 attribute annotations as in the CelebA database.

**References**:
- [2015 ICCV] Deep learning face attributes in the wild


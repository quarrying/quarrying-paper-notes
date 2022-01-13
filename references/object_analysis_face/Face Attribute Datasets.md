## MAAD-Face
MAAD-Face is build on the VGGFace2 database and thus, consists of **3.3M faces of over 9k individuals**. Using a novel annotation transfer-pipeline that allows an accurate label-transfer from multiple source-datasets to a target-dataset, MAAD-Face consists of 123.9M attribute annotations of 47 different binary attributes. Consequently, it provides 15 and 137 times more attribute labels than CelebA and LFW.

**References**:
- [202012] MAAD-Face_ A Massively Annotated Attribute Dataset for Face Images
- https://github.com/pterhoer/MAAD-Face


## CelebA, CelebFaces Attributes
CelebA 系 CelebFaces Attributes 的简称. CelebA 包含 200K 张图像, 40 个属性. CelebA 和 LFW 之间没有身份重叠.

CelebFaces Attributes Dataset (CelebA) is a large-scale face attributes dataset with more than 200K celebrity images, each with 40 attribute annotations.

**References**:
- http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html
- [2015 ICCV] Deep Learning Face Attributes in the Wild


## LFWA, LFW Attributes
LFWA is another unconstrained face attributes database with face images from the LFW database (13,233 images of 5,749 subjects), and the same 40 attribute annotations as in the CelebA database.

**References**:
- [2015 ICCV] Deep Learning Face Attributes in the Wild


## Adience
Adience 数据集来源为 Flickr 相册, 由用户使用 iPhone 或者其它智能手机设备拍摄. 该数据集主要用于进行年龄和性别的未经过滤的面孔估计. 同时里面还进行了相应的 landmark 的标注, 其中包含 2284 个类别和 26580 张图片. 年龄标签是年龄段, 为 (0-2, 4-6, 8-13, 15-20, 25-32, 38-43, 48-53, 60+). 

**References**:
- http://www.openu.ac.il/home/hassner/Adience/data.html


## UMDFaces
UMDFaces is a face dataset divided into two parts: 
- Still Images: 367,888 face annotations for 8,277 subjects.
- Video Frames: Over 3.7 million annotated video frames from over 22,000 videos of 3100 subjects.

**References**:
- http://www.umdfaces.io/
- [2017] The do’s and don’ts for cnn-based face verification
- [2016] Umdfaces: An annotated face dataset for training deep networks

    
## USTC CoarseData / FineData
This dataset contains [CoarseData](https://drive.google.com/open?id=0B0A9UsiwtVTHY0p4em5qUzRISW8) and [FineData](https://drive.google.com/open?id=0B6B08IBRi1PFbzhJeF9vNmVrUjA) augmented from 3131 images of [300-W](https://ibug.doc.ic.ac.uk/resources/300-W/) with the method described in the paper [3DFaceNet: Real-time Dense Face Reconstruction via Synthesizing Photo-realistic Face Images](https://arxiv.org/abs/1708.00980). CoarseData is constructed by varying poses and expressions of the original images. FineData is constructed by transferring details from other images to the original images. We augment each image 30 times for both CoarseData and FineData.

**References**:
- https://github.com/Juyong/3DFace
    

## MTFL, Multi-Task Facial Landmark
Multi-Task Facial Landmark (MTFL) dataset contains annotations of five facial landmarks and attributes of gender, head pose, etc. Consisting of 10,000 outdoor face images from the web. Each image is annotated with bounding box and five landmarks, i.e. centers of the eyes, nose, corners of the mouth.

**References**:
- [2013 CVPR] Deep Convolutional Network Cascade for Facial Point Detection
- [2014 ECCV] Facial landmark detection by deep multi-task learning
- http://mmlab.ie.cuhk.edu.hk/projects/TCDCN/data/MTFL.zip


## CEW, Closed Eyes In The Wild
Eye closeness detection is a challenging task in the unconstrained real-world application scenario which is full of challenging variations caused by individual difference and kinds of environment changes including lighting, blur, occlusion, and disguise. To investigate the performance of eye closeness detection in these conditions, we collected a dataset for eye closeness detection in the Wild. In particular, this dataset contains 2423 subjects, among which 1192 subjects with both eyes closed are collected directly from Internet, and 1231 subjects with eyes open are selected from the Labeled Face in the Wild database. 

**References**:
- http://parnec.nuaa.edu.cn/xtan/data/ClosedEyeDatabases.html
- [2014 PR] Eyes Closeness Detection from Still Images with Multi-scale Histograms of Principal Oriented Gradients

    
## YawDD
**References**:
- [2014] YawDD_ A Yawning Detection Dataset
    
    
## HUST-LEBW
**References**:
- [2019] Towards Real-time Eyeblink Detection in The Wild: Dataset, Theory and Practices
   

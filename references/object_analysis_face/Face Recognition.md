# 人脸识别
- DeepFace Series
    - [2014 CVPR] DeepFace: Closing the gap to human-level performance in face verification
    - [2015 CVPR] Web-Scale Training for Face Identification
- DeepID Series
    - DeepID: [2014 CVPR] Deep learning face representation from predicting 10,000 classes
    - DeepID2: [2014 NIPS] Deep Learning Face Representation by Joint Identification-Verification
    - DeepID2+: [2015 CVPR] Deeply learned face representations are sparse, selective, and robust
    - DeepID3: [2015] DeepID3_ Face Recognition with Very Deep Neural Networks
- VGGFace
    - [2015 BMVC] Deep Face Recognition
    - http://www.robots.ox.ac.uk/~vgg/software/vgg_face/
- **FaceNet**
    - [2015 CVPR] FaceNet: A unified embedding for face recognition and clustering
- **CenterLoss**, Face-ResNet
    - [2016 ECCV] A Discriminative Feature Learning Approach for Deep Face Recognition
- DocFace
    - [2018] Docface_ Matching id document photos to selfies
    - [2018] DocFace+_ ID Document to Selfie Matching
    - https://github.com/seasonSH/DocFace
- Bisample
    - [2018] Large-scale bisample learning on id vs. spot face recognition
- NoiseFace
    - [2019] Noise-Tolerant Paradigm for Training Face Recognition CNNs
- Unequal-Training
    - [2019 CVPR] Unequal-Training for Deep Face Recognition With Long-Tailed Noisy Data
- RegularFace
    - [2019 CVPR] RegularFace_ Deep Face Recognition via Exclusive Regularization
- UniformFace
    - [2019 CVPR] UniformFace_ Learning Deep Equidistributed Representation for Face Recognition
- **ArcFace**
    - [2019 CVPR] ArcFace_ Additive Angular Margin Loss for Deep Face Recognition
- P2SGrad
    - [2019 CVPR] P2SGrad_ Refined Gradients for Optimizing Deep Face Models
- AdaptiveFace
    - [2019 CVPR] AdaptiveFace_ Adaptive Margin and Sampling for Face Recognition
- AdaCos
    - [2019 CVPR] AdaCos_ Adaptively Scaling Cosine Logits for Effectively Learning Deep Face Representations
- AirFace
    - [2019] AirFace_ Lightweight and Efficient Model for Face Recognition
- [2019 CVPR] Low-Rank Laplacian-Uniform Mixed Model for Robust Face Recognition
- [2019 CVPR] Feature Transfer Learning for Face Recognition With Under-Represented Data
- [2019 CVPR] R3 Adversarial Network for Cross Model Face Recognition
- [2020] Partial FC_ Training 10 Million Identities on a Single Machine



# 跨模态人脸识别
- Recon. + UDP
    - [2015 CVPRW] NIR-VIS Heterogeneous Face Recognition via Cross-Spectral Joint Dictionary Learning and Reconstruction
- TRIVET
    - [2016 ICB] Transferring deep representation for nir-vis heterogeneous face recognition
- IDR, Invariant Deep Representation
    - [2017 AAAI] Learning Invariant Deep Representation for NIR-VIS Face Recognition
- CDL, Coupled deep learning
    - [2018 AAAI] Coupled Deep Learning for Heterogeneous Face Recognition
- ADFL, Adversarial Discriminative Feature Learning
    - [2018 AAAI] Adversarial Discriminative Heterogeneous Face Recognition
- W-CNN
    - [2018 TPAMI] Wasserstein CNN: Learning Invariant Features for NIR-VIS Face Recognition
- DVR, Disentangled Variational Representation
    - [2019 AAAI] Disentangled Variational Representation for Heterogeneous Face Recognition
    
    
# 三维人脸识别
- [2003 TPAMI] Face recognition based on fitting a 3D morphable model
- [2016 ECCV] Face recognition using a unified 3D morphable model
- [2016] Do We Really Need to Collect Millions of Faces for Effective Face Recognition?
- [2017] Learning from millions of 3d scans for large-scale 3d face recognition
- Led3D
    - [2019 CVPR] Led3D_ A Lightweight and Efficient Deep Approach to Recognizing Low-Quality 3D Faces
    
    
# 人脸数据增强
- [2016] Frankenstein_ Learning Deep Face Representations using Small Data
- [2018] Training Deep Face Recognition Systems with Synthetic Data
- [2016 ECCV] Do we really need to collect millions of faces for effective face recognition
- [2017 FG] Rapid Synthesis of Massive Face Sets for Improved Face Recognition
- [2018] Face Synthesis for Eyeglass-Robust Face Recognition
- [2018] Generating Photo-Realistic Training Data to Improve Face Recognition Accuracy
- [2018] Priming Deep Neural Networks with Synthetic Faces for Enhanced Performance


# 人脸聚类
- [2016] Clustering Millions of Faces by Identity
- [2019 CVPR] Linkage based face clustering via graph convolution network


# 基于图像集或视频的人脸识别
- [2017] Video-based face recognition using ensemble of haar-like deep convolutional neural networks
- [2017 CVPR] Range loss for deep face recognition with long-tailed training data
- NAN
    - [2017 CVPR] Neural Aggregation Network for Video Face Recognition
- QAN
    - [2017 CVPR] Quality Aware Network for Set to Set Recognition
- [2017 TPAMI] Trunk-Branch Ensemble Convolutional Neural Networks for Video-based Face Recognition
- [2018] Unsupervised Learning of Face Representations
- SeqFace
    - [2018] SeqFace_ Make full use of sequence information for face recognition
- GhostVLAD
    - [2018 ACCV] GhostVLAD for set-based face recognition
- C-FAN
    - [2019] Video Face Recognition: Component-wise Feature Aggregation Network (C-FAN)
    
    
# 经典传统方法
- PCA-Eigenface
    - [1991 CVPR] Eigenfaces for Recognition
- LDA-Fisherface
    - [1997] Discriminant analysis for recognition of human face images
    - [1997 TPAMI] Eigenfaces vs. Fisherfaces: Recognition Using Class Specific Linear Projection
- EBGM
    - [1997 TPAMI] Face recognition by elastic bunch graph matching
- Laplacianfaces
    - [2005 TPAMI] Face Recognition Using Laplacianfaces,
- LDML-MkNN
    -[2009 ICPR] Is that you? metric learning approaches for face identification
- Multishot
    - [2009 BMVC] Multiple one-shots for utilizing class label information
- LE
    - [2010 CVPR] Face recognition with learning based descriptor
- Associate-Predict
    - [2011 CVPR] An associate-predict model for face recognition
- Tom-vs-Pete
    - [2012 BMVC] Tom-vs-pete classifiers and identitypreserving alignment for face verification
- Fisher Vector Face
    - [2013 BMVC] Fisher vector faces in the wild
- Joint Bayesian
    - [2012 ECCV] Bayesian face revisited: A joint formulation
- TL Joint Bayesian
    - [2013 ICCV] A practical transfer learning algorithm for face verification
- Gaussian Face (在 LFW 上达到 98.52% 的正确率)
    - [2014] Surpassing human-level face verification performance on lfw with gaussianface
- PLDA (Probabilistic LDA, 是一种生成式模型, 主要考虑解决人脸识别中光照姿态等影响)
    - [2007 ICCV] Probabilistic Linear Discriminant Analysis for Inferences About Identity
    - [2013 TPAMI] A Scalable Formulation of Probabilistic Linear Discriminant Analysis: Applied to Face Recognition
- LBP
    - [2006 TPAMI] Face Description with Local Binary Patterns: Application to Face Recognition 
    - [2007] Multi-scale local binary pattern histograms for face recognition
    - [2013 CVPR] Blessing of dimensionality: High-dimensional feature and its efficient compression for face verification
- Gabor
    - [2002 TIP] Gabor feature based classification using the enhanced fisher linear discriminant model for face recognition
    - [2007 TIP] Histogram of Gabor phase patterns (hgpp): a novel object representation approach for face recognition
    - [2010 TIP] Fusing local patterns of gabor magnitude and phase for face recognition
- Sparse
    - [2009] Robust Face Recognition via Sparse Representation


# 综合其他
- [handong1587 face-recognition](https://handong1587.github.io/deep_learning/2015/10/09/face-recognition.html)
- OpenFace
    - https://github.com/cmusatyalab/openface
- FaceNet
    - https://github.com/davidsandberg/facenet
- SeetaFace
    - https://github.com/seetaface/SeetaFaceEngine
- face_recognition
    - https://github.com/ageitgey/face_recognition
- insightface
    - https://github.com/deepinsight/insightface
- OpenBR
    - https://github.com/biometrics/openbr
    - http://www.openbiometrics.org
- DeepFace
    - https://github.com/RiweiChen/DeepFace
- gluon-face
    - https://github.com/THUFutureLab/gluon-face
- FaceX-Zoo
    - https://github.com/JDAI-CV/FaceX-Zoo
- face.evoLVe
    - https://github.com/ZhaoJ9014/face.evoLVe.PyTorch
- https://github.com/meownoid/face-identification-tpe
- https://bitbucket.org/marcopede/face-eval
- https://github.com/SelinaFelton/LightFaceNet
- https://gitee.com/kuaikuaikim/dface
- https://github.com/auroua/InsightFace_TF/
- https://github.com/hanson-young/nniefacelib


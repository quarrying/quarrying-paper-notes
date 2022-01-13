# 文献
- [2009] Facial expression recognition based on local binary patterns_ A comprehensive study
- [2012] Facial expression recognition based on local phase quantization and sparse representation
- [2017 CVPR] Using synthetic data to improve facial expression analysis with 3d convolutional networks
- ExpNet
    - [2018 FG] ExpNet_ Landmark-Free, Deep, 3D Facial Expressions
    - https://github.com/fengju514/Expression-Net
- [2019] Region Attention Networks for Pose and Occlusion Robust Facial Expression Recognition
    - https://github.com/kaiwang960112/Challenge-condition-FER-dataset
    
    
# Datasets & Challenges

## Google Facial Expression Comparison Dataset
This dataset by Google is a large-scale facial expression dataset that consists of face image triplets along with human annotations that specify, which two faces in each triplet form the most similar pair in terms of facial expression. 

Size: The size of the dataset is 200MB, which includes 500K triplets and 156K face images.

Projects: The dataset is intended to aid researchers working on topics related to facial expression analysis such as expression-based image retrieval, expression-based photo album summarisation, emotion classification, expression synthesis, etc.

**References**:
- https://research.google/tools/datasets/google-facial-expression/
  

## RAF-DB, Real-world Affective Faces Database
Real-world Affective Faces Database (RAF-DB) is a large-scale facial expression database with around 30K great-diverse facial images downloaded from the Internet. Based on the crowdsourcing annotation, each image has been independently labeled by about 40 annotators. Images in this database are of great variability in subjects' age, gender and ethnicity, head poses, lighting conditions, occlusions, (e.g. glasses, facial hair or self-occlusion), post-processing operations (e.g. various filters and special effects), etc.

**References**:
- http://www.whdeng.cn/raf/model1.html
- [2017 CVPR] Reliable Crowdsourcing and Deep Locality-Preserving Learning for Expression Recognition in the Wild
- [2019 TIP] Reliable Crowdsourcing and Deep Locality-Preserving Learning for Unconstrained Facial Expression Recognition

    
## RAF-ML, Real-world Affective Faces Multi Label
**References**:
- http://whdeng.cn/RAF/model2.html
- [2019 IJCV] Blended Emotion in-the-Wild: Multi-label Facial Expression Recognition Using Crowdsourced Annotations and Deep Locality Feature Learning

    
## BNU-LSVED, BNU Large-scale Spontaneous Visual Expression Database
**References**:
- [2016] BNU-LSVED: a multimodal spontaneous expression database in educational environment


## FERPlus


## AffectNet


## FER 2013
The Facial Expression Recognition 2013 (FER-2013) database was introduced in the ICML 2013 Challenges in Representation Learning. The database was created using the Google image search API and faces have been automatically registered. Faces are labeled as any of the six basic expressions as well as the neutral. The resulting database contains 35,887 images most of them in wild settings.

the FER2013 database (one of the largest recently released FER databases) contains 35,887 images of different subjects yet only 547 of the images portray disgust.

The FER 2013 challenge was created using Google image search API with 184 emotion related keywords, like blissful, enraged. Keywords were combined with phrases for gender, age and ethnicity in order to obtain up to 600 different search queries. Image data was collected for the first 1000 images for each query. Collected images were passed through post-processing, that involved face region cropping and image alignment. Images were then grouped into the corresponding fine-grained emotion classes, rejecting wrongfully labeled frames and adjusting cropped regions. The resulting data contains nearly 36,000 images, divided into 8 classes (7 effective expressions and a neutral class), with each emotion class containing a few thousand images (disgust being the exception with only 547 frames).

**References**:
- http://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge


## GENKI-4K
The GENKI-4K dataset contains 4,000 face images spanning a wide range of subjects, facial appearance, illumination, geographical locations, imaging conditions, and camera models. All images are labeled for both Smile content (1=smile, 0=non-smile) and Head Pose (yaw, pitch, and roll parameters, in radians).

Among these pictures, 2162 images are labeled as smile and 1838 im- ages are labeled as non-smile. 


## JAFFE, The Japanese Female Facial Expression Database
The database contains 213 images of 7 facial expressions (6 basic facial expressions + 1 neutral) posed by 10 Japanese female models. Each image has been rated on 6 emotion adjectives by 60 Japanese subjects. The database was planned and assembled by Michael Lyons, Miyuki Kamachi, and Jiro Gyoba. We thank Reiko Kubota for her help as a research assistant. The photos were taken at the Psychology Department in Kyushu University.

**References**:
- http://www.kasrl.org/jaffe.html
- http://www.kasrl.org/jaffeimages.zip

    
## CK, CK+, Cohn-Kanade AU-Coded Expression Database
The Extended Cohn-Kanade database (CK+) includes 593 video sequences recorded from 123 subjects ranging from 18 to 30 years old. Subjects displayed different expressions starting from the neutral for all sequences, and some sequences are labeled with basic expressions.

**References**:
- [2010 CVPRW] The extended cohn-kanade dataset (ck+): a complete dataset for action unit and emotion-specified expression
- http://www.consortium.ri.cmu.edu/ckagree/

    
## NovaEmotions
NovaEmotions, aim to represent facial expressions and emotional state as captured in a non-controlled environment. The data is collected in a crowd-sourcing manner, where subjects were put in front of a gaming device, which captured their response to scenes and challenges in the game itself. The game, in time, reacted to the player’s response as well. This allowed collecting spontaneous expressions from a large pool of variations. 
The NovaEmotions dataset consists of over 42,000 images taken from 40 different people. Majority of the participants were college students with ages ranges between 18 and 25. Data presents a variety of poses and illumination. 

**References**:
- [2013 ACMMM] Competitive affective gaming: Winning with a smile
- [2016 CVIU] Crowdsourcing facial expressions for affective-interaction

    
## EmotiW
EmotiW 2015; EmotiW 2016

**References**:
- [20015] Video and Image based Emotion Recognition Challenges in the Wild: EmotiW 2015


## AFEW / SFEW
Acted Facial Expressions In The Wild (AFEW) is a dynamic temporal facial expressions data corpus consisting of close to real world environment extracted from movies. Static Facial Expressions in the Wild (SFEW)  has been developed by selecting frames from AFEW. 

**References**:
- https://cs.anu.edu.au/few/AFEW.html

    
## MMI
**References**:
- http://mmifacedb.eu/ 
- http://ibug.doc.ic.ac.uk/research/mmi-database/


## USTC-NVIE
The Key Laboratory of Computing and Communication Software of Anhui Province(CCSL) has constructed the USTC-NVIE (Natural Visible and Infrared facial Expression) database under the sponsor of the 863 project. To date, most facial expression analysis has been based on visible and posed expression databases. Visible images, however, are easily affected by illumination variations, while posed expressions differ in appearance and timing from natural ones. We propose and establish a natural visible and infrared facial expression database, which contains both spontaneous and posed expressions of more than 100 subjects, recorded simultaneously by a visible and an infrared thermal camera, with illumination provided from three different directions. The posed database also includes expression image sequences with and without glasses.


## DISFA/DISFA+
**References**:
- http://mohammadmahoor.com/disfa/

    
## BP4D
**References**:
- http://www.cs.binghamton.edu/~lijun/Research/3DFE/3DFE_Analysis.html


    
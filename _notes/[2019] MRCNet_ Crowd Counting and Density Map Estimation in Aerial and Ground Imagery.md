- 20200105
----

论文主要有两个贡献: 
1) 提出一个新的人群数据集: DLR Aerial Crowd Dataset (DLR-ACD), 据称是第一个公开的航拍人群数据集. 
2) 提出 Multi-Resolution Crowd Network (MRCNet). The encoder is based on the VGG-16 network and the decoder is composed of a set of bilinear upsampling and convolutional layers.  In addition, MRCNet utilizes contextual and detailed local information by combining high- and low-level features through a number of lateral connections inspired by the Feature Pyramid Network (FPN) technique.

## DLR-ACD
DLR-ACD is a collection of 33 large RGB aerial images with average size of 3619×5226 pixels acquired through 16 different flight campaigns performed between 2011 and 2017.

数据集标注: The dataset was labeled manually with point-annotations on individual people taking about 80 hours, and resulted in 226,291 person annotations, ranging from 285 to 24,368 annotations per image. Crowd annotation in aerial images is a challenging task due to the large image sizes as well as the large number and the small size of the people in the images. While in dense crowd areas, discriminating each person from adjacent people is difficult, in sparse crowd areas localizing and discriminating each person from similar-looking objects is also challenging and time consuming.

数据集划分: The dataset was manually split into 19 training and 14 test images, and the splits were not randomized. The counts in the training and test sets are 138,151 and 88,140 persons.

常见数据集比较:
![](<[2019] MRCNet_ Crowd Counting and Density Map Estimation in Aerial and Ground Imagery/dataset_comparsion.png>)

## MRCNet
MRCNet 的架构是以 VGG 为蓝本, 并借鉴了 FPN, 如下:
![](<[2019] MRCNet_ Crowd Counting and Density Map Estimation in Aerial and Ground Imagery/mrcnet.png>)

It takes a single image of arbitrary size and, in a fully-convolutional manner, predicts two density maps, one with 1/4 of the input image size for the people counting task and the other one with the input image size for the density map estimation task. 


## Evaluation Metrics
人群计数性能评估指标使用常规的Mean Absolute Error (MAE) 和Root Mean Squared Error (RMSE), 除此之外论文还提出了一个新的评估指标: Mean Normalized Absolute Error (MNAE). 论文指出 MAE and RMSE treat all images equally without considering the differences between their true counts. This could be problematic for the datasets with large variations of the image counts. 它们的定义如下:
![](<[2019] MRCNet_ Crowd Counting and Density Map Estimation in Aerial and Ground Imagery/eval_metric.png>)

论文还在 DLR-ACD 数据集上进行了人体检测, 使用的评估指标是: precision, recall 和 f1-score.

## Experiments
论文在 DLR-ACD 和 ShanghaiTech 两个数据集上做了实验. 

生成热图: 采用的是 [2016 CVPR] Single-image crowd counting via multi-column convolutional neural network 中的方法: smoothing the person locations with a small 2D Gaussian, a procedure which is aimed at avoiding the imbalance between the number of positive and negative samples (a pixel on each person versus all other image pixels). 由于 DLR-ACD 数据集的 spatial resolution (GSD; ground sampling distances) 是已知的, 所以在该数据集上可以根据 GSD 自适应地确定高斯平滑的程度. 

数据预处理: 包括裁剪, 数据增强等. 

实验结果如下:
![](<[2019] MRCNet_ Crowd Counting and Density Map Estimation in Aerial and Ground Imagery/table_3.png>)

![](<[2019] MRCNet_ Crowd Counting and Density Map Estimation in Aerial and Ground Imagery/table_4.png>)


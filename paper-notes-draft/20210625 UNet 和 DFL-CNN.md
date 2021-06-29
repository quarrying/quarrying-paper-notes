## [2015] U-Net_ Convolutional Networks for Biomedical Image Segmentation

U-Net 主要包含编码器和解码器两部分. 编码器主要由一系列的卷积层和池化层构成, 每经过一次下采样, 通道数翻倍. 解码器主要由一系列的上采样层和卷积层构成. 解码器最终得到与原图同样大小的特征图, 其再经过一个核尺寸为 1x1 的卷积层, 得到每个像素属于每个类别的概率. 另外 U-Net 还通过横向连接融合了解码器的高层语义信息和编码器的底层细节信息, 使分割结果更加精细.

## [2016] Learning a Discriminative Filter Bank within a CNN for Fine-grained Recognition

DFL-CNN 主要包括骨干网络和分支网络. 常见的经典 CNN 都可以用来作为骨干网络, 其用来提取基础特征. 分支网络分为三个部分: 1) G-Stream: 用来提取全局特征; 2) P-Stream, 用来提取判别性的块特征; 3) Side Branch: 用来提取类依赖的判别性的块特征. 可以在骨干网络的多个尺度上引出分支网络, 最后各尺度的各分支的输出特征进行加权融合, 得到最终的特征, 送入分类器进行分类. DFL-CNN 的最终特征融合了多尺度的全局和局部特征, 具有较高的可判别性. 


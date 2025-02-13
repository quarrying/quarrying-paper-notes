- 20210113
- 20210218
---
![](<[2021] Pushing the Envelope of Thin Crack Detection/paper_title.png>)

该论文将 crack detection 定义为语义分割问题. 但为了检测细裂纹, 该论文采用了非常规的标注方式, 用单像素宽度的线来表示裂纹 (文中提出一种半自动的标注方法). 论文的创新之处有: 1) 为了与标注方式相匹配, 使用 MSE loss 而不是 CE loss; 2) 提出一种数据增强方式: 图像先缩小再放大回原来尺寸, 而标注不变 (这种增强方式在 CV 中是比较常用的); 3) 用 Lp Pooling 替换了网络 (UNet) 中所有的 Max Pooling (没看明白文中的解释); 4) 利用 auto-encoder 来学习裂纹的形状先验, 并用其来消除一些检测到的短裂纹.

## 论文摘记
1) Surface crack detection 中 surface 常见的有: roads, concrete surfaces, metals.

2) In the problem of crack detection, thick cracks are easy to detect while thin cracks are not. Thus, accuracy is mostly determined by how well the method can detect thin cracks.  crack detection的准确率主要受细裂痕的影响. 

3) In the case of concrete surfaces of a typical type of bridges, it is requested to find cracks with 0.5mm width and sometimes even those with 0.1mm width. 在某些场景下, crack detection 的精度要求比较高, 到亚毫米级别.

4) As we employ the same formulation as semantic segmentation, the network outputs a map of crack likelihood. Even for a thick crack having several pixel widths on the image, it has one pixel width in the label map, resulting in that many pixels on the imaged crack will be annotated as non-crack. The standard loss function used for semantic segmentation may not work well in the presence of such label differences. 该论文将 crack detection 定义为语义分割问题. 但本文标注方式比较特殊(只有一像素宽, 即使对于宽裂纹也是如此), 不能直接使用语义分割的交叉熵损失.

5) Cracks emerging on concrete surfaces tend to have more than a certain length and usually do not form isolated short segments due to a physical reason. 混凝土上的裂纹通常具有一定的长度.

## 论文疑问
I have some questions, any help from you will be greatly appreciated.

1) [36] and [37] maybe the same source.
![](<[2021] Pushing the Envelope of Thin Crack Detection/may_be_same.png>)

2) In Section 5.1
![](<[2021] Pushing the Envelope of Thin Crack Detection/360_degree_rotation.png>)

Colud you explain "Random 360-degree rotation"?

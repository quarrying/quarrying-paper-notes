- 20201203
----
![](<[2020 ECCV] PIoU Loss_ Towards Accurate Oriented Object Detection in Complex Environments/paper_title.png>)

本文的主要贡献是: 提出 了PIoU loss, 其可以改进目标检测的效果, 特别是具有高宽高比和复杂背景的旋转目标检测的效果. 作者认为基于 IoU 的 loss 要好于 distance loss (如 SmoothL1 Loss 等), 而 oriented bounding box (OBB) 之间IOU 的计算比较复杂, 于是本文提出了一种易于计算且同时适用于 horizontal and oriented bounding box (HBB and OBB) 的 IoU 计算方法, 并称之为 Pixels-IoU (简称为 PIoU), 其计算过程简述如下: 首先引入点在 OBB 内部或外部的判断函数, 然后在两个 OBB 的最小外接HBB中逐像素地累计两个 OBB 的重叠像素(同时在两个 OBB 中的像素)和两个 OBB 的并集像素(至少在一个 OBB 中的像素)的数目. 这种方式计算得到的 IoU 离散且不可导, 为此本文提出了一个带参数的核函数将 IoU 转化为连续且可导的形式. 最后在此基础上提出了 PIoU Loss. 另外本文还提出了一个新的目标检测数据集: Retail50K.




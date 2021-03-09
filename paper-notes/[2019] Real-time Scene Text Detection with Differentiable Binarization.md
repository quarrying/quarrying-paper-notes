- 20201217
-----
![](<[2019] Real-time Scene Text Detection with Differentiable Binarization/paper_title.png>)

场景文本检测(Scene Text Detection; STD)算法大致可以分为两类: 基于回归的方法和基于分割的方法. 基于分割的STD的优势在于可以描述不同形状的文本, 包括horizontal, multi-oriented and curved text等, 但同时具有后处理复杂的缺点. 二值化是基于分割STD的后处理中的重要步骤, 之前的做法是直接根据固定的全局阈值对分割网络得到的probability map做二值化得到binarization map, 之后还要用一些启发式的方法将binarization map上的前景像素合并为text instances. 本文的主要贡献是: 提出了一个Differentiable Binarization (DB)模块, 其可以在线的学习probability map上每个位置的阈值 (即学习threshold map), 结合probability map和threshold map能得到一个高健壮性的binarization map (文中有述: The differentiable binarization with adaptive thresholds can not only help differentiate text regions from the background, but also separate text instances which are closely jointed.), 简化了后处理操作 (猜测: 不再需要前述的启发式方法合并前景像素这一步骤, 而这一步通常是比较耗时的). 

论文要点: 1) 标准的二值化函数是不可导的, 本文提出了一个标准二值化函数的平滑近似函数; 2) 损失函数分为三部分, 分别为: 监督probability map的损失, 监督threshold map的损失和监督binarization map的损失.
- 20170214
----

论文作者在 AlexNet 的模型上做了一个有趣的实验, 发现: 低层的卷积层中的一些滤波器核存在着负相关程度很高的滤波器核, 且层次越高的卷积层, 这一现象越不明显. 作者把这一现象称为 pairing phenomenon.

设网络的某层滤波器组的卷积核的单位向量组表示为 ${\vec \phi _1},{\vec \phi _2}, \cdots ,{\vec \phi _n}$, 定义 ${\vec \phi _i}$ 的 pairing filter 为 $\vec \phi _i^* = \arg {\min _{{{\vec \phi }_j}}}\left\langle {{\vec \phi_i},{\vec \phi_j}} \right\rangle$, 其中 $j = 1,2, \cdots ,n$, $n$ 为该卷积层的滤波器数目. 同时它们之间的余弦相似度记为, $\mu _i^\phi  = \left\langle {{{\vec \phi }_i},\vec \phi _i^*} \right\rangle$.

论文作者基于上面的现象提出了一个假设: 
> we hypothesize that despite ReLU erasing negative linear responses, the first few convolution layers of a deep CNN manage to capture both negative and positive phase information through learning pairs or groups of negatively correlated filters. This conjecture implies that there exists a redundancy among the filters

为了消除 ReLU 带来的冗余, 论文作者提出了一个新的激活机制 (activation scheme), 称为 Concatenated Rectified Linear Units, 简称为 CReLU, 定义如下: 
$\operatorname{CReLU} \left( x \right) = \left( {{{\left[ x \right]}_ + },{{\left[ { - x} \right]}_ + }} \right)$, 其中 ${\left[  \cdot  \right]_ + } = \max \left( { \cdot ,0} \right)$.

注意到其与一般激活函数的不同之处: CReLU 有二维输出, 而一般的激活函数只有一维输出. 所以, 论文中提到: CReLU is based on an activation scheme rather than a function, which fundamentally differentiates itself from Leaky ReLU or other variants. 不过笔者觉得将 CReLU 视作一维输入二维输出的激活函数也无妨.

最后作者在三个数据集上验证了 CReLU 的有效性: CIFAR-10, CIFAR-100 和 ImageNet. 此外论文作者还从正则化和重建角度对 CReLU 的有效性进行了定性的讨论.


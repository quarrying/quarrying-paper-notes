- 20200813
----

## 论文疑问和想法

1) 第五面, batch bard 应为 batch hard, squired distance 应为 squared distance.
2) 公式 1), 为了论文自洽, 最好说明 $\[ \cdot \]_{+}$ 的含义.
3) As shown in Figure 2, our CBDB-Net contains four components: the Backbone Network, the Consecutive Batch DropBlock Module (CBDBM), the Elastic Loss and Network Architecture Overview. "Network Architecture Overview" 不宜称为 CBDB-Net 的一个 component, 而是 Section III 的一部分.
4) In this subsection, we revisit the network architecture and summary loss functions of our CBDB-Net for the training and testing stage. summary 应为动词.
5) 一些想法: 保留完整 feature map; 各分支 ResBlock 参数不共享.


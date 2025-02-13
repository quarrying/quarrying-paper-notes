- 20201207
----
![](<[2020] Cc-Loss_ Channel Correlation Loss For Image Classification/paper_title.png>)

该文的主要贡献是: 提出了一个新的分类 loss. 作者认为之前的 CELoss 及其改进 Loss (如ArcFace loss 等) 没有考虑特征分布与网络结构之间的关系, 所以限制了可判别特征的学习. 鉴于此, 该文提出了 CC-Loss (channel correlation loss), 其能够约束类与通道之间的特定关系, 同时保持类内和类间的可分性. 

论文使用 SE module 作为 channel attention module, 用其来产生 channel attention vector. 在此基础上引入了 CC-Loss, 以使同类的 channel attention vector 距离变小, 而不同类的 channel attention vector 距离变大.

论文不足之处: 1) 2.3. Computational Complexity Reduction 节中计算复杂度的计算可能有误; 2) 没有在更大规模数据集 (如人脸识别数据集) 上做验证.


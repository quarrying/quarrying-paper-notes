- 20201208
----
![](<[2020] OneNet_ End-to-End One-Stage Object Detection by Classificaion Cost/paper_title.png>)

该论文的主要贡献是提出了一种新的 label assignment, 并基于此实现了一种端到端的 one-stage detector, 文中称之为 OneNet (取义于 one-stage pipeline and one positive sample). 

新的 label assignment 不仅考虑了通常使用的 position cost, 还考虑了 classification cost, 最终的 matching cost 是 position cost (具有 L1Loss 和 GIoULoss 相同的数学形式) 和 classification cost (具有 FocalLoss 相同的数学形式)的加权和. 另外对于每个 ground-truth, 所有样本中与其 matching cost 最小的样本才被选为正样本标签, 其他样本均为负样本 (for each ground-truth, only one sample of minimum cost among all samples is chosen as positive sample, others are all negative ones). 

论文实验验证了新的 label assignment 使 NMS 不再必要(添加了 NMS, 性能反而会下降), 且有不错的效果 (On coco dataset, OneNet achieves 35.0 AP and 67 FPS using ResNet50 and image size of 512 pixels), 实现了端到端地训练.

一些细节:
1) 已有 Two-stage detector 在 label assignment 中引入 classification cost, 但还没有 one-stage detector 引入 classification cost. ( Section 1 中: The well-established end-to-end detectors [1, 13, 10] assign labels by both position cost and classification cost. However, existing one-stage detectors assign labels by sole location cost without classification cost, which leads to redundant boxes of high confidence scores in inference, making non-maximum suppression(NMS) post-processing a necessary component.)
2) OneNet 的训练 loss 和 label assignment 中的 cost 具有相同的数学形式. (Section 3 中: The training loss is the same as the matching cost except that only performed on matched pairs.)
3) 一般文献使用的 position cost 是 pre-defined position cost (The location cost of pre-defined is the distance between fixed position of grid point in feature map and position of ground-truth box center). 该论文还引入了 predicted position cost (参考 Section 2). 由 Table 1 可见, 单独使用 predicted position cost 作为 matching cost 的效果惨不忍睹, 但结合 classification cost 之后效果要好于 pre-defined position cost+classification cost.

## 相关链接
- https://arxiv.org/abs/2012.05780
- https://github.com/PeizeSun/OneNet



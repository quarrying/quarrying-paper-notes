- 20201208
----
![](<[2020] MAAD-Face_ A Massively Annotated Attribute Dataset for Face Images/paper_title.png>)

本文的主要贡献是:
1) 提出了一种构建高质量人脸属性数据集的方法. 这是论文的核心.
2) 采用提出的方法, 构建了迄今最大的人脸属性数据集 MAAD-Face. 该数据集提供了47类二元属性标注, 共有 123.9M 条标注, 规模是LFW的137倍, CelebA的15倍. 

## Label-transfer pipeline

使用 CelebA 和 LFW 作为源数据集, VGGFace2 作为目标数据集.

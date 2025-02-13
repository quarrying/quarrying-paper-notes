- 20201229
----
![](<[2020] Scene Text Detection with Scribble Lines/paper_title.png>)

本文的主要贡献是: 提出了一种弱监督的场景文本检测 (STD) 框架. 用在 STD 任务中的标注类型有: 1) 轴对称包围盒; 2) 四边形或带方向的矩形包围盒; 3) 多边形. 1) 和 2) 的没有包含足够多的形状信息, 3)的标注成本较高. 于是本文提出了新的标注类型 scribble line (可以认为是按顺序连接 text instance 中各字符中心的折线, 其标注成本与3)相比要小, 但也不失通用性), 以及利用该标注类型的 STD 框架. 新的 STD 框架包括两个 head: 1) Character Detection Branch. 由于 scribble line 不包含字符或文本边界信息, 为此该文用一个预训练模型 (使用合成数据训练的) 来生成某些字符的包围盒和类别, 该分支的标签即为这些包围盒和类别; 2) Text-Line Segmentation Branch. 该分支的标签是 scribble line. 在训练时, 先使用合成数据进行预训练, 再使用合成数据和真实数据进行微调. 作者在几个经典的 STD benchmark 上验证了该框架的有效性, 有的数据集上还取得了 SOTA.

## 相关链接
- https://arxiv.org/abs/2012.05030

## Bibtex
```bibtex
@misc{zhang2020scene,
      title={Scene Text Detection with Scribble Lines}, 
      author={Wenqing Zhang and Yang Qiu and Minghui Liao and Rui Zhang and Xiaolin Wei and Xiang Bai},
      year={2020},
      eprint={2012.05030},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
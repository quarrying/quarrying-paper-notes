
- 数据集半自动化标注
    - 图像级, 实例级, 像素级
    - 实例级, 类别级, 数据集级
- 数据集半自动化清洗
- 数据集调试
- 数据集管理


# 数据管理
用 git 结合其他命令做数据集管理, 或者用类似 git 的工具管理数据集.

## DVC, Data Version Control
---
- https://dvc.org/
- https://zhuanlan.zhihu.com/p/487688085
- https://zhuanlan.zhihu.com/p/345720908

## TensorBay
----
- https://zhuanlan.zhihu.com/p/363496820


# 半自动化清洗

## Confident learning, CL, cleanlab
----

### Out-of-sample and in-sample predicted probabilities 
> Out-of-sample predicted probabilities refer to the model's probabilistic predictions made only on datapoints that were not shown to the model during training. In contrast, in-sample predicted probabilities on the model's training data will often be way overconfident and cannot be trusted.

### References
- https://cleanlab.ai/
- https://github.com/cleanlab/cleanlab
- [2022] Confident Learning_ Estimating Uncertainty in Dataset Labels

## [2021] Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks
----

## [2020] A survey on deep learning with noisy labels: How to train your model when you cannot trust on the annotations?
----

## ProMix
----
- [2022] ProMix: Combating Label Noise via Maximizing Clean Sample Utility


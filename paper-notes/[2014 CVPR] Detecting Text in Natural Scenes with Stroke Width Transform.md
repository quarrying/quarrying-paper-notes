- 2014
---

大致流程为：利用Canny算子得到图像的边缘图，利用梯度算子得到图像上每个像素的梯度方向（即归一化梯度向量），利用几何知识确定以边缘为开始且以该点处的梯度方向为方向的射线上像素的笔画宽度。边缘像素均做如上处理，得到SWT图。

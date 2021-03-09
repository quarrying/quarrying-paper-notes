- 20201103
-----
![](<[2020 ECCV] Dive Deeper Into Box for Object Detection/paper_title.png>)

## Related Work
基于Anchor的目标检测器的缺点是: anchor 的预置参数较多 (包括 anchor 的尺寸, anchor 的宽高比等), 以及需要一些预置参数来标记 anchor 的标签.

Facts: DenseBox 是 anchor-free 检测器的先锋之作, 但由于它不能有效处理目标重叠的情况, 故而不太适用于通用目标检测.

Facts: anchor-free 的方法容易在远离目标中心的位置产生大量的低质量的包围盒. 在 FCOS 中引入了 centerness 分支用来预测包围盒内像素相对于包围盒中心的偏移程度, 预测得到的 centerness 得分可用来抑制检测到的低质量的包围盒.


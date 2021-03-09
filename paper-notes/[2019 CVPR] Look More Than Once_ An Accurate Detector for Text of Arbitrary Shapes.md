
- 20210218
----
![](<[2019 CVPR] Look More Than Once_ An Accurate Detector for Text of Arbitrary Shapes/paper_title.png>)

该论文在 backbone 之后引出三个分支, DR (Direct Regressor, 思路来源自 EAST, 用来生成 text proposal), IRM (Iterative Refinement Module, 用来解决 long text 难检测的问题, 可以使用一次或多次), SEM(Shape Expression Module, 用来解决arbitrary-shape text 难检测的问题). 三个分支都引出独立的损失函数, 其中 DR 的 loss 包含分割 loss 和回归 loss; IRM 的 loss 只有回归 loss; SEM 的 loss 包含分割 loss 和回归 loss. 注: IRM 和 SEM 都用到了 ROI transform layer, 这是一种与 ROI Pooling 和 ROI Align 功能类似的网络层, 出自 TextNet, 没有细看.


## LOMO 的结构
![](<[2019 CVPR] Look More Than Once_ An Accurate Detector for Text of Arbitrary Shapes/lomo_arch.png>)

> In order to settle the two problems above (注: long text 和 irregular text 的检测问题), we introduce two modules namely iterative refinement module (IRM) and shape expression module (SEM) based on an improved one-shot text detector namely direct regressor (DR) which adopts the direct regression manner. With IRM and SEM integrated, the proposed architecture of LOMO can be trained in an end-to-end fashion.

> For long text instances, the DR generates text proposals firstly, then IRM refines the quadrangle proposals neatly close to ground truth by regressing the coordinate offsets once or more times.

> For irregular text, the representation with four corner coordinates struggles with giving precise estimations of the geometry properties and may include large background area. Inspired by Mask R-CNN and TextSnake, SEM regresses the geometry attributes of text instances, i.e., text region, text center line and corresponding border offsets. Using these properties, SEM can reconstruct a more precise polygon expression. SEM can effectively fit text of arbitrary shapes, i.e., those in horizontal, multi-oriented, curved and wavy forms.



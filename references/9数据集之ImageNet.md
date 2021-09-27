# ImageNet 
The ImageNet Large Scale Visual Recognition Challenge (ILSVRC)

ImageNet is a dataset of over 15 million labeled high-resolution images belonging to roughly 22,000 categories.

- 子集
    - ImageNet-1K: 1.28 million images and 1000 classes. Each image has a single label. 50K validation images.
    - ImageNet-5K
    - ImageNet-22K: 14.2 million images and 21k classes organized by the WordNet hierarchy. Images may contain multiple labels.

**References**:
- http://www.image-net.org/
- [2015 IJCV] ImageNet Large Scale Visual Recognition Challenge


## ILSVRC 2012
ILSVRC 2012 uses a subset of ImageNet with roughly 1000 images in each of 1000 categories. In all, there are roughly 1.2 million training images, 50,000 validation images, and 150,000 testing images.

- http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_test.tar
- http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_val.tar
- http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_train.tar
- http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_devkit_t12.tar
- http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_bbox_train_v2.tar


## ILSVRC 2014
The ILSVRC 2014 classification challenge involves the task of classifying the image into one of 1000 leaf-node categories in the ImageNet hierarchy. There are about 1.2 million images for training, 50,000 for validation and 100,000 images for testing. Each image is associated with one ground truth category, and performance is measured based on the highest scoring classifier predictions. Two numbers are usually reported: the top-1 accuracy rate, which compares the ground truth against the first predicted class, and the top-5 error rate, which compares the ground truth against the first 5 predicted classes: an image is deemed correctly classified if the ground truth is among the top-5, regardless of its rank in them.


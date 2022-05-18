## iNat 2017 (FGVC4 workshop at CVPR 2017)
---
Super-Class             | Class | Train   | Val    | BBoxes
------------------------|-------|---------|--------|--------
Plantae 植物界          | 2,101 | 158,407 | 38,206 | -
Insecta 昆虫纲          | 1,021 | 100,479 | 18,076 | 125,679
Aves 鸟纲               |   964 | 214,295 | 21,226 | 311,669
Reptilia 爬行纲         |   289 |  35,201 |  5,680 |  42,351
Mammalia 哺乳纲         |   186 |  29,333 |  3,490 |  35,222
Fungi 真菌              |   121 |   5,826 |  1,780 | -
Amphibia 两栖纲         |   115 |  15,318 |  2,385 |  18,281
Mollusca 软体动物门     |    93 |   7,536 |  1,841 |  10,821
Animalia 动物界         |    77 |   5,228 |  1,362 |   8,536
Arachnida 蛛形纲        |    56 |   4,873 |  1,086 |   5,826
Actinopterygii 辐鳍鱼纲 |    53 |   1,982 |    637 |   3,382
Chromista 假菌界        |     9 |     398 |    144 | -
Protozoa 原生动物门     |     4 |     308 |     73 | -
Total                   | 5,089 | 579,184 | 95,986 | 561,767

### iNat2017 标注框

| Super Category | Train Boxes  | Val Boxes |
|----------------|--------------|-----------|
| Insecta        | 106,304      |16,732     |
| Aves           | 283,931      |17,314     |
| Reptilia       | 36,476       |5,480      |
| Mammalia       | 31,109       |2,654      |
| Amphibia       | 15,812       |2,280      |
| Mollusca       | 8,566        |1,571      |
| Animalia       | 6,643        |1,143      |
| Arachnida      | 4,752        |1,051      |
| Actinopterygii | 2,571        |511        |
| Total          | 496,164      |48,736     |


**References**:
- [2018] The iNaturalist Species Classification and Detection Dataset
- https://github.com/visipedia/inat_comp/tree/master/2017
- https://www.kaggle.com/competitions/inaturalist-challenge-at-fgvc-2017


## iNat 2018 (FGVC5 workshop at CVPR 2018)
---

There are a total of 8,142 species in the dataset, with 437,513 training images, 24,426 validation images, and 149,394 test images.

| Super Category   | Category Count   | Train Images | Val Images |
|------------------|------------------|--------------|------------|
| Plantae          | 2,917            | 118,800      |8,751       |
| Insecta          | 2,031            | 87,192       |6,093       |
| Aves             | 1,258            | 143,950      |3,774       |
| Actinopterygii   | 369              | 7,835        |1,107       |
| Fungi            | 321              | 6,864        |963         |
| Reptilia         | 284              | 22,754       |852         |
| Mollusca         | 262              | 8,007        |786         |
| Mammalia         | 234              | 20,104       |702         |
| Animalia         | 178              | 5,966        |534         |
| Amphibia         | 144              | 11,156       |432         |
| Arachnida        | 114              | 4,037        |342         |
| Chromista        | 25               | 621          |75          |
| Protozoa         | 4                | 211          |12          |
| Bacteria         | 1                | 16           |3           |
| Total            | 8,142            | 437,513      |24,426      |

**References**:
- https://github.com/visipedia/inat_comp/tree/master/2018
- https://www.kaggle.com/competitions/inaturalist-2018


## iNat 2019 (FGVC6 workshop at CVPR 2019)
---
> There are a total of 1,010 species in the dataset, spanning 72 genera, with a combined training and validation set of 268,243 images. The dataset was constructed such that each genera contains at least 10 species, making the dataset inherently fine-grained. 

**References**:
- https://github.com/visipedia/inat_comp/tree/master/2019


## Semi-iNat 2020 (FGVC7 workshop at CVPR 2020)
---
> We first selected 1000 Aves (birds) species from 1258 Aves taxa included in the iNat-2018 challenge [2]. From the 1000 species, we selected 200 species as in-class and 800 species as out-of-class categories.
> 
> For in-class categories, we selected 3,959 images as labeled data ($L_{in}$) and the remaining 26,640 images as in-class unlabeled data ($U_{in}$). We ensure that each class has at least 5 labeled images. However, due to the natural class imbalance in the original data the ratio of labeled and unlabeled images varies across categories. The out-of-class unlabeled data ($U_{out}$) are from the remaining 800 bird species.
> 
> First, most of the teams found pseudo-labeling on in-class unlabeled data to be the most effective. State-of-the art methods such as MixMatch [8] or FixMatch [20] were not widely used, or were reported to not provide significant improvement. Most teams found that there is less benefit from using out-of-class unlabeled data, while one team reported using clustering labels for pre-training is better than only using ImageNet pre-trained model [12]. This was surprising to us as the out-of-class data is similar in domain. Overall, general tricks for image classification such as extensive data augmentation and ensembles were most useful.

**References**:
- https://www.kaggle.com/competitions/semi-inat-2020
- https://github.com/cvl-umass/semi-inat-2020
- [2021] The Semi-Supervised iNaturalist-Aves Challenge at FGVC7 Workshop


## iNat 2021 (FGVC8 workshop at CVPR 2021)
---

> There is a total of 10,000 species in the dataset. The full training dataset contains nearly 2.7M images. To make the dataset more accessible we have also created a "mini" training dataset with 50 examples per species for a total of 500K images. Each species has 10 validation images. There are a total of 500,000 test images. 

| Super Category    | Species Count | Train Images  | Train Mini Images | Val Images | Test Images |
|-------------------|---------------|---------------|-------------------|------------|-------------|
| Plants            | 4,271         | 1,148,702     | 213,550           |42,710      | x           |
| Insects           | 2,526         | 663,682       | 126,300           |25,260      | x           |
| Birds             | 1,486         | 414,847       | 74,300            |14,860      | x           |
| Fungi             | 341           | 90,048        | 17,050            |3,410       | x           |
| Reptiles          | 313           | 86,830        | 15,650            |3,130       | x           |
| Mammals           | 246           | 68,917        | 12,300            |2,460       | x           |
| Ray-finned Fishes | 183           | 45,166        | 9,150             |1,830       | x           |
| Amphibians        | 170           | 46,252        | 8,500             |1,700       | x           |
| Mollusks          | 169           | 44,670        | 8,450             |1,690       | x           |
| Arachnids         | 153           | 40,687        | 7,650             |1,530       | x           |
| Animalia          | 142           | 37,042        | 7,100             |1,420       | x           |
| Total             | 10,000        | 2,686,843     | 500,000           |100,000     | 500,000     |

**References**:
- https://github.com/visipedia/inat_comp/tree/master/2021
- https://www.kaggle.com/competitions/inaturalist-2021


## Semi-iNat 2021 (FGVC8 workshop at CVPR 2021)
----
**References**:
- https://www.kaggle.com/competitions/semi-inat-2021
- https://github.com/cvl-umass/semi-inat-2021
  

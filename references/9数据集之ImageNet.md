# ImageNet 
The ImageNet Large Scale Visual Recognition Challenge (ILSVRC)

ImageNet is a dataset of over 15 million labeled high-resolution images belonging to roughly 22,000 categories.

- ImageNet-1K: **1.28 million** images and 1000 classes. Each image has a single label. **50K** validation images.
- ImageNet-5K
- ImageNet-21K: **14.2 million** images and 21k classes organized by the WordNet hierarchy. Images may contain multiple labels.

**the ImageNet-21K dataset and ImageNet-22K are the same dataset, and the names have changed due to differences in understanding.**


**References**:
- http://www.image-net.org/
- [2015 IJCV] ImageNet Large Scale Visual Recognition Challenge


## ILSVRC 2012
---
ILSVRC 2012 uses a subset of ImageNet with roughly 1000 images in each of 1000 categories. In all, there are roughly 1.2 million training images, 50,000 validation images, and 150,000 testing images.

- http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_test.tar
- http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_val.tar
- http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_train.tar
- http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_devkit_t12.tar
- http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_bbox_train_v2.tar


## ILSVRC 2014
----
> The ILSVRC 2014 classification challenge involves the task of classifying the image into one of 1000 leaf-node categories in the ImageNet hierarchy. There are about 1.2 million images for training, 50,000 for validation and 100,000 images for testing. Each image is associated with one ground truth category, and performance is measured based on the highest scoring classifier predictions. Two numbers are usually reported: the top-1 accuracy rate, which compares the ground truth against the first predicted class, and the top-5 error rate, which compares the ground truth against the first 5 predicted classes: an image is deemed correctly classified if the ground truth is among the top-5, regardless of its rank in them.

## ImageNet21K
---
- https://image-net.org/data/winter21_whole.tar.gz
    - MD5: ab313ce03179fd803a401b02c651c0a2

## cleaned-up ReaL labels
---
对 ILSVRC2012 ImageNet 的标签进行了清洗.

- [2020] Are we done with ImageNet?

## [2019] ImageNet-V2, ImageNetV2
---
- [2019] Do imagenet classifiers generalize to imagenet

## [2021 CVPR] Re-labeling imagenet: from single to multi-labels, from global to localized labels
----

## [2021] ImageNet-21K-P 
----
- [2021] ImageNet-21K Pretraining for the Masses
- https://image-net.org/data/imagenet21k_resized.tar.gz
    - MD5: c314e95f17e357b3e9cbf0a18ef7ecd6
- https://github.com/Alibaba-MIIL/ImageNet21K

## ImageNet-Sketch
---

## ImageNet-A
---

## ImageNet-R
---

## ImageNet 2012 同义词表中文翻译
---
- ImageNet 2012 中文标签（Chinese Labels）
    - https://blog.csdn.net/haoji007/article/details/76782642
- ImageNet图像库1000个类别名称（中文注释不断更新）
    - https://blog.csdn.net/weixin_41770169/article/details/80482942
- ImageNet2012数据集中英文标签对照
    - https://www.cnblogs.com/cpxlll/p/13493247.html
- lajifenlei
    - https://github.com/hongchongqin/lajifenlei/tree/master
    
```
n01440764 tench, Tinca tinca
          丁鱥, 欧洲丁鱥, 丁桂鱼, 须鱼岁; Animal, Fish
          https://baike.baidu.com/item/丁鱥/7233884 
n01443537 goldfish, Carassius auratus
          金鱼, 金鲫鱼; Animal, Fish
          https://baike.baidu.com/item/金鱼/32862 
n01484850 great white shark, white shark, man-eater, man-eating shark, Carcharodon carcharias
          大白鲨, 噬人鲨; Animal, Fish
          https://baike.baidu.com/item/噬人鲨/40175 
n01491361 tiger shark, Galeocerdo cuvieri
          虎鲨, 鼬鲨; Animal, Fish
          https://baike.baidu.com/item/鼬鲨/1976141 
n01494475 hammerhead, hammerhead shark
          双髻鲨, 锤头鲨; Animal, Fish
          https://baike.baidu.com/item/双髻鲨/4702759 
n01496331 electric ray, crampfish, numbfish, torpedo
          电鳐
n01498041 stingray
          黄貂鱼
n01514668 cock
          公鸡
n01514859 hen
          母鸡
n01518878 ostrich, Struthio camelus
          鸵鸟
n01530575 brambling, Fringilla montifringilla
          燕雀
n01531178 goldfinch, Carduelis carduelis
          金翅雀
n01532829 house finch, linnet, Carpodacus mexicanus
          家朱雀
n01534433 junco, snowbird
          灯芯草雀
n01537544 indigo bunting, indigo finch, indigo bird, Passerina cyanea
          靛蓝雀,靛蓝鸟
n01558993 robin, American robin, Turdus migratorius
          蓝鹀
n01560419 bulbul
          夜莺
n01580077 jay
          松鸦
n01582220 magpie
          喜鹊
n01592084 chickadee
          山雀
n01601694 water ouzel, dipper
          河鸟
n01608432 kite
          鸢
n01614925 bald eagle, American eagle, Haliaeetus leucocephalus
          秃头鹰
n01616318 vulture
          秃鹫
n01622779 great grey owl, great gray owl, Strix nebulosa
          大灰猫头鹰
n01629819 European fire salamander, Salamandra salamandra
          欧洲火蝾螈
n01630670 common newt, Triturus vulgaris
          普通蝾螈
n01631663 eft
          水蜥
n01632458 spotted salamander, Ambystoma maculatum
          斑点蝾螈
n01632777 axolotl, mud puppy, Ambystoma mexicanum
          蝾螈,泥狗
n01641577 bullfrog, Rana catesbeiana
          牛蛙
n01644373 tree frog, tree-frog
          树蛙
n01644900 tailed frog, bell toad, ribbed toad, tailed toad, Ascaphus trui
          尾蛙,铃蟾蜍,肋蟾蜍,尾蟾蜍
n01664065 loggerhead, loggerhead turtle, Caretta caretta
          红海龟
n01665541 leatherback turtle, leatherback, leathery turtle, Dermochelys coriacea
          皮革龟
n01667114 mud turtle
          泥龟
n01667778 terrapin
          淡水龟
n01669191 box turtle, box tortoise
          箱龟
n01675722 banded gecko
          带状壁虎
n01677366 common iguana, iguana, Iguana iguana
          普通鬣蜥
n01682714 American chameleon, anole, Anolis carolinensis
          美国变色龙
n01685808 whiptail, whiptail lizard
          鞭尾蜥蜴
n01687978 agama
          飞龙科蜥蜴
n01688243 frilled lizard, Chlamydosaurus kingi
          褶边蜥蜴
n01689811 alligator lizard
          鳄鱼蜥蜴
n01692333 Gila monster, Heloderma suspectum
          毒蜥
n01693334 green lizard, Lacerta viridis
          绿蜥蜴
n01694178 African chameleon, Chamaeleo chamaeleon
          非洲变色龙
n01695060 Komodo dragon, Komodo lizard, dragon lizard, giant lizard, Varanus komodoensis
          科莫多蜥蜴
n01697457 African crocodile, Nile crocodile, Crocodylus niloticus
          非洲鳄,尼罗河鳄鱼
n01698640 American alligator, Alligator mississipiensis
          美国鳄鱼,鳄鱼
n01704323 triceratops
          三角龙
n01728572 thunder snake, worm snake, Carphophis amoenus
          雷蛇,蠕虫蛇
n01728920 ringneck snake, ring-necked snake, ring snake
          环蛇,环颈蛇
n01729322 hognose snake, puff adder, sand viper
          希腊蛇
n01729977 green snake, grass snake
          绿蛇,草蛇
n01734418 king snake, kingsnake
          国王蛇
n01735189 garter snake, grass snake
          袜带蛇,草蛇
n01737021 water snake
          水蛇
n01739381 vine snake
          藤蛇
n01740131 night snake, Hypsiglena torquata
          夜蛇
n01742172 boa constrictor, Constrictor constrictor
          大蟒蛇
n01744401 rock python, rock snake, Python sebae
          岩石蟒蛇,岩蛇,蟒蛇
n01748264 Indian cobra, Naja naja
          印度眼镜蛇
n01749939 green mamba
          绿曼巴
n01751748 sea snake
          海蛇
n01753488 horned viper, cerastes, sand viper, horned asp, Cerastes cornutus
          角腹蛇
n01755581 diamondback, diamondback rattlesnake, Crotalus adamanteus
          菱纹响尾蛇
n01756291 sidewinder, horned rattlesnake, Crotalus cerastes
          角响尾蛇
n01768244 trilobite
          三叶虫
n01770081 harvestman, daddy longlegs, Phalangium opilio
          盲蜘蛛
n01770393 scorpion
          蝎子
n01773157 black and gold garden spider, Argiope aurantia
          黑金花园蜘蛛
n01773549 barn spider, Araneus cavaticus
          谷仓蜘蛛
n01773797 garden spider, Aranea diademata
          花园蜘蛛
n01774384 black widow, Latrodectus mactans
          黑寡妇蜘蛛
n01774750 tarantula
          狼蛛
n01775062 wolf spider, hunting spider
          狼蜘蛛,狩猎蜘蛛
n01776313 tick
          壁虱
n01784675 centipede
          蜈蚣
n01795545 black grouse
          黑松鸡
n01796340 ptarmigan
          松鸡,雷鸟
n01797886 ruffed grouse, partridge, Bonasa umbellus
          披肩鸡,披肩榛鸡
n01798484 prairie chicken, prairie grouse, prairie fowl
          草原鸡,草原松鸡
n01806143 peacock
          孔雀
n01806567 quail
          鹌鹑
n01807496 partridge
          鹧鸪
n01817953 African grey, African gray, Psittacus erithacus
          非洲灰鹦鹉
n01818515 macaw
          金刚鹦鹉
n01819313 sulphur-crested cockatoo, Kakatoe galerita, Cacatua galerita
          硫冠鹦鹉
n01820546 lorikeet
          短尾鹦鹉
n01824575 coucal
          褐翅鸦鹃
n01828970 bee eater
          蜜蜂
n01829413 hornbill
          犀鸟
n01833805 hummingbird
          蜂鸟
n01843065 jacamar
          鹟䴕
n01843383 toucan
          犀鸟
n01847000 drake
          野鸭
n01855032 red-breasted merganser, Mergus serrator
          红胸秋沙鸭
n01855672 goose
          鹅
n01860187 black swan, Cygnus atratus
          黑天鹅
n01871265 tusker
          大象
n01872401 echidna, spiny anteater, anteater
          针鼹鼠
n01873310 platypus, duckbill, duckbilled platypus, duck-billed platypus, Ornithorhynchus anatinus
          鸭嘴兽
n01877812 wallaby, brush kangaroo
          沙袋鼠
n01882714 koala, koala bear, kangaroo bear, native bear, Phascolarctos cinereus
          考拉,考拉熊
n01883070 wombat
          袋熊
n01910747 jellyfish
          水母
n01914609 sea anemone, anemone
          海葵
n01917289 brain coral
          脑珊瑚
n01924916 flatworm, platyhelminth
          扁形虫扁虫
n01930112 nematode, nematode worm, roundworm
          线虫,蛔虫
n01943899 conch
          海螺
n01944390 snail
          蜗牛
n01945685 slug
          鼻涕虫
n01950731 sea slug, nudibranch
          海参
n01955084 chiton, coat-of-mail shell, sea cradle, polyplacophore
          石鳖
n01968897 chambered nautilus, pearly nautilus, nautilus
          鹦鹉螺
n01978287 Dungeness crab, Cancer magister
          珍宝蟹
n01978455 rock crab, Cancer irroratus
          石蟹
n01980166 fiddler crab
          招潮蟹
n01981276 king crab, Alaska crab, Alaskan king crab, Alaska king crab, Paralithodes camtschatica
          帝王蟹,阿拉斯加蟹,阿拉斯加帝王蟹
n01983481 American lobster, Northern lobster, Maine lobster, Homarus americanus
          美国龙虾,缅因州龙虾
n01984695 spiny lobster, langouste, rock lobster, crawfish, crayfish, sea crawfish
          大螯虾
n01985128 crayfish, crawfish, crawdad, crawdaddy
          小龙虾
n01986214 hermit crab
          寄居蟹
n01990800 isopod
          等足目动物(明虾和螃蟹近亲)
n02002556 white stork, Ciconia ciconia
          白鹳
n02002724 black stork, Ciconia nigra
          黑鹳
n02006656 spoonbill
          鹭
n02007558 flamingo
          火烈鸟
n02009229 little blue heron, Egretta caerulea
          小蓝鹭
n02009912 American egret, great white heron, Egretta albus
          美国鹭,大白鹭
n02011460 bittern
          麻鸦
n02012849 crane
          鹤
n02013706 limpkin, Aramus pictus
          秧鹤
n02017213 European gallinule, Porphyrio porphyrio
          欧洲水鸡,紫水鸡
n02018207 American coot, marsh hen, mud hen, water hen, Fulica americana
          沼泽泥母鸡,水母鸡
n02018795 bustard
          鸨
n02025239 ruddy turnstone, Arenaria interpres
          红翻石鹬
n02027492 red-backed sandpiper, dunlin, Erolia alpina
          红背鹬,黑腹滨鹬
n02028035 redshank, Tringa totanus
          红脚鹬
n02033041 dowitcher
          半蹼鹬
n02037110 oystercatcher, oyster catcher
          蛎鹬
n02051845 pelican
          鹈鹕
n02056570 king penguin, Aptenodytes patagonica
          国王企鹅
n02058221 albatross, mollymawk
          信天翁,大海鸟
n02066245 grey whale, gray whale, devilfish, Eschrichtius gibbosus, Eschrichtius robustus
          灰鲸
n02071294 killer whale, killer, orca, grampus, sea wolf, Orcinus orca
          杀人鲸,逆戟鲸,虎鲸
n02074367 dugong, Dugong dugon
          海牛
n02077923 sea lion
          海狮
n02085620 Chihuahua
          奇瓦瓦
n02085782 Japanese spaniel
          日本猎犬
n02085936 Maltese dog, Maltese terrier, Maltese
          马尔济斯犬
n02086079 Pekinese, Pekingese, Peke
          狮子狗
n02086240 Shih-Tzu
          西施犬
n02086646 Blenheim spaniel
          布莱尼姆猎犬
n02086910 papillon
          巴比狗
n02087046 toy terrier
          玩具犬
n02087394 Rhodesian ridgeback
          罗得西亚长背猎狗
n02088094 Afghan hound, Afghan
          阿富汗猎犬
n02088238 basset, basset hound
          猎犬
n02088364 beagle
          比格犬,猎兔犬
n02088466 bloodhound, sleuthhound
          侦探犬
n02088632 bluetick
          蓝色快狗
n02089078 black-and-tan coonhound
          黑褐猎浣熊犬
n02089867 Walker hound, Walker foxhound
          沃克猎犬
n02089973 English foxhound
          英国猎狐犬
n02090379 redbone
          美洲赤狗
n02090622 borzoi, Russian wolfhound
          俄罗斯猎狼犬
n02090721 Irish wolfhound
          爱尔兰猎狼犬
n02091032 Italian greyhound
          意大利灰狗
n02091134 whippet
          惠比特犬
n02091244 Ibizan hound, Ibizan Podenco
          依比沙猎犬
n02091467 Norwegian elkhound, elkhound
          挪威猎犬
n02091635 otterhound, otter hound
          奥达猎犬,水獭猎犬
n02091831 Saluki, gazelle hound
          沙克犬,瞪羚猎犬
n02092002 Scottish deerhound, deerhound
          苏格兰猎鹿犬,猎鹿犬
n02092339 Weimaraner
          威玛猎犬
n02093256 Staffordshire bullterrier, Staffordshire bull terrier
          斯塔福德郡牛头梗,斯塔福德郡斗牛梗
n02093428 American Staffordshire terrier, Staffordshire terrier, American pit bull terrier, pit bull terrier
          美国斯塔福德郡梗,美国比特斗牛梗,斗牛梗
n02093647 Bedlington terrier
          贝德灵顿梗
n02093754 Border terrier
          边境梗
n02093859 Kerry blue terrier
          凯丽蓝梗
n02093991 Irish terrier
          爱尔兰梗
n02094114 Norfolk terrier
          诺福克梗
n02094258 Norwich terrier
          诺维奇梗
n02094433 Yorkshire terrier
          约克郡梗
n02095314 wire-haired fox terrier
          刚毛猎狐梗
n02095570 Lakeland terrier
          莱克兰梗
n02095889 Sealyham terrier, Sealyham
          锡利哈姆梗
n02096051 Airedale, Airedale terrier
          艾尔谷犬
n02096177 cairn, cairn terrier
          凯恩梗
n02096294 Australian terrier
          澳大利亚梗
n02096437 Dandie Dinmont, Dandie Dinmont terrier
          丹迪丁蒙梗
n02096585 Boston bull, Boston terrier
          波士顿梗
n02097047 miniature schnauzer
          迷你雪纳瑞犬
n02097130 giant schnauzer
          巨型雪纳瑞犬
n02097209 standard schnauzer
          标准雪纳瑞犬
n02097298 Scotch terrier, Scottish terrier, Scottie
          苏格兰梗
n02097474 Tibetan terrier, chrysanthemum dog
          西藏梗,菊花狗
n02097658 silky terrier, Sydney silky
          丝毛梗
n02098105 soft-coated wheaten terrier
          软毛麦色梗
n02098286 West Highland white terrier
          西高地白梗
n02098413 Lhasa, Lhasa apso
          拉萨阿普索犬
n02099267 flat-coated retriever
          平毛寻回犬
n02099429 curly-coated retriever
          卷毛寻回犬
n02099601 golden retriever
          金毛猎犬
n02099712 Labrador retriever
          拉布拉多猎犬
n02099849 Chesapeake Bay retriever
          乞沙比克猎犬
n02100236 German short-haired pointer
          德国短毛猎犬
n02100583 vizsla, Hungarian pointer
          维兹拉犬
n02100735 English setter
          英国谍犬
n02100877 Irish setter, red setter
          爱尔兰雪达犬,红色猎犬
n02101006 Gordon setter
          戈登雪达犬
n02101388 Brittany spaniel
          布列塔尼犬猎犬
n02101556 clumber, clumber spaniel
          黄毛,黄毛猎犬
n02102040 English springer, English springer spaniel
          英国史宾格犬
n02102177 Welsh springer spaniel
          威尔士史宾格犬
n02102318 cocker spaniel, English cocker spaniel, cocker
          可卡犬,英国可卡犬
n02102480 Sussex spaniel
          萨塞克斯猎犬
n02102973 Irish water spaniel
          爱尔兰水猎犬
n02104029 kuvasz
          哥威斯犬
n02104365 schipperke
          舒柏奇犬
n02105056 groenendael
          比利时牧羊犬
n02105162 malinois
          马里努阿犬
n02105251 briard
          伯瑞犬
n02105412 kelpie
          凯尔皮犬
n02105505 komondor
          匈牙利牧羊犬
n02105641 Old English sheepdog, bobtail
          老英国牧羊犬
n02105855 Shetland sheepdog, Shetland sheep dog, Shetland
          喜乐蒂牧羊犬
n02106030 collie
          牧羊犬
n02106166 Border collie
          边境牧羊犬
n02106382 Bouvier des Flandres, Bouviers des Flandres
          法兰德斯牧牛狗
n02106550 Rottweiler
          罗特韦尔犬
n02106662 German shepherd, German shepherd dog, German police dog, alsatian
          德国牧羊犬,德国警犬,阿尔萨斯
n02107142 Doberman, Doberman pinscher
          多伯曼犬,杜宾犬
n02107312 miniature pinscher
          迷你杜宾犬
n02107574 Greater Swiss Mountain dog
          大瑞士山地犬
n02107683 Bernese mountain dog
          伯恩山犬
n02107908 Appenzeller
          Appenzeller狗
n02108000 EntleBucher
          EntleBucher狗
n02108089 boxer
          拳师狗
n02108422 bull mastiff
          斗牛獒
n02108551 Tibetan mastiff
          藏獒
n02108915 French bulldog
          法国斗牛犬
n02109047 Great Dane
          大丹犬
n02109525 Saint Bernard, St Bernard
          圣伯纳德狗
n02109961 Eskimo dog, husky
          爱斯基摩犬,哈士奇
n02110063 malamute, malemute, Alaskan malamute
          雪橇犬,阿拉斯加爱斯基摩狗
n02110185 Siberian husky
          哈士奇
n02110341 dalmatian, coach dog, carriage dog
          达尔马提亚,教练车狗
n02110627 affenpinscher, monkey pinscher, monkey dog
          狮毛狗
n02110806 basenji
          巴辛吉狗
n02110958 pug, pug-dog
          哈巴狗,狮子狗
n02111129 Leonberg
          莱昂贝格狗
n02111277 Newfoundland, Newfoundland dog
          纽芬兰岛狗
n02111500 Great Pyrenees
          大白熊犬
n02111889 Samoyed, Samoyede
          萨摩耶犬
n02112018 Pomeranian
          博美犬
n02112137 chow, chow chow
          松狮,松狮
n02112350 keeshond
          荷兰卷尾狮毛狗
n02112706 Brabancon griffon
          布鲁塞尔格林芬犬
n02113023 Pembroke, Pembroke Welsh corgi
          彭布洛克威尔士科基犬
n02113186 Cardigan, Cardigan Welsh corgi
          威尔士柯基犬
n02113624 toy poodle
          玩具贵宾犬
n02113712 miniature poodle
          迷你贵宾犬
n02113799 standard poodle
          标准贵宾犬
n02113978 Mexican hairless
          墨西哥无毛犬
n02114367 timber wolf, grey wolf, gray wolf, Canis lupus
          灰狼
n02114548 white wolf, Arctic wolf, Canis lupus tundrarum
          白狼,北极狼
n02114712 red wolf, maned wolf, Canis rufus, Canis niger
          红太狼,鬃狼,犬犬鲁弗斯
n02114855 coyote, prairie wolf, brush wolf, Canis latrans
          狼,草原狼,刷狼,郊狼
n02115641 dingo, warrigal, warragal, Canis dingo
          澳洲野狗,澳大利亚野犬
n02115913 dhole, Cuon alpinus
          豺
n02116738 African hunting dog, hyena dog, Cape hunting dog, Lycaon pictus
          非洲猎犬,土狼犬
n02117135 hyena, hyaena
          鬣狗
n02119022 red fox, Vulpes vulpes
          红狐狸
n02119789 kit fox, Vulpes macrotis
          沙狐
n02120079 Arctic fox, white fox, Alopex lagopus
          北极狐狸,白狐狸
n02120505 grey fox, gray fox, Urocyon cinereoargenteus
          灰狐狸
n02123045 tabby, tabby cat
          虎斑猫
n02123159 tiger cat
          山猫,虎猫
n02123394 Persian cat
          波斯猫
n02123597 Siamese cat, Siamese
          暹罗猫
n02124075 Egyptian cat
          埃及猫
n02125311 cougar, puma, catamount, mountain lion, painter, panther, Felis concolor
          美洲狮,美洲豹
n02127052 lynx, catamount
          猞猁,山猫
n02128385 leopard, Panthera pardus
          豹子
n02128757 snow leopard, ounce, Panthera uncia
          雪豹
n02128925 jaguar, panther, Panthera onca, Felis onca
          美洲虎
n02129165 lion, king of beasts, Panthera leo
          狮子
n02129604 tiger, Panthera tigris
          老虎
n02130308 cheetah, chetah, Acinonyx jubatus
          猎豹
n02132136 brown bear, bruin, Ursus arctos
          棕熊
n02133161 American black bear, black bear, Ursus americanus, Euarctos americanus
          美洲黑熊
n02134084 ice bear, polar bear, Ursus Maritimus, Thalarctos maritimus
          冰熊,北极熊
n02134418 sloth bear, Melursus ursinus, Ursus ursinus
          懒熊
n02137549 mongoose
          猫鼬
n02138441 meerkat, mierkat
          猫鼬,海猫
n02165105 tiger beetle
          虎甲虫
n02165456 ladybug, ladybeetle, lady beetle, ladybird, ladybird beetle
          瓢虫
n02167151 ground beetle, carabid beetle
          土鳖虫
n02168699 long-horned beetle, longicorn, longicorn beetle
          天牛
n02169497 leaf beetle, chrysomelid
          龟甲虫
n02172182 dung beetle
          粪甲虫
n02174001 rhinoceros beetle
          犀牛甲虫
n02177972 weevil
          象甲
n02190166 fly
          苍蝇
n02206856 bee
          蜜蜂
n02219486 ant, emmet, pismire
          蚂蚁
n02226429 grasshopper, hopper
          蚱蜢
n02229544 cricket
          蟋蟀
n02231487 walking stick, walkingstick, stick insect
          竹节虫
n02233338 cockroach, roach
          蟑螂
n02236044 mantis, mantid
          螳螂
n02256656 cicada, cicala
          蝉
n02259212 leafhopper
          叶蝉
n02264363 lacewing, lacewing fly
          草蜻蛉
n02268443 dragonfly, darning needle, devil's darning needle, sewing needle, snake feeder, snake doctor, mosquito hawk, skeeter hawk
          蜻蜓
n02268853 damselfly
          豆娘,蜻蛉
n02276258 admiral
          优红蛱蝶
n02277742 ringlet, ringlet butterfly
          小环蝴蝶
n02279972 monarch, monarch butterfly, milkweed butterfly, Danaus plexippus
          君主蝴蝶,大斑蝶
n02280649 cabbage butterfly
          菜粉蝶
n02281406 sulphur butterfly, sulfur butterfly
          白蝴蝶
n02281787 lycaenid, lycaenid butterfly
          灰蝶
n02317335 starfish, sea star
          海星
n02319095 sea urchin
          海胆
n02321529 sea cucumber, holothurian
          海参,海黄瓜
n02325366 wood rabbit, cottontail, cottontail rabbit
          野兔
n02326432 hare
          兔
n02328150 Angora, Angora rabbit
          安哥拉兔
n02342885 hamster
          仓鼠
n02346627 porcupine, hedgehog
          刺猬,豪猪,
n02356798 fox squirrel, eastern fox squirrel, Sciurus niger
          黑松鼠
n02361337 marmot
          土拨鼠
n02363005 beaver
          海狸
n02364673 guinea pig, Cavia cobaya
          豚鼠,豚鼠
n02389026 sorrel
          栗色马
n02391049 zebra
          斑马
n02395406 hog, pig, grunter, squealer, Sus scrofa
          猪
n02396427 wild boar, boar, Sus scrofa
          野猪
n02397096 warthog
          疣猪
n02398521 hippopotamus, hippo, river horse, Hippopotamus amphibius
          河马
n02403003 ox
          牛
n02408429 water buffalo, water ox, Asiatic buffalo, Bubalus bubalis
          水牛,亚洲水牛
n02410509 bison
          野牛
n02412080 ram, tup
          公羊
n02415577 bighorn, bighorn sheep, cimarron, Rocky Mountain bighorn, Rocky Mountain sheep, Ovis canadensis
          大角羊,洛矶山大角羊
n02417914 ibex, Capra ibex
          山羊
n02422106 hartebeest
          狷羚
n02422699 impala, Aepyceros melampus
          黑斑羚
n02423022 gazelle
          瞪羚
n02437312 Arabian camel, dromedary, Camelus dromedarius
          阿拉伯单峰骆驼,骆驼
n02437616 llama
          骆驼
n02441942 weasel
          黄鼠狼
n02442845 mink
          水貂
n02443114 polecat, fitch, foulmart, foumart, Mustela putorius
          臭猫
n02443484 black-footed ferret, ferret, Mustela nigripes
          黑足鼬
n02444819 otter
          水獭
n02445715 skunk, polecat, wood pussy
          臭鼬,木猫
n02447366 badger
          獾
n02454379 armadillo
          犰狳
n02457408 three-toed sloth, ai, Bradypus tridactylus
          树懒
n02480495 orangutan, orang, orangutang, Pongo pygmaeus
          猩猩,婆罗洲猩猩
n02480855 gorilla, Gorilla gorilla
          大猩猩
n02481823 chimpanzee, chimp, Pan troglodytes
          黑猩猩
n02483362 gibbon, Hylobates lar
          长臂猿
n02483708 siamang, Hylobates syndactylus, Symphalangus syndactylus
          合趾猿长臂猿,合趾猿
n02484975 guenon, guenon monkey
          长尾猴
n02486261 patas, hussar monkey, Erythrocebus patas
          赤猴
n02486410 baboon
          狒狒
n02487347 macaque
          恒河猴,猕猴
n02488291 langur
          白头叶猴
n02488702 colobus, colobus monkey
          疣猴
n02489166 proboscis monkey, Nasalis larvatus
          长鼻猴
n02490219 marmoset
          狨（美洲产小型长尾猴）
n02492035 capuchin, ringtail, Cebus capucinus
          卷尾猴
n02492660 howler monkey, howler
          吼猴
n02493509 titi, titi monkey
          伶猴
n02493793 spider monkey, Ateles geoffroyi
          蜘蛛猴
n02494079 squirrel monkey, Saimiri sciureus
          松鼠猴
n02497673 Madagascar cat, ring-tailed lemur, Lemur catta
          马达加斯加环尾狐猴,鼠狐猴
n02500267 indri, indris, Indri indri, Indri brevicaudatus
          大狐猴,马达加斯加大狐猴
n02504013 Indian elephant, Elephas maximus
          印度大象,亚洲象
n02504458 African elephant, Loxodonta africana
          非洲象,非洲象
n02509815 lesser panda, red panda, panda, bear cat, cat bear, Ailurus fulgens
          小熊猫
n02510455 giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca
          大熊猫
n02514041 barracouta, snoek
          杖鱼
n02526121 eel
          鳗鱼
n02536864 coho, cohoe, coho salmon, blue jack, silver salmon, Oncorhynchus kisutch
          银鲑,银鲑鱼
n02606052 rock beauty, Holocanthus tricolor
          三色刺蝶鱼
n02607072 anemone fish
          海葵鱼
n02640242 sturgeon
          鲟鱼
n02641379 gar, garfish, garpike, billfish, Lepisosteus osseus
          雀鳝
n02643566 lionfish
          狮子鱼
n02655020 puffer, pufferfish, blowfish, globefish
          河豚
n02666196 abacus
          算盘
n02667093 abaya
          长袍
n02669723 academic gown, academic robe, judge's robe
          学位袍
n02672831 accordion, piano accordion, squeeze box
          手风琴
n02676566 acoustic guitar
          原声吉他
n02687172 aircraft carrier, carrier, flattop, attack aircraft carrier
          航空母舰
n02690373 airliner
          客机
n02692877 airship, dirigible
          飞艇
n02699494 altar
          祭坛
n02701002 ambulance
          救护车
n02704792 amphibian, amphibious vehicle
          水陆两用车
n02708093 analog clock
          模拟时钟
n02727426 apiary, bee house
          蜂房
n02730930 apron
          围裙
n02747177 ashcan, trash can, garbage can, wastebin, ash bin, ash-bin, ashbin, dustbin, trash barrel, trash bin
          垃圾桶
n02749479 assault rifle, assault gun
          攻击步枪,枪
n02769748 backpack, back pack, knapsack, packsack, rucksack, haversack
          背包
n02776631 bakery, bakeshop, bakehouse
          面包店,面包铺,
n02777292 balance beam, beam
          平衡木
n02782093 balloon
          热气球
n02783161 ballpoint, ballpoint pen, ballpen, Biro
          圆珠笔
n02786058 Band Aid
          创可贴
n02787622 banjo
          班卓琴
n02788148 bannister, banister, balustrade, balusters, handrail
          栏杆,楼梯扶手
n02790996 barbell
          杠铃
n02791124 barber chair
          理发师的椅子
n02791270 barbershop
          理发店
n02793495 barn
          牲口棚
n02794156 barometer
          晴雨表
n02795169 barrel, cask
          圆筒
n02797295 barrow, garden cart, lawn cart, wheelbarrow
          园地小车,手推车
n02799071 baseball
          棒球
n02802426 basketball
          篮球
n02804414 bassinet
          婴儿床
n02804610 bassoon
          巴松管,低音管
n02807133 bathing cap, swimming cap
          游泳帽
n02808304 bath towel
          沐浴毛巾
n02808440 bathtub, bathing tub, bath, tub
          浴缸,澡盆
n02814533 beach wagon, station wagon, wagon, estate car, beach waggon, station waggon, waggon
          沙滩车,旅行车
n02814860 beacon, lighthouse, beacon light, pharos
          灯塔
n02815834 beaker
          高脚杯
n02817516 bearskin, busby, shako
          熊皮高帽
n02823428 beer bottle
          啤酒瓶
n02823750 beer glass
          啤酒杯
n02825657 bell cote, bell cot
          钟塔
n02834397 bib
          （小儿用的）围嘴
n02835271 bicycle-built-for-two, tandem bicycle, tandem
          串联自行车,
n02837789 bikini, two-piece
          比基尼
n02840245 binder, ring-binder
          装订册
n02841315 binoculars, field glasses, opera glasses
          双筒望远镜
n02843684 birdhouse
          鸟舍
n02859443 boathouse
          船库
n02860847 bobsled, bobsleigh, bob
          雪橇
n02865351 bolo tie, bolo, bola tie, bola
          饰扣式领带
n02869837 bonnet, poke bonnet
          阔边女帽
n02870880 bookcase
          书橱
n02871525 bookshop, bookstore, bookstall
          书店,书摊
n02877765 bottlecap
          瓶盖
n02879718 bow
          弓箭
n02883205 bow tie, bow-tie, bowtie
          蝴蝶结领结
n02892201 brass, memorial tablet, plaque
          铜制牌位
n02892767 brassiere, bra, bandeau
          奶罩
n02894605 breakwater, groin, groyne, mole, bulwark, seawall, jetty
          防波堤,海堤
n02895154 breastplate, aegis, egis
          铠甲
n02906734 broom
          扫帚
n02909870 bucket, pail
          桶
n02910353 buckle
          扣环
n02916936 bulletproof vest
          防弹背心
n02917067 bullet train, bullet
          动车,子弹头列车
n02927161 butcher shop, meat market
          肉铺,肉菜市场
n02930766 cab, hack, taxi, taxicab
          出租车
n02939185 caldron, cauldron
          大锅
n02948072 candle, taper, wax light
          蜡烛
n02950826 cannon
          大炮
n02951358 canoe
          独木舟
n02951585 can opener, tin opener
          开瓶器,开罐器
n02963159 cardigan
          开衫
n02965783 car mirror
          车镜
n02966193 carousel, carrousel, merry-go-round, roundabout, whirligig
          旋转木马
n02966687 carpenter's kit, tool kit
          木匠的工具包,工具包
n02971356 carton
          纸箱
n02974003 car wheel
          车轮
n02977058 cash machine, cash dispenser, automated teller machine, automatic teller machine, automated teller, automatic teller, ATM
          取款机,自动取款机
n02978881 cassette
          盒式录音带
n02979186 cassette player
          卡带播放器
n02980441 castle
          城堡
n02981792 catamaran
          双体船
n02988304 CD player
          CD播放器
n02992211 cello, violoncello
          大提琴
n02992529 cellular telephone, cellular phone, cellphone, cell, mobile phone
          移动电话,手机
n02999410 chain
          铁链
n03000134 chainlink fence
          围栏
n03000247 chain mail, ring mail, mail, chain armor, chain armour, ring armor, ring armour
          链甲
n03000684 chain saw, chainsaw
          电锯,油锯
n03014705 chest
          箱子
n03016953 chiffonier, commode
          衣柜,洗脸台
n03017168 chime, bell, gong
          编钟,钟,锣
n03018349 china cabinet, china closet
          中国橱柜
n03026506 Christmas stocking
          圣诞袜
n03028079 church, church building
          教堂,教堂建筑
n03032252 cinema, movie theater, movie theatre, movie house, picture palace
          电影院,剧场
n03041632 cleaver, meat cleaver, chopper
          切肉刀,菜刀
n03042490 cliff dwelling
          悬崖屋
n03045698 cloak
          斗篷
n03047690 clog, geta, patten, sabot
          木屐,木鞋
n03062245 cocktail shaker
          鸡尾酒调酒器
n03063599 coffee mug
          咖啡杯
n03063689 coffeepot
          咖啡壶
n03065424 coil, spiral, volute, whorl, helix
          螺旋结构（楼梯）
n03075370 combination lock
          组合锁
n03085013 computer keyboard, keypad
          电脑键盘,键盘
n03089624 confectionery, confectionary, candy store
          糖果,糖果店
n03095699 container ship, containership, container vessel
          集装箱船
n03100240 convertible
          敞篷车
n03109150 corkscrew, bottle screw
          开瓶器,瓶螺杆
n03110669 cornet, horn, trumpet, trump
          短号,喇叭
n03124043 cowboy boot
          牛仔靴
n03124170 cowboy hat, ten-gallon hat
          牛仔帽
n03125729 cradle
          摇篮
n03126707 crane
          起重机
n03127747 crash helmet
          头盔
n03127925 crate
          板条箱
n03131574 crib, cot
          小儿床
n03133878 Crock Pot
          砂锅
n03134739 croquet ball
          槌球
n03141823 crutch
          拐杖
n03146219 cuirass
          胸甲
n03160309 dam, dike, dyke
          大坝,堤防
n03179701 desk
          书桌
n03180011 desktop computer
          台式电脑
n03187595 dial telephone, dial phone
          有线电话
n03188531 diaper, nappy, napkin
          尿布湿
n03196217 digital clock
          数字时钟
n03197337 digital watch
          数字手表
n03201208 dining table, board
          餐桌板
n03207743 dishrag, dishcloth
          抹布
n03207941 dishwasher, dish washer, dishwashing machine
          洗碗机,洗碟机
n03208938 disk brake, disc brake
          盘式制动器
n03216828 dock, dockage, docking facility
          码头,船坞,码头设施
n03218198 dogsled, dog sled, dog sleigh
          狗拉雪橇
n03220513 dome
          圆顶
n03223299 doormat, welcome mat
          门垫,垫子
n03240683 drilling platform, offshore rig
          钻井平台,海上钻井
n03249569 drum, membranophone, tympan
          鼓,乐器,鼓膜
n03250847 drumstick
          鼓槌
n03255030 dumbbell
          哑铃
n03259280 Dutch oven
          荷兰烤箱
n03271574 electric fan, blower
          电风扇,鼓风机
n03272010 electric guitar
          电吉他
n03272562 electric locomotive
          电力机车
n03290653 entertainment center
          电视,电视柜
n03291819 envelope
          信封
n03297495 espresso maker
          浓缩咖啡机
n03314780 face powder
          扑面粉
n03325584 feather boa, boa
          女用长围巾
n03337140 file, file cabinet, filing cabinet
          文件,文件柜,档案柜
n03344393 fireboat
          消防船
n03345487 fire engine, fire truck
          消防车
n03347037 fire screen, fireguard
          火炉栏
n03355925 flagpole, flagstaff
          旗杆
n03372029 flute, transverse flute
          长笛
n03376595 folding chair
          折叠椅
n03379051 football helmet
          橄榄球头盔
n03384352 forklift
          叉车
n03388043 fountain
          喷泉
n03388183 fountain pen
          钢笔
n03388549 four-poster
          有四根帷柱的床
n03393912 freight car
          运货车厢
n03394916 French horn, horn
          圆号,喇叭
n03400231 frying pan, frypan, skillet
          煎锅
n03404251 fur coat
          裘皮大衣
n03417042 garbage truck, dustcart
          垃圾车
n03424325 gasmask, respirator, gas helmet
          防毒面具,呼吸器
n03425413 gas pump, gasoline pump, petrol pump, island dispenser
          汽油泵
n03443371 goblet
          高脚杯
n03444034 go-kart
          卡丁车
n03445777 golf ball
          高尔夫球
n03445924 golfcart, golf cart
          高尔夫球车
n03447447 gondola
          狭长小船
n03447721 gong, tam-tam
          锣
n03450230 gown
          礼服
n03452741 grand piano, grand
          钢琴
n03457902 greenhouse, nursery, glasshouse
          温室,苗圃
n03459775 grille, radiator grille
          散热器格栅
n03461385 grocery store, grocery, food market, market
          杂货店,食品市场
n03467068 guillotine
          断头台
n03476684 hair slide
          小发夹
n03476991 hair spray
          头发喷雾
n03478589 half track
          半履带装甲车
n03481172 hammer
          锤子
n03482405 hamper
          大篮子
n03483316 hand blower, blow dryer, blow drier, hair dryer, hair drier
          手摇鼓风机,吹风机
n03485407 hand-held computer, hand-held microcomputer
          手提电脑
n03485794 handkerchief, hankie, hanky, hankey
          手帕
n03492542 hard disc, hard disk, fixed disk
          硬盘
n03494278 harmonica, mouth organ, harp, mouth harp
          口琴,口风琴
n03495258 harp
          竖琴
n03496892 harvester, reaper
          收割机
n03498962 hatchet
          斧头
n03527444 holster
          手枪皮套
n03529860 home theater, home theatre
          家庭影院
n03530642 honeycomb
          蜂窝
n03532672 hook, claw
          钩爪
n03534580 hoopskirt, crinoline
          衬裙
n03535780 horizontal bar, high bar
          单杠
n03538406 horse cart, horse-cart
          马车
n03544143 hourglass
          沙漏
n03584254 iPod
          iPod
n03584829 iron, smoothing iron
          熨斗
n03590841 jack-o'-lantern
          南瓜灯笼
n03594734 jean, blue jean, denim
          牛仔裤,蓝色牛仔裤
n03594945 jeep, landrover
          吉普车
n03595614 jersey, T-shirt, tee shirt
          运动衫,T恤
n03598930 jigsaw puzzle
          拼图
n03599486 jinrikisha, ricksha, rickshaw
          人力车
n03602883 joystick
          操纵杆
n03617480 kimono
          和服
n03623198 knee pad
          护膝
n03627232 knot
          蝴蝶结
n03630383 lab coat, laboratory coat
          大褂,实验室外套
n03633091 ladle
          长柄勺
n03637318 lampshade, lamp shade
          灯罩
n03642806 laptop, laptop computer
          笔记本电脑
n03649909 lawn mower, mower
          割草机
n03657121 lens cap, lens cover
          镜头盖
n03658185 letter opener, paper knife, paperknife
          开信刀,裁纸刀
n03661043 library
          图书馆
n03662601 lifeboat
          救生艇
n03666591 lighter, light, igniter, ignitor
          点火器,打火机
n03670208 limousine, limo
          豪华轿车
n03673027 liner, ocean liner
          远洋班轮
n03676483 lipstick, lip rouge
          唇膏,口红
n03680355 Loafer
          平底便鞋
n03690938 lotion
          洗剂
n03691459 loudspeaker, speaker, speaker unit, loudspeaker system, speaker system
          扬声器
n03692522 loupe, jeweler's loupe
          放大镜
n03697007 lumbermill, sawmill
          锯木厂
n03706229 magnetic compass
          磁罗盘
n03709823 mailbag, postbag
          邮袋
n03710193 mailbox, letter box
          信箱
n03710637 maillot
          女游泳衣
n03710721 maillot, tank suit
          有肩带浴衣
n03717622 manhole cover
          窨井盖
n03720891 maraca
          沙球（一种打击乐器）
n03721384 marimba, xylophone
          马林巴木琴
n03724870 mask
          面膜
n03729826 matchstick
          火柴
n03733131 maypole
          花柱
n03733281 maze, labyrinth
          迷宫
n03733805 measuring cup
          量杯
n03742115 medicine chest, medicine cabinet
          药箱
n03743016 megalith, megalithic structure
          巨石,巨石结构
n03759954 microphone, mike
          麦克风
n03761084 microwave, microwave oven
          微波炉
n03763968 military uniform
          军装
n03764736 milk can
          奶桶
n03769881 minibus
          迷你巴士
n03770439 miniskirt, mini
          迷你裙
n03770679 minivan
          面包车
n03773504 missile
          导弹
n03775071 mitten
          连指手套
n03775546 mixing bowl
          搅拌钵
n03776460 mobile home, manufactured home
          活动房屋（由汽车拖拉的）
n03777568 Model T
          T型发动机小汽车
n03777754 modem
          调制解调器
n03781244 monastery
          修道院
n03782006 monitor
          显示器
n03785016 moped
          电瓶车
n03786901 mortar
          砂浆
n03787032 mortarboard
          学士
n03788195 mosque
          清真寺
n03788365 mosquito net
          蚊帐
n03791053 motor scooter, scooter
          摩托车
n03792782 mountain bike, all-terrain bike, off-roader
          山地自行车
n03792972 mountain tent
          登山帐
n03793489 mouse, computer mouse
          鼠标,电脑鼠标
n03794056 mousetrap
          捕鼠器
n03796401 moving van
          搬家车
n03803284 muzzle
          口套
n03804744 nail
          钉子
n03814639 neck brace
          颈托
n03814906 necklace
          项链
n03825788 nipple
          乳头（瓶）
n03832673 notebook, notebook computer
          笔记本,笔记本电脑
n03837869 obelisk
          方尖碑
n03838899 oboe, hautboy, hautbois
          双簧管
n03840681 ocarina, sweet potato
          陶笛,卵形笛
n03841143 odometer, hodometer, mileometer, milometer
          里程表
n03843555 oil filter
          滤油器
n03854065 organ, pipe organ
          风琴,管风琴
n03857828 oscilloscope, scope, cathode-ray oscilloscope, CRO
          示波器
n03866082 overskirt
          罩裙
n03868242 oxcart
          牛车
n03868863 oxygen mask
          氧气面罩
n03871628 packet
          包装
n03873416 paddle, boat paddle
          船桨
n03874293 paddlewheel, paddle wheel
          明轮,桨轮
n03874599 padlock
          挂锁,扣锁
n03876231 paintbrush
          画笔
n03877472 pajama, pyjama, pj's, jammies
          睡衣
n03877845 palace
          宫殿
n03884397 panpipe, pandean pipe, syrinx
          排箫,鸣管
n03887697 paper towel
          纸巾
n03888257 parachute, chute
          降落伞
n03888605 parallel bars, bars
          双杠
n03891251 park bench
          公园长椅
n03891332 parking meter
          停车收费表,停车计时器
n03895866 passenger car, coach, carriage
          客车,教练车
n03899768 patio, terrace
          露台,阳台
n03902125 pay-phone, pay-station
          付费电话
n03903868 pedestal, plinth, footstall
          基座,基脚
n03908618 pencil box, pencil case
          铅笔盒
n03908714 pencil sharpener
          卷笔刀
n03916031 perfume, essence
          香水（瓶）
n03920288 Petri dish
          培养皿
n03924679 photocopier
          复印机
n03929660 pick, plectrum, plectron
          拨弦片,拨子
n03929855 pickelhaube
          尖顶头盔
n03930313 picket fence, paling
          栅栏,栅栏
n03930630 pickup, pickup truck
          皮卡,皮卡车
n03933933 pier
          桥墩
n03935335 piggy bank, penny bank
          存钱罐
n03937543 pill bottle
          药瓶
n03938244 pillow
          枕头
n03942813 ping-pong ball
          乒乓球
n03944341 pinwheel
          风车
n03947888 pirate, pirate ship
          海盗船
n03950228 pitcher, ewer
          水罐
n03954731 plane, carpenter's plane, woodworking plane
          木工刨
n03956157 planetarium
          天文馆
n03958227 plastic bag
          塑料袋
n03961711 plate rack
          板架
n03967562 plow, plough
          犁型铲雪机
n03970156 plunger, plumber's helper
          手压皮碗泵
n03976467 Polaroid camera, Polaroid Land camera
          宝丽来相机
n03976657 pole
          电线杆
n03977966 police van, police wagon, paddy wagon, patrol wagon, wagon, black Maria
          警车,巡逻车
n03980874 poncho
          雨披
n03982430 pool table, billiard table, snooker table
          台球桌
n03983396 pop bottle, soda bottle
          充气饮料瓶
n03991062 pot, flowerpot
          花盆
n03992509 potter's wheel
          陶工旋盘
n03995372 power drill
          电钻
n03998194 prayer rug, prayer mat
          祈祷垫,地毯
n04004767 printer
          打印机
n04005630 prison, prison house
          监狱
n04008634 projectile, missile
          炮弹,导弹
n04009552 projector
          投影仪
n04019541 puck, hockey puck
          冰球
n04023962 punching bag, punch bag, punching ball, punchball
          沙包,吊球
n04026417 purse
          钱包
n04033901 quill, quill pen
          羽管笔
n04033995 quilt, comforter, comfort, puff
          被子
n04037443 racer, race car, racing car
          赛车
n04039381 racket, racquet
          球拍
n04040759 radiator
          散热器
n04041544 radio, wireless
          收音机
n04044716 radio telescope, radio reflector
          射电望远镜,无线电反射器
n04049303 rain barrel
          雨桶
n04065272 recreational vehicle, RV, R.V.
          休闲车,房车
n04067472 reel
          卷轴,卷筒
n04069434 reflex camera
          反射式照相机
n04070727 refrigerator, icebox
          冰箱,冰柜
n04074963 remote control, remote
          遥控器
n04081281 restaurant, eating house, eating place, eatery
          餐厅,饮食店,食堂
n04086273 revolver, six-gun, six-shooter
          左轮手枪
n04090263 rifle
          步枪
n04099969 rocking chair, rocker
          摇椅
n04111531 rotisserie
          电转烤肉架
n04116512 rubber eraser, rubber, pencil eraser
          橡皮
n04118538 rugby ball
          橄榄球
n04118776 rule, ruler
          直尺
n04120489 running shoe
          跑步鞋
n04125021 safe
          保险柜
n04127249 safety pin
          安全别针
n04131690 saltshaker, salt shaker
          盐瓶（调味用）
n04133789 sandal
          凉鞋
n04136333 sarong
          纱笼,围裙
n04141076 sax, saxophone
          萨克斯管
n04141327 scabbard
          剑鞘
n04141975 scale, weighing machine
          秤,称重机
n04146614 school bus
          校车
n04147183 schooner
          帆船
n04149813 scoreboard
          记分牌
n04152593 screen, CRT screen
          屏幕
n04153751 screw
          螺丝
n04154565 screwdriver
          螺丝刀
n04162706 seat belt, seatbelt
          安全带
n04179913 sewing machine
          缝纫机
n04192698 shield, buckler
          盾牌,盾牌
n04200800 shoe shop, shoe-shop, shoe store
          皮鞋店,鞋店
n04201297 shoji
          障子
n04204238 shopping basket
          购物篮
n04204347 shopping cart
          购物车
n04208210 shovel
          铁锹
n04209133 shower cap
          浴帽
n04209239 shower curtain
          浴帘
n04228054 ski
          滑雪板
n04229816 ski mask
          滑雪面罩
n04235860 sleeping bag
          睡袋
n04238763 slide rule, slipstick
          滑尺
n04239074 sliding door
          滑动门
n04243546 slot, one-armed bandit
          角子老虎机
n04251144 snorkel
          潜水通气管
n04252077 snowmobile
          雪橇
n04252225 snowplow, snowplough
          扫雪机,扫雪机
n04254120 soap dispenser
          皂液器
n04254680 soccer ball
          足球
n04254777 sock
          袜子
n04258138 solar dish, solar collector, solar furnace
          碟式太阳能,太阳能集热器,太阳能炉
n04259630 sombrero
          宽边帽
n04263257 soup bowl
          汤碗
n04264628 space bar
          空格键
n04265275 space heater
          空间加热器
n04266014 space shuttle
          航天飞机
n04270147 spatula
          铲（搅拌或涂敷用的）
n04273569 speedboat
          快艇
n04275548 spider web, spider's web
          蜘蛛网
n04277352 spindle
          纺锤,纱锭
n04285008 sports car, sport car
          跑车
n04286575 spotlight, spot
          聚光灯
n04296562 stage
          舞台
n04310018 steam locomotive
          蒸汽机车
n04311004 steel arch bridge
          钢拱桥
n04311174 steel drum
          钢滚筒
n04317175 stethoscope
          听诊器
n04325704 stole
          女用披肩
n04326547 stone wall
          石头墙
n04328186 stopwatch, stop watch
          秒表
n04330267 stove
          火炉
n04332243 strainer
          过滤器
n04335435 streetcar, tram, tramcar, trolley, trolley car
          有轨电车,电车
n04336792 stretcher
          担架
n04344873 studio couch, day bed
          沙发床
n04346328 stupa, tope
          佛塔
n04347754 submarine, pigboat, sub, U-boat
          潜艇,潜水艇
n04350905 suit, suit of clothes
          套装,衣服
n04355338 sundial
          日晷
n04355933 sunglass
          太阳镜
n04356056 sunglasses, dark glasses, shades
          太阳镜,墨镜
n04357314 sunscreen, sunblock, sun blocker
          防晒霜,防晒剂
n04366367 suspension bridge
          悬索桥
n04367480 swab, swob, mop
          拖把
n04370456 sweatshirt
          运动衫
n04371430 swimming trunks, bathing trunks
          游泳裤
n04371774 swing
          秋千
n04372370 switch, electric switch, electrical switch
          开关,电器开关
n04376876 syringe
          注射器
n04380533 table lamp
          台灯
n04389033 tank, army tank, armored combat vehicle, armoured combat vehicle
          坦克,装甲战车,装甲战斗车辆
n04392985 tape player
          磁带播放器
n04398044 teapot
          茶壶
n04399382 teddy, teddy bear
          泰迪,泰迪熊
n04404412 television, television system
          电视
n04409515 tennis ball
          网球
n04417672 thatch, thatched roof
          茅草,茅草屋顶
n04418357 theater curtain, theatre curtain
          幕布,剧院的帷幕
n04423845 thimble
          顶针
n04428191 thresher, thrasher, threshing machine
          脱粒机
n04429376 throne
          宝座
n04435653 tile roof
          瓦屋顶
n04442312 toaster
          烤面包机
n04443257 tobacco shop, tobacconist shop, tobacconist
          烟草店,烟草
n04447861 toilet seat
          马桶
n04456115 torch
          火炬
n04458633 totem pole
          图腾柱
n04461696 tow truck, tow car, wrecker
          拖车,牵引车,清障车
n04462240 toyshop
          玩具店
n04465501 tractor
          拖拉机
n04467665 trailer truck, tractor trailer, trucking rig, rig, articulated lorry, semi
          拖车,铰接式卡车
n04476259 tray
          托盘
n04479046 trench coat
          风衣
n04482393 tricycle, trike, velocipede
          三轮车
n04483307 trimaran
          三体船
n04485082 tripod
          三脚架
n04486054 triumphal arch
          凯旋门
n04487081 trolleybus, trolley coach, trackless trolley
          无轨电车
n04487394 trombone
          长号
n04493381 tub, vat
          浴盆,浴缸
n04501370 turnstile
          旋转式栅门
n04505470 typewriter keyboard
          打字机键盘
n04507155 umbrella
          伞
n04509417 unicycle, monocycle
          独轮车
n04515003 upright, upright piano
          直立式钢琴
n04517823 vacuum, vacuum cleaner
          真空吸尘器
n04522168 vase
          花瓶
n04523525 vault
          拱顶
n04525038 velvet
          天鹅绒
n04525305 vending machine
          自动售货机
n04532106 vestment
          祭服
n04532670 viaduct
          高架桥
n04536866 violin, fiddle
          小提琴,小提琴
n04540053 volleyball
          排球
n04542943 waffle iron
          松饼机
n04548280 wall clock
          挂钟
n04548362 wallet, billfold, notecase, pocketbook
          钱包,皮夹
n04550184 wardrobe, closet, press
          衣柜,壁橱
n04552348 warplane, military plane
          军用飞机
n04553703 washbasin, handbasin, washbowl, lavabo, wash-hand basin
          洗脸盆,洗手盆
n04554684 washer, automatic washer, washing machine
          洗衣机,自动洗衣机
n04557648 water bottle
          水瓶
n04560804 water jug
          水壶
n04562935 water tower
          水塔
n04579145 whiskey jug
          威士忌壶
n04579432 whistle
          哨子
n04584207 wig
          假发
n04589890 window screen
          纱窗
n04590129 window shade
          百叶窗
n04591157 Windsor tie
          温莎领带
n04591713 wine bottle
          葡萄酒瓶
n04592741 wing
          飞机翅膀,飞机
n04596742 wok
          炒菜锅
n04597913 wooden spoon
          木制的勺子
n04599235 wool, woolen, woollen
          毛织品,羊绒
n04604644 worm fence, snake fence, snake-rail fence, Virginia fence
          栅栏,围栏
n04606251 wreck
          沉船
n04612504 yawl
          双桅船
n04613696 yurt
          蒙古包
n06359193 web site, website, internet site, site
          网站,互联网网站
n06596364 comic book
          漫画
n06785654 crossword puzzle, crossword
          纵横字谜
n06794110 street sign
          路标
n06874185 traffic light, traffic signal, stoplight
          交通信号灯
n07248320 book jacket, dust cover, dust jacket, dust wrapper
          防尘罩,书皮
n07565083 menu
          菜单
n07579787 plate
          盘子
n07583066 guacamole
          鳄梨酱
n07584110 consomme
          清汤
n07590611 hot pot, hotpot
          罐焖土豆烧肉
n07613480 trifle
          蛋糕
n07614500 ice cream, icecream
          冰淇淋
n07615774 ice lolly, lolly, lollipop, popsicle
          雪糕,冰棍,冰棒
n07684084 French loaf
          法式面包
n07693725 bagel, beigel
          百吉饼
n07695742 pretzel
          椒盐脆饼
n07697313 cheeseburger
          芝士汉堡
n07697537 hotdog, hot dog, red hot
          热狗
n07711569 mashed potato
          土豆泥
n07714571 head cabbage
          结球甘蓝
n07714990 broccoli
          西兰花
n07715103 cauliflower
          菜花
n07716358 zucchini, courgette
          绿皮密生西葫芦
n07716906 spaghetti squash
          西葫芦
n07717410 acorn squash
          小青南瓜
n07717556 butternut squash
          南瓜
n07718472 cucumber, cuke
          黄瓜
n07718747 artichoke, globe artichoke
          朝鲜蓟
n07720875 bell pepper
          甜椒
n07730033 cardoon
          刺棘蓟
n07734744 mushroom
          蘑菇
n07742313 Granny Smith
          绿苹果
n07745940 strawberry
          草莓
n07747607 orange
          橘子
n07749582 lemon
          柠檬
n07753113 fig
          无花果
n07753275 pineapple, ananas
          菠萝
n07753592 banana
          香蕉
n07754684 jackfruit, jak, jack
          菠萝蜜
n07760859 custard apple
          蛋奶冻苹果
n07768694 pomegranate
          石榴
n07802026 hay
          干草
n07831146 carbonara
          烤面条加干酪沙司
n07836838 chocolate sauce, chocolate syrup
          巧克力酱,巧克力糖浆
n07860988 dough
          面团
n07871810 meat loaf, meatloaf
          瑞士肉包,肉饼
n07873807 pizza, pizza pie
          披萨,披萨饼
n07875152 potpie
          馅饼
n07880968 burrito
          卷饼
n07892512 red wine
          红葡萄酒
n07920052 espresso
          意大利浓咖啡
n07930864 cup
          杯子
n07932039 eggnog
          蛋酒
n09193705 alp
          高山
n09229709 bubble
          泡泡
n09246464 cliff, drop, drop-off
          悬崖
n09256479 coral reef
          珊瑚礁
n09288635 geyser
          间歇泉
n09332890 lakeside, lakeshore
          湖边,湖岸
n09399592 promontory, headland, head, foreland
          海角
n09421951 sandbar, sand bar
          沙洲,沙坝
n09428293 seashore, coast, seacoast, sea-coast
          海滨,海岸
n09468604 valley, vale
          峡谷
n09472597 volcano
          火山
n09835506 ballplayer, baseball player
          棒球,棒球运动员
n10148035 groom, bridegroom
          新郎
n10565667 scuba diver
          潜水员
n11879895 rapeseed
          油菜
n11939491 daisy
          雏菊
n12057211 yellow lady's slipper, yellow lady-slipper, Cypripedium calceolus, Cypripedium parviflorum
          杓兰
n12144580 corn
          玉米
n12267677 acorn
          橡子
n12620546 hip, rose hip, rosehip
          玫瑰果
n12768682 buckeye, horse chestnut, conker
          七叶树果实
n12985857 coral fungus
          珊瑚菌
n12998815 agaric
          木耳
n13037406 gyromitra
          鹿花菌
n13040303 stinkhorn, carrion fungus
          鬼笔菌
n13044778 earthstar
          地星
n13052670 hen-of-the-woods, hen of the woods, Polyporus frondosus, Grifola frondosa
          多叶奇果菌
n13054560 bolete
          牛肝菌
n13133613 ear, spike, capitulum
          玉米穗
n15075141 toilet tissue, toilet paper, bathroom tissue
          卫生纸
```
# 图像视频审核 (Image and Video Auditing, IVA)
- 鉴黄: 色情图像
- 鉴暴: 暴力图像
- 鉴恐: 恐怖图像
- 鉴政: 政治敏感图像
- 恶心: 腐烂, 密集, 畸形, 血腥, 蛇, 虫子, 牙齿等
- 不良行为: 打架斗殴, 赌博, 抽烟
- 广告引导类

## 百度图像内容审核
- 百度官方违禁图库：基于百度海量历史数据和政府指令，提供对敏感事件、场景及对监管机构要求封禁图片的识别能力
- 色情识别：检测图中是否包含各类色情违禁、儿童裸露、女性性感等内容
- 暴恐识别：检测图中是否包含暴恐旗帜/人物、警察部队、军事武器等内容
- 旗帜标志识别：检测图片中是否包含国旗、国徽、党旗党徽、警徽、臂章以及反动组织的各类标志
- 政治人物识别：检测图中是否包含政治人物/公众人物的人脸
- 用户头像审核：对图片中人脸的角度、遮挡、占比、清晰度等进行审核，筛选合适作为头像的照片
- 图文审核：检测图片的文字是否包含色情、政治敏感、广告等违禁内容
- 广告检测：检测图片中是否包含水印、二维码、条形码
- 不良场景识别：检测图中是否包含吸烟、饮酒、赌博、吸毒等行为
- 恶心图像识别：检测图片中是否包含病变组织、流血恐怖等恶心内容
- 图像质量检测：对图像的清晰度和美观度进行打分
- 自定义图像黑名单：对用户黑名单中的图片进行拦截
- 自定义图像白名单：对用户白名单中的图片直接放过
- 自定义图片审核-EasyDL：支持用户通过EasyDL自助定制图像分类、物体检测模型，满足个性化审核需求

## 鉴黄

### 鉴黄新闻
- 智能鉴黄争霸，NPDI图片测试集亲测哪家强
    http://www.chinaz.com/news/2016/1103/606011.shtml

### 数据集/项目
- OpenNSFW
    - https://github.com/yahoo/open_nsfw
- nsfw_data_source_urls
    - https://github.com/EBazarov/nsfw_data_source_urls
- nsfw_data_scrapper
    - https://github.com/alexkimxyz/nsfw_data_scrapper
- sfwjs
    - https://github.com/infinitered/nsfwjs
- nsfw-resnet
    - https://github.com/yangbisheng2009/nsfw-resnet


### 类别
- normal (正常)
- hot (性感)
- porn (色情)
    - female-breast
    - female-genital
    - male-genital
    - pubes
    - anus
    - sex

## 市面产品
- 棱镜-图片视频鉴黄
    - https://market.cloud.tencent.com/products/21809
- 易源数据-图片鉴黄与鉴暴恐
    - https://market.cloud.tencent.com/products/9036
- 色情图片识别-极速数据
    - https://market.cloud.tencent.com/products/11701
    
    


头条文本分类
=
分类代码在ipynb文件里
-
上传的是原数据集，整理后的数据集太大无法上传，截图如下
=
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/90304231/150448158-7e4cb6ea-9dda-4fd5-8a80-1f9248835c0f.png">

分类code与名称：
-
100 民生 故事 news_story  101 文化 文化 news_culture  102 娱乐 娱乐 news_entertainment  103 体育 体育 news_sports  104 财经 财经 news_finance  106 房产 房产 news_house  107 汽车 汽车 news_car  108 教育 教育 news_edu   109 科技 科技 news_tech  110 军事 军事 news_military  112 旅游 旅游 news_travel  113 国际 国际 news_world  114 证券 股票 stock  115 农业 三农 news_agriculture  116 电竞 游戏 news_game

现有两种方法进行抖音爬虫，方法一已实现，方法二正在修改代码中
=
1.douyin_spider_web.py
-
是基于selenium对网页版抖音进行数据爬取，运行后首先有60秒的时间手动进行滑块验证，扫码登录，保存cookies后重新打开抖音，开始爬取视频简介和评论。

过程中如果遇到文字验证，会自动退出重进，避免了除滑块验证以外的其他验证。

重新打开后的滑块验证可以自动破解，具体电脑对应的get_offset内数据不同。

2.douyin_spider_app.py
-
 原项目是用appium+python+虚拟机爬取app中出现的广告视频
 
然后是根据jieba对采集的数据进行分词，统计出词频最高的10个词，进行贝叶斯分类
=

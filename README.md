头条分类在ipynb文件里
=
上传的是原数据集，整理后的数据集太大无法上传，截图如下
=
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/90304231/150448158-7e4cb6ea-9dda-4fd5-8a80-1f9248835c0f.png">


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

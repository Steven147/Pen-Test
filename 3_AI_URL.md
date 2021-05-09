# 技术路线三：AI-URL筛选

@尹俊同 @林绍钦
因为比较重要所以单独拉出来成一个文件了，现在服务器环境已经配置好了，以后在vscode中链接服务器，切换python环境，其余使用和本地一致。

## vscode 远程服务器配置

[官方文档 Visual Studio Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview)

链接命令：`ssh contest2021@202.120.39.26 -p 10151`

```
Host zft-contest
    HostName 202.120.39.26
    User contest2021
    Port 10151
```
密码:`**************`

## conda 环境配置

[官方文档 Command reference](https://docs.conda.io/projects/conda/en/latest/commands.html)

<!-- conda 安装：[conda的安装与使用（2020-07-08更新） - 简书](https://www.jianshu.com/p/edaa744ea47d)

[Index of /anaconda/archive/ | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/) -->

<!-- `wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh`

`bash Anaconda3-5.3.1-Linux-x86_64.sh` -->

在shell下启动conda环境：`. ~/anaconda3/bin/activate `

conda env list

conda create --name [env_name] python=3.6

conda activate [env_name]

## tensorflow 学习

[A Survey on Deep Learning: Algorithms, Techniques, and Applications: ACM Computing Surveys: Vol 51, No 5](https://dl.acm.org/doi/abs/10.1145/3234150) 【概述论文：深度学习概览：算法，技术和应用】

[tensorflow-tutorials](https://tensorflow.google.cn/tutorials) 官方教程，兼容性最好，bug最少，质量碾压csdn

[A Neural Network Playground 神经网络可视化](http://playground.tensorflow.org/) 可视化，先来无事可以玩一玩

[[双语字幕]吴恩达深度学习deeplearning.ai_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili](https://www.bilibili.com/video/BV1FT4y1E74V/?spm_id_from=333.788.recommend_more_video.1) 

[Keras 快速搭建神经网络 (莫烦 Python 教程)](https://www.bilibili.com/video/av16910214) keras视频，看不懂代码可以看看

[大白话讲解卷积神经网络工作原理](https://www.bilibili.com/video/av35087157/?spm_id_from=333.788.videocard.0) 全网将卷积讲的最清楚的视频！

## 技术路线实现

> 待补充

<!-- Python 机器学习：https://zhuanlan.zhihu.com/p/112123064
Python 之 Sklearn 使用教程：https://www.jianshu.com/p/6ada34655862

算法总结：
优化算法分类及总结：https://blog.csdn.net/qq997843911/article/details/83445318 -->

<!-- [python 3.x-通过Selenium在Chrome上打开检查（按F12）-代码日志](https://stackoverflow.com/questions/59365968/opening-inspect-pressing-f12-on-chrome-via-selenium)

[java-Selenium Webdriver commit（）vs click（）-代码日志](https://stackoverflow.com/questions/17530104/selenium-webdriver-submit-vs-click)

[The Selenium Browser Automation Project :: Documentation for Selenium](https://www.selenium.dev/documentation/en/)

post方式结合
sqlmap.py -u "http://192.168.160.1/sqltest/post.php" --forms 
或 
sqlmap -u http://xxx.xxx.com/Login.asp --data "n=1&p=1"

sqlmap.py -u "http://localhost:8003/Production/PRODUCT_DETAIL.asp?id=1513"

[Usage · sqlmapproject/sqlmap Wiki](https://github.com/sqlmapproject/sqlmap/wiki/Usage)

[(11条消息) sqlmap之(一)----命令详解_fendo-CSDN博客_sqlmap命令详解](https://blog.csdn.net/u011781521/article/details/53979998)

可注入的url与url自身的特征有关，如参数，单词语义等相关。

因此首先建立规则过滤一些url后，然后用模型检测哪些可能是有漏洞的url，输入给sqlmap。

模型首先需要有一个GroundTruth参考标准数据集，哪些url是无漏洞的，哪些url有漏洞的，各有1000个

通过机器学习如随机森林，建立检测模型。要达到95%以上检测率。

找前辈要现有的技术路线。

- url 特征相关：
面向机器学习的恶意 URL 检测，主要关注提取特征：[用机器学习玩转恶意URL检测 - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/network/131279.html)，技术路线如下：
    
  1. 分别拿到正常请求和恶意请求的数据集。
  2. 对无规律的数据集进行处理得到特征矩阵。
  3. 使用机器逻辑回归方式使用特征矩阵训练检测模型。
  4. 最后计算模型的准确度，并使用检测模型判断未知 URL 请求是恶意的还是正常的。

- 构建 url 样本集的统计学或机器学习模型：[基于机器学习的web异常检测 - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/web/126543.html)
  1. 基于统计学习模型：特征例如，URL参数个数、参数值长度的均值和方差、参数字符分布、URL的访问频率
  2. 基于文本分析的机器学习模型：基于日志文本的分析
  3. 基于单分类模型：学习单类样本的最小边界，边界之外的则识别为异常。
  4. 基于聚类模型： -->

## 数据流程

1. 目标站点根目录
   - `asy_spider.py` 爬取目录
   - 初步规则筛选
2. 网页内容爬取



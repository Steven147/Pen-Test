# AI渗透测试

等级保护-》渗透
（缺乏渗透人员-需求量大）
针对web的适应性框架（完整流程）
带人工智能 自动化
重点不在框架，在方案的实际意义

## 技术路线

1. 基于kali-linux熟练使用渗透工具awvs，sqlmap，metasploit，构思集成方案。
2. 采用机器学习或其他方案实现优化url列表、版本识别。sqlmap
3. 积累poc资源，实现测试方案，分析测试效果。
4. 对专家智能渗透流程进行模拟和评估。（重置 密码：重置密码漏洞）（策略，可累加）（逻辑漏洞）
5. 框架逻辑整合，界面编写
  
<!-- 
GUI搭建与逻辑整合：分级抽象渗透框架的搭建

> 受到xyntax设计思路启发。[01 需求与设计 · Xyntax/POC-T Wiki](https://github.com/Xyntax/POC-T/wiki/01-%E9%9C%80%E6%B1%82%E4%B8%8E%E8%AE%BE%E8%AE%A1)

渗透攻击已经拥有了如此之多的**PoC资源**，以及繁多的**现成框架**，为何还需要我们的框架呢？

首先，所谓PoC，就是一个渗透概念的基础实例。不是将所有PoC整合就是完美的扫描器，而是必须与框架结合，统一使用才能发挥出“量变引起质变”的效果。因此，PoC通常需要一定程度的**基于框架的二次开发**。

现有的框架基本覆盖了渗透测试的所有需求，但每一个框架都有其局限性，所以维护一个**兼容性好**，**扩展潜力强**，并且**开发思路清晰**的框架是有意义的。几乎所有的渗透框架（msf[yes]...）都支持扩展插件，来保证框架的扩展性。框架对插件和模块的调用构成了框架的**实例**。

然而所有框架都存在矛盾，为了保证扩展插件的质量，框架一般会给出复杂的文档格式要求（Pocsuite[yes],msf[unknown]...），格式的限制增加了插件开发的成本，也增加了实例的使用成本。使得一些简易的PoC无法很快的融入框架。

而我们这套框架的优势便在于**覆盖了渗透测试实例的每个级别**。从低到高分别是代码级，专一框架级，多功能框架级，以及最高的OS发行版本级。一般框架所支持的插件与实例都是局限在某一级别。我们的框架（希望实现）对从代码级到多功能框架级的实例都能有较好的支持。

在低层次级，给插件最大的自由度，不需要继承框架中的模块，只需要读取最基本的输入。保证渗透工程师能够高效快速编写测试简易的PoC。
同时在高层次级，不仅能提供高可靠性的模块以及现成框架接口，保证插件的稳定性。在面向非专业用户，高层次的应用插件提供的实例也有足够的易用性。

总结，安全技术人员经常会遇到不同层次的需求，本框架（希望实现）对从代码级到多功能框架级的渗透测试实例都能有较好的支持。安全技术人员在使用本框架进行渗透测试实践的时候，可以根据需求，灵活的选择框架中不同级别的模块和接口，**高效编写**出符合需求的**渗透测试实例**。 -->

<!-- [Penetration test - Wikipedia](https://en.wikipedia.org/wiki/Penetration_test#Specialized_OS_distributions)

- 代码级
- 框架级: 
  - 专一框架、工具级别：Nmap,awvs,
  - 多功能框架：Metasploit Project,（本框架的定位）
- OS发行版本级: Kali Linux based on Debian, -->

<!-- > 根据对框架的分析，可以重新锚定各条技术路线的位置。
> 本项目的技术路线可以概括为搭建分级框架，并且为了验证框架的可扩展性，在框架的不同层级不同部分进行实例化 -->

<!-- **路线1：基于kali-linux熟练使用渗透工具awvs，sqlmap，metasploit，构思集成方案。**：
>【接口实现】为现有的框架与本框架之间编写接口（metasploit等），并且编写框架直接的链接模块
- 分析输入，调用框架，保存输出（awvs[yes]）
- 将输入输出转化为统一格式
  - （扫描报告是否有现成的储存格式？有则）储存为现有数据格式
  - msf 输入格式
    - avws扫描的结果很不完全
    - 新框架都采用深度学习

**路线2：采用机器学习或其他方案实现优化url列表、版本识别。**：
>【AI模块实现】加入、调用机器学习模块。
- 输入URL列表，给出对URL恶意性的猜测评估。筛选URL，xray（非开源）
- （版本识别模块如何通过AI优化？）

**路线3：积累poc资源，实现测试方案，分析测试效果。**
> 【PoC实例化】将已有poc（以及不同来源的poc组）依照本框架进行实例化，同时要实现
- 简易PoC的易移植性，只需要遵守框架最底层的模块限制
- 复杂PoC的可移植性、可靠性，需要实现对高级模块和接口的调用

**路线4：对专家智能渗透流程进行模拟和评估。**
> 【】 -->

### 1. 基于kali-linux熟练使用渗透工具awvs，sqlmap，metasploit，构思集成方案。

[漏扫使用技巧分享：场景不同，结果两极化严重 - 知乎](https://zhuanlan.zhihu.com/p/111875353)
选择漏洞扫描器时需要考虑扫描类型。

- **现有技术一**：论文一：集成和自动化识别工具方法，完整样例。

<!-- 参考文献：1. 渗透测试中信息采集的知识提取与集成 Knowledge Extraction and Integration for Information Gathering in Penetration Testing.docx 

本文回顾和识别开源子域枚举和服务扫描工具，并提出了一种集成和自动化识别工具的方法。 结果表明，由于减少了人工任务，使用我们的方法大大改善了信息收集过程。【本竞赛项目的基本依据以及期望达到的目标】

本研究论文的重点是确定能够收集信息的工具，以便集成这些工具，从而使这些工具的组合输出易于管理、组织和分析。【评价标准】

我们正在审查和识别在识别信息系统的子域和开放端口方面最有效和最有效的子域和服务扫描工具。 然后我们使用shell脚本集成这些工具。 我们将集成工具的结果与独立工具进行比较，以评估我们的信息收集方法的效率和有效性。【技术路线】 -->

- **现有技术二**：[awvs_script_decode](https://github.com/fnmsd/awvs_script_decode)，可针对性的对awvs扫描器进行输入输出测试。

<!-- [gatlindada/awvs-decode: The best and easiest way to decode and repack AWVS scripts. AWVS 最好、最简单、最新的解码/再打包方法，仅15行代码！](https://github.com/gatlindada/awvs-decode) -->

- **现有技术三**：[allfro/pymetasploit](https://github.com/allfro/pymetasploit)，综合python与metasploit

<!-- > 工作概述：论文提供了一条技术路线，可以适当进行复现，并参考论文的分析和对比方法。利用现有对awvs的解码以及pymetasploit库的支持，可以简要实现从搭建broken服务器，到利用awvs针对性的扫描出该漏洞，并使用python的msf接口进行尝试性攻击，最后将信息收集流程、攻击流程以及攻击结果报告集成到gui中。 -->

---

- **目前工作**：搭建并配置有漏洞的web应用程序

> **重要参考：metasploit渗透测试魔鬼训练营**

[渗透测试靶场介绍](https://www.cnblogs.com/cainiao-chuanqi/p/13870199.html)

[enaqx/awesome-pentest](https://github.com/enaqx/awesome-pentest)

<!-- - 环境一：windows XP(vmware) + phpstudy 搭建本地服务器
包含b站视频教程，已失效，保存在本地
[小皮面板(phpstudy) - 让天下没有难配的服务器环境！](https://www.xp.cn/)

[新手指南：手把手教你如何搭建自己的渗透测试环境 - FreeBuf网络安全行业门户](https://www.freebuf.com/sectool/102661.html) -->

- 环境：[digininja/DVWA: Damn Vulnerable Web Application (DVWA)](https://github.com/digininja/DVWA)

[新手指南：DVWA-1.9全级别教程（完结篇，附实例）之XSS - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/web/123779.html)

<!-- 使用PHP语言写的测试平台，要先搭好PHP+MYSQL的环境，把文件直接解压到你的站点根目录。

使用浏览器访问,我的本地环境：[Damn Vulnerable Web Application (DVWA) v1.10](http://10.10.10.130/DVWA)，输入用户名admin，密码password即可登录 -->

推荐新手首选靶场，DVWA的目的是通过简单易用的界面来实践一些最常见的Web漏洞，这些漏洞具有不同的难度，是一个涵盖了多种漏洞一个综合的靶机
<!-- 
- 【参考】 DVWA靶场共有十个模块，分别是

    - Brute Force（暴力（破解））
    - Command Injection（命令行注入） [phpStudy远程RCE漏洞复现_过云的博客-CSDN博客](https://blog.csdn.net/weixin_43268670/article/details/107098135)
    - CSRF（跨站请求伪造）
    - File Inclusion（文件包含）
    - File Upload（文件上传）
    - Insecure CAPTCHA （不安全的验证码）
    - SQL Injection（SQL注入）模拟sql注入攻击漏洞：[深入学习1———利用phpstudy搭建本地sql注入漏洞_这周末在做梦的博客-CSDN博客_phpstudy sql注入](https://blog.csdn.net/weixin_46203060/article/details/109411239)
    - SQL Injection（Blind）（SQL盲注）
    - XSS（Reflected）（反射型跨站脚本）
    - XSS（Stored）（存储型跨站脚本） -->

---

- 环境：OWASP Broken Web Applications VM, Version 0.94.  See www.owaspbwa.org for more information.
Login with username=root and password=owaspbwa

靶场由OWASP专门为Web安全研究者和初学者开发的一个靶场，包含了大量存在已知安全漏洞的训练实验环境和真实Web应用程序；
靶场在官网下载后是一个集成虚拟机，可以直接在vm中打开，物理机访问ip即可访问到web平台，使用root owaspbwa 登入就会返回靶场地址，直接可以访问靶场。
dvwa适合了解漏洞和简单的漏洞利用，owaspbwa则就更贴近实际的复杂的业务环境

- **目前工作**：使用AWVS进行扫描，导出输出结果，用适当形式储存

- **目前工作**：综合python与metasploit



### 2. 【深度搜索url】采用机器学习或其他方案实现优化url列表、版本识别。

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

### 3. 积累poc资源，实现测试方案，分析测试效果。

[概念验证 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E6%A6%82%E5%BF%B5%E9%AA%8C%E8%AF%81)

poc有很多引擎，先找个python引擎如巡风或修改pocsuite，关键要增强有效的poc库达到百以上。然后对今年新出poc要有些展现。

概念验证（英语：Proof of concept，简称POC）是对某些想法的一个**较短而不完整的实现**，以证明其可行性，示范其原理，其目的是为了验证一些概念或理论。概念验证通常被认为是一个有里程碑意义的实现的原型 。 

<!-- 在计算机安全术语中，概念验证经常被用来作为漏洞利用的别名。（英语：Exploit，本意为“利用”）是计算机安全术语，指的是利用程序中的某些漏洞，来得到计算机的控制权 -->

- **现有技术**

- POC验证引擎（开源）包含作者设计引擎的思路 [01 需求与设计 · Xyntax/POC-T Wiki](https://github.com/Xyntax/POC-T/wiki/01-%E9%9C%80%E6%B1%82%E4%B8%8E%E8%AE%BE%E8%AE%A1)
    - 与Pocsuite的差异
        - Seebug+Pocsuite+ZoomEye 一条龙服务确实很好用。Pocsuite的所有PoC需要按模板要求使用Pocsuite指定的函数，这样的优点在于可以在HTTP请求层面直接做控制，从而支持“全局代理”，“全局随机UA”等功能，同时保证了脚本的稳定性与规范性，对于不懂验证逻辑的客户或运维人员，直接运行脚本即可。
        - 我在设计POC-T的初衷就是给脚本最大的自由度，可以引入第三方库，不需要任何模板和继承。这样既能够扩展其功能，又能保证效率的最大化，不用每次写脚本都查文档格式，一个脚本一行命令，三五分钟即可完成任务。缺点就是脚本的稳定性需要自己的编码能力和经验来保证。此外，POC-T提供更多的输入输出方式和第三方接口支持。
    - PoC相关
        - 曾经认为将大量PoC整合到一起即是最强大的“扫描器”。 然而现状是PoC开发水平良莠不齐，大部分容错性很差，真正集成到扫描器中需要二次开发。
        - 目前Bugscan收集了大量PoC，但是其编写者设置level的机制导致大部分PoC无法被获取。相比之下在Seebug付出一点时间就可以拿到自己想要的。
        - 练习PoC编写可以多关注新鲜的exp资源，如：http://www.exploitalert.com/

- POC验证引擎2:[knownsec/pocsuite3: pocsuite3 is an open-sourced remote vulnerability testing framework developed by the Knownsec 404 Team.](https://github.com/knownsec/pocsuite3)

> Seebug+Pocsuite+ZoomEye PoC路线

[漏洞列表 - 知道创宇 Seebug 漏洞平台](https://www.seebug.org/vuldb/vulnerabilities?has_poc=true)

### 4. 对专家智能渗透流程进行模拟和评估。

[WSP-LAB/FUSE: A penetration testing tool for finding file upload bugs (NDSS 2020)](https://github.com/WSP-LAB/FUSE) 这是一个逻辑漏洞的通用解决，多做几个逻辑漏洞就可，

### 5. 框架逻辑整合，界面编写

[关于 PyQt5 Hello World - maicss](https://maicss.gitbook.io/pyqt5-chinese-tutoral/hello_world)

<!-- 使用python搭建交互式终端实例
[PyQtTerminal-1/QTerminal.py at master · niuzhenjiang/PyQtTerminal-1](https://github.com/niuzhenjiang/PyQtTerminal-1/blob/master/QTerminal.py)

[Helium-icons 图标 - 113 个免费矢量图标下载 - Easyicon](https://www.easyicon.net/iconsearch/iconset:Helium-icons/?s=addtime_DESC) -->

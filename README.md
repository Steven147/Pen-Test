# AI渗透测试

## 技术路线

1. 基于kali-linux熟练使用渗透工具awvs，sqlmap，metasploit，构思集成方案。
2. 采用机器学习或其他方案实现优化url列表、版本识别。
3. 积累poc资源，实现测试方案，分析测试效果。
4. 对专家智能渗透流程进行模拟和评估。
5. 系统输入输出逻辑整合与基于pyqt的GUI编写。

### 1. 基于kali-linux熟练使用渗透工具awvs，sqlmap，metasploit，构思集成方案。

- **现有技术一**：论文一集成和自动化识别工具方法，完整样例。

参考文献：1. 渗透测试中信息采集的知识提取与集成 Knowledge Extraction and Integration for Information Gathering in Penetration Testing.docx 

本文回顾和识别开源子域枚举和服务扫描工具，并提出了一种集成和自动化识别工具的方法。 结果表明，由于减少了人工任务，使用我们的方法大大改善了信息收集过程。【本竞赛项目的基本依据以及期望达到的目标】

本研究论文的重点是确定能够收集信息的工具，以便集成这些工具，从而使这些工具的组合输出易于管理、组织和分析。【评价标准】

我们正在审查和识别在识别信息系统的子域和开放端口方面最有效和最有效的子域和服务扫描工具。 然后我们使用shell脚本集成这些工具。 我们将集成工具的结果与独立工具进行比较，以评估我们的信息收集方法的效率和有效性。【技术路线】

- **现有技术二**：awvs解码，可针对性的对awvs扫描器进行输入输出测试。

[fnmsd/awvs_script_decode: 解密好的AWVS10.5 data/script/目录下的脚本](https://github.com/fnmsd/awvs_script_decode)

[gatlindada/awvs-decode: The best and easiest way to decode and repack AWVS scripts. AWVS 最好、最简单、最新的解码/再打包方法，仅15行代码！](https://github.com/gatlindada/awvs-decode)

- **现有技术三**：PyMetasploit，综合python与metasploit

[allfro/pymetasploit: A full-fledged msfrpc library for Metasploit framework.](https://github.com/allfro/pymetasploit)

> 工作概述：论文提供了一条技术路线，可以适当进行复现，并参考论文的分析和对比方法。利用现有对awvs的解码以及pymetasploit库的支持，可以简要实现从搭建broken服务器，到利用awvs针对性的扫描出该漏洞，并使用python的msf接口进行尝试性攻击，最后将信息收集流程、攻击流程以及攻击结果报告集成到gui中。

- **目前工作**：搭建并配置有漏洞的web应用程序

[渗透测试靶场介绍 - 菜鸟-传奇 - 博客园](https://www.cnblogs.com/cainiao-chuanqi/p/13870199.html)

[enaqx/awesome-pentest: A collection of awesome penetration testing resources, tools and other shiny things](https://github.com/enaqx/awesome-pentest)

- 环境一：windows XP(vmware) + phpstudy 搭建本地服务器
包含b站视频教程，已失效，保存在本地
[小皮面板(phpstudy) - 让天下没有难配的服务器环境！](https://www.xp.cn/)

[新手指南：手把手教你如何搭建自己的渗透测试环境 - FreeBuf网络安全行业门户](https://www.freebuf.com/sectool/102661.html)

- 环境二：[digininja/DVWA: Damn Vulnerable Web Application (DVWA)](https://github.com/digininja/DVWA)

[新手指南：DVWA-1.9全级别教程（完结篇，附实例）之XSS - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/web/123779.html)

使用PHP语言写的测试平台，要先搭好PHP+MYSQL的环境，把文件直接解压到你的站点根目录。

使用浏览器访问,我的本地环境：[Damn Vulnerable Web Application (DVWA) v1.10](http://10.10.10.130/DVWA)，输入用户名admin，密码password即可登录

- 环境三：OWASP Broken Web Applications VM, Version 0.94.  See www.owaspbwa.org for more information.
Login with username=root and password=owaspbwa

参考：metasploit渗透测试魔鬼训练营，[OWASP Broken Web Applications](https://owasp.org/www-project-broken-web-applications/#)


- **目前工作**：模拟漏洞并攻击

DVWA

推荐新手首选靶场，DVWA的目的是通过简单易用的界面来实践一些最常见的Web漏洞，这些漏洞具有不同的难度，是一个涵盖了多种漏洞一个综合的靶机

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
    - XSS（Stored）（存储型跨站脚本）

OWASP Broken Web Applications Project

靶场由OWASP专门为Web安全研究者和初学者开发的一个靶场，包含了大量存在已知安全漏洞的训练实验环境和真实Web应用程序；
靶场在官网下载后是一个集成虚拟机，可以直接在vm中打开，物理机访问ip即可访问到web平台，使用root owaspbwa 登入就会返回靶场地址，直接可以访问靶场。
dvwa适合了解漏洞和简单的漏洞利用，owaspbwa则就更贴近实际的复杂的业务环境



### 2. 采用机器学习或其他方案实现优化url列表、版本识别。

### 3. 积累poc资源，实现测试方案，分析测试效果。

### 4. 对专家智能渗透流程进行模拟和评估。

### 5. 系统输入输出逻辑整合与基于pyqt的GUI编写。

- **目前工作**：GUI搭建与逻辑整合

[关于 PyQt5 Hello World - maicss](https://maicss.gitbook.io/pyqt5-chinese-tutoral/hello_world)

使用python搭建交互式终端实例
[PyQtTerminal-1/QTerminal.py at master · niuzhenjiang/PyQtTerminal-1](https://github.com/niuzhenjiang/PyQtTerminal-1/blob/master/QTerminal.py)

[Helium-icons 图标 - 113 个免费矢量图标下载 - Easyicon](https://www.easyicon.net/iconsearch/iconset:Helium-icons/?s=addtime_DESC)
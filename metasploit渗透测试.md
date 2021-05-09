<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [metasploit渗透测试魔鬼训练营](#metasploit渗透测试魔鬼训练营)
  - [1 初识metasploit](#1-初识metasploit)
    - [1.1 渗透测试](#11-渗透测试)
    - [1.2 漏洞分析](#12-漏洞分析)
    - [1.3 渗透测试软件metasploit](#13-渗透测试软件metasploit)
    - [1.6 metasploit使用接口](#16-metasploit使用接口)
  - [渗透测试实验环境](#渗透测试实验环境)
  - [情报搜集技术](#情报搜集技术)

<!-- /code_chunk_output -->

# metasploit渗透测试魔鬼训练营

> **metasploit 能做的只是非常少的一部分，文件上传漏洞、sql注入这些都做不了，所以才需要人工智能渗透的方案**

## 1 初识metasploit

### 1.1 渗透测试

模拟恶意攻击者的技术与方法，挫败目标系统安全控制措施，取得访问控制权，并发现具备业务影响后果安全隐患的一种安全测试与评估方法。分类：黑盒测试、白盒测试、灰盒测试

渗透测试方法学：
- [OSSTMM 开源安全测试方法介绍](https://www.halospacex.com/portal.php?mod=view&aid=35)
- [NIST SP800 系列标准](http://blog.sina.com.cn/s/blog_5386f0790102xr6t.html)
- [OWASP-CHINA](http://www.owasp.org.cn/)
- WASC-TC
- PTES

环节：
1. 前期交互阶段：确定测试范围、目标，涉及
1. 情报收集阶段：网络拓扑、系统配置
1. 威胁建模阶段：
1. 漏洞分析阶段：安全漏洞扫描结果、服务差点？信息
1. 渗透攻击阶段：
1. 后渗透攻击阶段：
1. 报告阶段：

### 1.2 漏洞分析

渗透攻击流程中最核心和最基本的内容是找出目标系统中存在的安全漏洞，并试试渗透攻击。

漏洞生命周期：
1. 安全漏洞研究与挖掘
1. 漏洞代码开发与测试（与漏洞挖掘同时）：开发概念验证性的渗透攻击代码（POC）
1. 安全漏洞、渗透代码传播
1. 补丁、检测应用

安全漏洞公共资源库
[教育行业漏洞报告平台（Beta）](https://src.sjtu.edu.cn/)

### 1.3 渗透测试软件metasploit

开源的渗透测试框架软件，也将成为支持整个渗透测试过程的安全技术集成开发与应用环境。

渗透测试框架软件：
1. 情报收集：扫描探测，查点辅助模块？插件调用nmap nessus openvas等开源网络扫描工具
1. 威胁建模
1. 漏洞分析
1. 后渗透攻击
1. 报告生成阶段

metasploit框架中最重要的是辅助模块、渗透攻击模块、后渗透攻击模块、攻击载荷模块、空指令模块、编码器模块

### 1.6 metasploit使用接口

功能最强大的接口是MSF终端

```shell
$ msfconsole
$ help search 
```

> samba susermap_script安全漏洞

[一个古老的漏洞username map script，翻出来说说-Mingo-51CTO博客](https://blog.51cto.com/13444271/2125364)

[(11条消息) Metasploit学习： Samba服务 usermap_script安全漏洞利用_Sy0ung_的博客-CSDN博客](https://blog.csdn.net/Karol_agan/article/details/109784575?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)

[(11条消息) 利用metasploit(MSF)对windows 7的ms17-010漏洞进行攻击过程（永恒之蓝）_Bulldozer_GD的博客-CSDN博客](https://blog.csdn.net/Bulldozer_GD/article/details/105900785)

[(11条消息) Metasploit使用msfcli命令行接口编写shell脚本程序_m0_46161993的博客-CSDN博客](https://blog.csdn.net/m0_46161993/article/details/107070620)


## 渗透测试实验环境

## 情报搜集技术

[[网络安全] 二.Web渗透信息收集之域名、端口、服务、指纹、旁站、CDN和敏感信息-技术圈](https://jishuin.proginn.com/p/763bfbd2b014)

- 外围信息收集
  - DNS IP `whois testfire.net` `dig @nswatson.ibm.com testfire.com` IP2Location netcratf
  <!-- - whois baidu.com
   Domain Name: BAIDU.COM
   Registry Domain ID: 11181110_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.markmonitor.com
   Registrar URL: http://www.markmonitor.com
   Updated Date: 2020-12-09T04:04:41Z
   Creation Date: 1999-10-11T11:05:17Z
   Registry Expiry Date: 2026-10-11T11:05:17Z
   Registrar: MarkMonitor Inc.
   Registrar IANA ID: 292
   Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
   Registrar Abuse Contact Phone: +1.2083895740
   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
   Domain Status: serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited
   Domain Status: serverTransferProhibited https://icann.org/epp#serverTransferProhibited
   Domain Status: serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited
   Name Server: NS1.BAIDU.COM
   Name Server: NS2.BAIDU.COM
   Name Server: NS3.BAIDU.COM
   Name Server: NS4.BAIDU.COM
   Name Server: NS7.BAIDU.COM
   DNSSEC: unsigned
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/ -->
  <!-- - dig @ns.watson.ibm.com testfire.com                                                   10 ⨯
    ; <<>> DiG 9.16.11-Debian <<>> @ns.watson.ibm.com testfire.com
    ; (1 server found)
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: REFUSED, id: 880
    ;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1
    ;; WARNING: recursion requested but not available

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 4096
    ; COOKIE: ce4424c1e8a3768b24a7cfbc605a8d078a3e08892e4226c8 (good)
    ;; QUESTION SECTION:
    ;testfire.com.                  IN      A

    ;; Query time: 236 msec
    ;; SERVER: 129.34.20.80#53(129.34.20.80)
    ;; WHEN: 三 3月 24 08:51:20 CST 2021
    ;; MSG SIZE  rcvd: 69 -->
 - 搜索引擎 google hacking
    - 搜索网站目录结构 [【渗透测试小白系列】之目录扫描、Nmap的使用及使用Metasploit通过MS17-010获取系统权限 - osc_9sai706y的个人空间 - OSCHINA - 中文开源技术交流社区](https://my.oschina.net/u/4383170/blog/3384909)
- 主机探测、端口扫描 nmap
  - ICMP ping
  - metasploit主机发现模块：[(11条消息) 【渗透测试笔记】之【MSF 信息搜集】_AA8j的博客-CSDN博客](https://blog.csdn.net/qq_44874645/article/details/109548694?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_baidulandingword-1&spm=1001.2101.3001.4242)
  - 系统
  - 端口扫描、服务类型探测
  - 探测扫描结果分析：主机、对应操作系统、主要的开放端口、对应的服务版本
- 服务扫描、查点
  - telnet ssh服务
  - 口令


<!-- ## Web应用渗透技术

## 网络服务渗透攻击

## 客户端渗透攻击

## 社会工程学

## 移动环境渗透测试

## meterpreter

## 黑客夺旗竞赛实战

## 渗透测试报告撰写 -->
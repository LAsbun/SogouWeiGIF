# 搜狗微信 GIF 爬虫程序

## 项目简介

- 基于搜狗微信搜索，从搜狗微信文章中爬取 动态图以及相关内容
- 抓取搜狗微信搜索的搜索热词中的动态图
- 抓取跟关键字有关的微信公众号

## 环境、架构

- 开发语言: python2.7
- 开发环境: Ubuntu 14.04
- 数据库: MongoDB 3.2.1
- 爬虫框架: Scrapy

## 爬取内容：

新建一个名为 **SogouWeixin** 的数据库。

通过爬取对应的文章,提取下述内容，然后将数据储存在表 **WeixinGIF** 中。
字段|含义
---|---
ContentUrl |抓取的文章的地址
PostTime    |抓取的文章的发布时间
ContentId    |唯一标识
GIFContents  |文章内的动态图以及文字信息
up_chars |图片上面的一个文字描述
under_desc |图片下面面的一个文字描述
gif_url |图片地址
ArticleAccount |文章发布的公众号信息
weixinname |公众号名称
weixinhao  |微信号



## 部署环境

1. 安装 mongodb
2. 安装 Scrapy 软件库
3. python 模块: pymongo, requests, base64, urllib, re, time, datetime, json
4. 登陆搜狗通行证的账号和密码置于 **cookies.py** 中
5. 用户搜索关键字置于 **startuser.py** 中


## 执行程序

总共有三个功能，分别对应三个Python文件:

**首先启动 MongoDB，然后切换到这三个文件所在的路径中，再根据需求执行相应的文件:**

- 通过关键字爬取文章: **RunKeyWord.py**
- 爬取首页热门推荐: **RunHotIndex.py**
- 爬取热搜: **RundHotKeyWord.py**


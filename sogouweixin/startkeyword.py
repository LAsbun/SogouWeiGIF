#!/usr/bin/env python
#coding:utf-8
__author__ = 'sws'

import urllib
import time

# 添加搜索关键字 #
KeyWord = ['搞笑', 'gif', '动图', '动态图']

url_func = lambda query, page=1: "http://weixin.sogou.com/weixin?"+urllib.urlencode({'query': query})+"&_sug_type_=&sut=4156&lkt=1%2C1468554851164%2C1468554851164&_sug_=y&type=2&"+urllib.urlencode({'sst0':int(time.time()*1000), 'page': page})+"&ie=utf8&w=01019900&dr=1"

Start_urls = [url_func(key) for key in KeyWord]
# print Start_urls



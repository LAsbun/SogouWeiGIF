#!/usr/bin/env python
#coding:utf-8
__author__ = 'sws'

import requests
import urllib
import time
import json
import random
from agents import AGENTS

url_func = lambda query, page=1: "http://weixin.sogou.com/weixin?"+urllib.urlencode({'query': query})+"&_sug_type_=&sut=4156&lkt=1%2C1468554851164%2C1468554851164&_sug_=y&type=2&sst0=1468554851267&"+urllib.urlencode({'page': page})+"&ie=utf8&w=01019900&dr=1"



# 获取热点关键词
def get_hot_key():
    headers = {}

    hot_keys = []

    url = 'http://weixin.sogou.com/pcindex/pc/web/web.js?'+urllib.urlencode({'t':int(time.time()*1000)})


    headers['User-Agent'] = random.choice(AGENTS)
    # time.sleep(5)
    res = requests.get(url, headers=headers)

    res = json.loads(res.content)

    for k in res['topwords']:
        hot_keys.append(k['word'].encode('utf8'))

    return hot_keys

HotKeys = [url_func(key) for key in get_hot_key()]

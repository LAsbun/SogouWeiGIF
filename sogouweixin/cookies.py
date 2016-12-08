#!/usr/bin/env python
#coding:utf-8
__author__ = 'sws'


import requests
import math
import random
import time
from agents import AGENTS

# 填写搜狗通行证账号密码 #
# 格式如下所示，no 代表账号, psw 代表密码
# 账号之间以逗号分隔
SogouAccount = [
    {'no': 'user', 'psw': 'pwd'},

]

# 获取token值
def get_token():

    f = lambda : "0x%X" %math.floor((1+random.random())*0x10000)
    token = ''
    for i in range(8):
        token += f()[3:]

    return token

def getCookies(Account):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://account.sogou.com/web/login'
    for elem in Account:
        account = elem['no']
        password = elem['psw']
        username = account
        postData = {
            'username':  username,
            'password':  password,
            'captcha':   '',
            'autoLogin': '0',
            'client_id': '1120',
            'xd':        'https://account.sogou.com/static/api/jump.htm',
            'token':     get_token()

        }
        headers = {}
        headers['User-Agent'] = random.choice(AGENTS)
        session = requests.Session()
        r = session.post(loginURL, data=postData, headers = headers)

        r = session.get("https://account.sogou.com/")

        cookie = session.cookies.get_dict()
        if len(cookie) != 0:
            cookies.append(cookie)

    return cookies

cookies = getCookies(SogouAccount)

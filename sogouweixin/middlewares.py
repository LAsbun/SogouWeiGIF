#!/usr/bin/env python
#coding:utf-8
__author__ = 'sws'
from agents import AGENTS
from cookies import cookies
import random

# Change User-Agent #
class CustomUserAgentMiddleware(object):
    """docstring for CustomUserAgentMiddleware"""
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent

# Change Cookie #
class CustomCookieMiddleware(object):
    # time.sleep(random.randint(1, 5))
    """docstring for CustomCookieMiddleware"""
    def process_request(self, request, spider):
        # print cookies, 'cookie '*5
        cookie = random.choice(cookies)
        request.cookies = cookie





# -*- coding: utf-8 -*-

# Scrapy settings for sogouweixin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sogouweixin'

SPIDER_MODULES = ['sogouweixin.spiders']
NEWSPIDER_MODULE = 'sogouweixin.spiders'

DOWNLOADER_MIDDLEWARES = {
    # 'sogouweixin.middlewares.CustomProxyMiddleware':400,
    'sogouweixin.middlewares.CustomUserAgentMiddleware': 401,
    'sogouweixin.middlewares.CustomCookieMiddleware': 402,

    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

DOWNLOAD_DELAY = 8
# LOG_LEVEL = 'INFO'



ITEM_PIPELINES = {
    'sogouweixin.pipelines.MongoDBPipleline': 300,
}


# 采用广度优先搜索
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
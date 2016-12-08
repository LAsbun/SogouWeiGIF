# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 关键词
class KeywordItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    KeyWord = scrapy.Field()    #关键字
    ArticleAccount = scrapy.Field()  # 微信号和名字  {'weixinhao':xx, 'weixinname':xx}

    #  GIFUrls 这是一个由字典构成的数组   {'gifurl':xx, 'desc':{'up_desc':xx,'self_desc':xx, 'under_desc':xx}}
    GIFContents = scrapy.Field()
    ContentUrl = scrapy.Field()  # 文章url
    ContentId = scrapy.Field()  #文章标识
    PostTime = scrapy.Field()  #文章发布时间

# 首页推荐
class HotIndexItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ArticleAccount = scrapy.Field()  # 微信号和名字  {'weixinhao':xx, 'weixinname':xx}

    #  GIFUrls 这是一个由字典构成的数组   {'gifurl':xx, 'desc':{'up_desc':xx,'self_desc':xx, 'under_desc':xx}}
    GIFContents = scrapy.Field()
    ContentUrl = scrapy.Field()  # 文章url
    ContentId = scrapy.Field()  #文章标识
    PostTime = scrapy.Field()  #文章发布时间
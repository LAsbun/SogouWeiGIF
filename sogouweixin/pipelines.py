# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from sogouweixin.items import KeywordItem, HotIndexItem
import logging

class MongoDBPipleline(object):
    def __init__(self):
        self.clinet = pymongo.MongoClient("localhost", 27017)
        db = self.clinet["SogouWeixin5"]
        self.Keyword = db['WeixinGIF']
        self.HotIndex = db['HotIndex']

    def process_item(self, item, spider):
        """ 判断数据库中该Content是否已经存在 """
        if isinstance(item, KeywordItem):
            Content_Id = self.Keyword.find({'ContentId': item['ContentId']})
            if Content_Id.count() == 0:
                try:
                    self.Keyword.insert_one(dict(item))
                    logging.info("Save Content File: %s !!!", item['ContentId'])
                    print "save post!!!"
                except Exception:
                    pass
        elif isinstance(item, HotIndexItem):
            Content_Id = self.HotIndex.find({'ContentId': item['ContentId']})
            if Content_Id.count() == 0:
                try:
                    self.HotIndex.insert_one(dict(item))
                    logging.info("Save Content File: %s !!!", item['ContentId'])
                    print "save post!!!"
                except Exception:
                    pass
        # return item

    def close_spider(self, spider):
        self.clinet.close()

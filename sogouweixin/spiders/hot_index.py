#!/usr/bin/env python
#coding:utf-8
__author__ = 'sws'

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from sogouweixin.items import KeywordItem

# 抓取首页热门推荐 文章
class HotIndex(scrapy.Spider):

    name = 'hotindex'

    allowed_domains = [
        "weixin.sogou.com",
        'mp.weixin.qq.com',
    ]

    start_urls  = [
        "http://weixin.sogou.com/"
    ]

    def parse(self, response):

        self.parse1(response)

        sel = Selector(response)

        tags = sel.xpath("//div[@class='wx-tabbox2']")

        prefix_url = 'http://weixin.sogou.com/pcindex/pc/pc_'

        for i in range(1,len(tags)):
            for j in range(1, 16):
                url = prefix_url+str(i)+"/"+str(j)+".html"
                yield Request(url=url, callback= self.parse1)


    def parse1(self, response):
        sel = Selector(response)

        link_lists = sel.xpath('//a[@class="wx-news-info"]/@href').extract()

        for link in link_lists:
            yield Request(url= link, callback = self.parse2)

    # 进入文章页面
    def parse2(self, response):
        sel = Selector(response)
        item = KeywordItem()
        item['ContentUrl'] = response.url
        item['ContentId'] = response.url.split('=')[-2]   # 每篇文章的唯一标识

         # 获取微信公众号以及微信公众号名字
        weixinhao = weixinname = None
        try:
            weixinhao = sel.xpath("//div[@class='profile_inner']/p[1]/span/text()").extract()[0]
        except Exception:
            pass
        try:
            weixinname = sel.xpath("//div[@class='profile_inner']/strong/text()").extract()[0]
        except Exception:
            pass
        # 存入item
        ArticleAccount = {}
        ArticleAccount['weixinhao'] = weixinhao
        ArticleAccount['weixinname'] = weixinname
        item['ArticleAccount'] = ArticleAccount
        # 获取文章发布时间
        PostTime = sel.xpath("//em[contains(@id, 'post-date')]/text()").extract()
        # 存入item
        item['PostTime'] = PostTime[0]

        gif_links = sel.xpath("//img[contains(@data-type, 'gif')]/@data-src").extract()
        p_lists = sel.xpath("//div[@class='rich_media_content ']/p") #获取全部的xpath
        # print gif_links, '^'*20

        GIFContents = [] # 动态图的url和相关描述

        # 提取图以及对应的文字说明
        for i in range(len(p_lists)):
            temp = {}

            if len(p_lists[i].xpath('./img[@data-type="gif"]')) == 0:
                continue
            # print p_lists[i]
            # break
            src = p_lists[i].xpath('./img/@data-src').extract()
            up_chars = under_chars = None
            if len(src) != 0:
                # print dir(p_lists[i])
                # 尝试获取上面的一个文字
                try:
                    up_chars = p_lists[i-1].xpath('./text()|./*/text()|./*/*/text()').extract()[0]
                except Exception:
                    pass
                    # 尝试获取下面的一个文字
                try:
                    under_chars = p_lists[i+1].xpath('./text()|./*/text()|./*/*/text()').extract()[0]
                except Exception:
                    pass
                temp['gif_url'] = src[0]
                temp['up_chars'] = up_chars
                temp['under_chars'] = under_chars
            # 判断是否有提取到数据 如果有存入数据库
            if len(temp) != 0:
                GIFContents.append(temp)

        # 如果网页中没有动态图片那么就不存
        if len(GIFContents) == 0:
            return
        item['GIFContents'] = GIFContents
        return item



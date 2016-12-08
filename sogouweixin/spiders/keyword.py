# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from sogouweixin.startkeyword import Start_urls
from sogouweixin.items import KeywordItem

# 抓取关键字 文章
class KeywordSpider(scrapy.Spider):
    name = "keyword"

    allowed_domains = [
        "weixin.sogou.com",
        'mp.weixin.qq.com',
    ]

    host = 'http://weixin.sogou.com/weixin'

    start_urls =Start_urls

    def parse(self, response):
        sel = Selector(response)
        next_links = sel.xpath("//div[@id='pagebar_container']/a")

        for next_link in next_links:
            url = self.host+next_link.xpath("./@href").extract()[0]
            yield Request(url=url, callback= self.parse1)


    def parse1(self, response):
        sel = Selector(response)

        #  尝试获取关键词
        item = KeywordItem()
        Keyword = None
        try:
            Keyword = sel.xpath('//input[@id="upquery"]/@value').extract()[0]
        except Exception:
            pass

        item['KeyWord'] = Keyword

        #  获取文章地址
        link_lists = sel.xpath('//div[@class="txt-box"]/h4/a/@href').extract()

        for link in link_lists:
            yield Request(url= link, meta={'item':item}, callback = self.parse2)



         # 查找是否还有其他的链接
        next_links = sel.xpath("//div[@id='pagebar_container']/a")

        for next_link in next_links:
            url = self.host+next_link.xpath("./@href").extract()[0]
            yield Request(url=url, callback= self.parse1)

    # 进入文章页面
    def parse2(self, response):
        sel = Selector(response)
        try:
            item = response.meta['item']
        except Exception:
            item = KeywordItem()
            item['KeyWord'] = None

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

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdianItem(scrapy.Item):
    # define the fields for your item here like:
    #景点名字
    name = scrapy.Field()
    #景点评级
    level = scrapy.Field()
    #景点热度
    hot = scrapy.Field()
    #景点地址
    address = scrapy.Field()
    #景点销量
    num = scrapy.Field()
    #所在页面
    page = scrapy.Field()
    #所爬取的城市
    city = scrapy.Field()

# -*- coding: utf-8 -*-
import scrapy
from jingdian.items import JingdianItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class QunarSpider(CrawlSpider):
    name = 'qunar'
    allowed_domains = ['piao.qunar.com']
    cities = ['厦门','杭州','新疆']
    start_urls = ['http://piao.qunar.com/ticket/list.htm?keyword=' + city + '&region=&from=mps_search_suggest&page=1' for city in cities]
    pagelinks = LinkExtractor(restrict_xpaths='//*[@id="pager-container"]/div/a')
    rules = [Rule(pagelinks,callback='url_parse',follow=True)]
    def url_parse(self,response):
        self.logger.info('正在爬取的url:%s'%response.url)
        item = JingdianItem()
        item['name'] = response.xpath('//*[@id="search-list"]/div/div/div[2]/h3/a/text()').extract()
        item['level'] = response.xpath('//*[@id="search-list"]/div/div/div[2]/div/div[1]/span[1]/text()').extract()
        item['hot'] = response.xpath('//*[@id="search-list"]/div/div/div[2]/div/div[1]/div/span[1]/em/span/text()').re(r'(\d.\d*)')
        item['address'] = response.xpath('//*[@id="search-list"]/div/div/div[2]/div/p/span/@title').extract()
        item['num'] = response.xpath('//*[@id="search-list"]/div/div/div[3]/table').re(r'<span class="hot_num">(\d*)')
        item['page'] = response.xpath('//*[@id="pager-container"]/div/em/text()').extract()
        item['city'] = response.xpath('//*[@id="search-list"]/div[1]/div/div[2]/div/div[1]/span/a/text()').extract()[0].split('·')[0]
        yield item
        # for city in self.cities:
        #     url = 'http://piao.qunar.com/ticket/list.htm?keyword={}&region=&from=mps_search_suggest&page=1'.format(city)
        #     yield scrapy.Request(url,callback=self.url_parse)



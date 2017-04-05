#coding:utf-8

import scrapy
from Dangdang_Spider.items import DangdangSpiderItem
import urllib2
import re

num = 1
class DangdangSpider(scrapy.Spider):
    name = 'DangdangSpider'
    allowed_domains = ["dangdang.com"]
    start_urls = ['http://search.dangdang.com/?key=%CD%F8%C2%E7%B0%B2%C8%AB&act=input&ddt-rpm=undefined']

    def parse(self,response):
        #print response+"11111111111"
        divs = response.xpath(u"//p[@name='title']/a")
        for div in divs:
            item = DangdangSpiderItem()
            book_url = div.xpath('@href')[0].extract()
            item["book_url"] = book_url if "http:" in book_url else ("http://product.dangdang.com"+ book_url)
            yield scrapy.Request(url = item["book_url"],meta = {"item":item},callback = self.parse_detail,dont_filter=False)
        global num
        num = num + 1
        if (num <= 5):
            next_url = "http://search.dangdang.com/?key=%CD%F8%C2%E7%B0%B2%C8%AB&act=input&ddt-rpm=undefined&page_index=" + str(num)
            yield scrapy.Request(url = next_url,callback = self.parse,dont_filter=False)
        #item = ScrapyDemo1Item()


    def parse_detail(self,response):
        item = response.meta["item"]
        item["book_name"] = response.xpath(u"//div[@class='name_info']/h1/@title")[0].extract()
        item["pub_company"] = response.xpath(u"//span[@dd_name='出版社']/a/text()")[0].extract()
        item["comm_num"] = response.xpath(u"//a[@id='comm_num_down']/text()")[0].extract()
        tmp_book_price = response.xpath(u"//p[@id='dd-price']/text()").extract()
        book_price = tmp_book_price[1].replace(' ', '')
        item["book_price"] = book_price
        return item
#coding=utf-8

import urllib
import urllib2
from lxml import etree

for num in range(1,6):
    url = "http://search.dangdang.com/?key=%CD%F8%C2%E7%B0%B2%C8%AB&act=input&ddt-rpm=undefined&page_index=" + str(num)
    #url = 'http://search.dangdang.com/?key=%CD%F8%C2%E7%B0%B2%C8%AB&act=input&ddt-rpm=undefined'
    req = urllib2.Request(url)
    r = urllib2.urlopen(req)
    html = r.read()        #返回网页内容
    #print html
    html = html.decode('gbk','ignore')
    tree=etree.HTML(html)
    goods_urls = tree.xpath(u"//p[@name='title']/a/@href")
    #print goods_urls
    #price = tree.xpath(u"//span[@class='search_now_price']/text()")
    #print price
    for goods in goods_urls:
      #goods_url = 'https:'+goods
      goods_req = urllib2.Request(goods)
      r2 = urllib2.urlopen(goods_req)
      goods_html = r2.read()
      goods_html = goods_html.decode('gbk','ignore')
      goods_tree = etree.HTML(goods_html)
      price = goods_tree.xpath(u"//p[@id='dd-price']/text()")
      name = goods_tree.xpath(u"//div[@class='name_info']/h1/@title")
      #collect_count = goods_tree.xpath(u"//a[@class='btn_scsp']/text()")[0]
      #good_judge = goods_tree.xpath(u"//span[@dd_name='好评']/text()")[0]
      pub_company = goods_tree.xpath(u"//span[@dd_name='出版社']/a/text()")
      comm_num = goods_tree.xpath(u"//a[@id='comm_num_down']/text()")
      #print good_judge
      print name[0] + " " + pub_company[0] + " " + price[1].replace(' ', '') + " " + comm_num[0] + " " + goods
      #print price[1].replace(' ', '')
      #print comm_num[0]



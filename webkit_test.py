#coding:utf-8

import spynner
from lxml import etree

browser = spynner.Browser()
browser.load(url='http://product.dangdang.com/22815096.html', load_timeout=200, tries=3)
try:
    browser.wait_load(10)
except:
    pass
string = browser.html
goods_tree = etree.HTML(string)
#collect_count = goods_tree.xpath(u"//a[@class='btn_scsp']/text()")[0]
good_judge = goods_tree.xpath(u"//span[@dd_name='好评']/text()")[0]
print good_judge

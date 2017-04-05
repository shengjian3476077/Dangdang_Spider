#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import urllib2

url='http://product.dangdang.com/index.php?r=callback%2Fcomment-list&productId=22815096&categoryPath=01.54.19.00.00.00&mainProductId=22815096&mediumId=0&pageIndex=1&sortType=1&filterType=1&isSystem=1&tagId=0&tagFilterCount=0' #这里的url比较长
#content=requests.get(url).content
req = urllib2.Request(url)
r = urllib2.urlopen(req)
html = r.read()        #返回网页内容
print html
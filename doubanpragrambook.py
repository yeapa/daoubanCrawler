#coding=utf-8
from bs4 import BeautifulSoup
import urllib2
import sys
import re
import string
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )
bookNameList=[]
priceList=[]

def saveUserInfo(idList,linkList):
    writeFile=file("result",'w')
    size=len(idList)
    for i in xrange(0,size):
        writeFile.write(idList[i]+'\t'+linkList[i]+'\n')
    writeFile.close()
def parseHtmlUserId(html):
    soup=BeautifulSoup(html)
    # td_tags=soup.select(".sub_ins td[width=\"80\"]")
    books=soup.select("#subject_list .subject-list > .subject-item .info")
    for book in books:
        bookNameTag=book.select("> h2 > a")
        if len(bookNameTag)!=0:
            bookName=bookNameTag[0].get("title")
            global bookNameList
            bookNameList.append(bookName)
        bookPriceTag=book.select("> .pub")
        bookPriceString=bookPriceTag[0].string
        bookPrice=bookPriceString.split("/")
        str=bookPrice[-1].strip()
        pattern=re.compile(r"[\d.]+");
        match=pattern.match(str);
        if match:
            price=match.group()
        else:
            price=0
        global priceList
        priceList.append(float(price))

def getHtml(url):
    response=urllib2.urlopen(url)
    html=response.read()
    return html

proxyInfo="127.0.0.1:8087"
proxySupport=urllib2.ProxyHandler({'http':proxyInfo})
opener=urllib2.build_opener(proxySupport)
urllib2.install_opener(opener);

for count in xrange(0,200,20):
    last="?start=%d&type=T" % count
    url="https://book.douban.com/tag/编程"+last
    html=getHtml(url)
    parseHtmlUserId(html)

resd=dict(zip(priceList,bookNameList))
resd=sorted(resd.iteritems(),key=lambda d:d[0])
print json.dumps(resd,encoding="utf-8",ensure_ascii=False)
# saveUserInfo(curIdList,curLinkList)
# print curIdList

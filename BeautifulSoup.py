from bs4 import BeautifulSoup
import urllib2
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def saveUserInfo(idList,linkList):
    writeFile=file("result",'w')
    size=len(idList)
    for i in xrange(0,size):
        writeFile.write(idList[i]+'\t'+linkList[i]+'\n')
    writeFile.close()
def parseHtmlUserId(html):
    idList=[]
    linkList=[]
    soup=BeautifulSoup(html)
    td_tags=soup.select(".sub_ins td[width=\"80\"]")

    # td_tags=soup.findAll('td',width='80',valign='top')
    i=0
    for td in td_tags:
        if i==20:
            break
        a=td.a
        link=a.get('href')
        i_start=link.find('people/')
        id=link[i_start+7:-1]
        idList.append(id)
        linkList.append(link)
        i+=1
    return (idList,linkList)

def getHtml(url):
    response=urllib2.urlopen(url)
    html=response.read()
    return html



proxyInfo="127.0.0.1:8087"
proxySupport=urllib2.ProxyHandler({'http':proxyInfo})
opener=urllib2.build_opener(proxySupport)
urllib2.install_opener(opener)

url="https://movie.douban.com/subject/10463953/collections?start=40"
html=getHtml(url)
(curIdList,curLinkList)=parseHtmlUserId(html)
saveUserInfo(curIdList,curLinkList)
print curIdList

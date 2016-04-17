import scrapy
class DoubanSpider(scrapy.spider.Spider):
    """docstring for DoubanSpider"""
    name="doubanspider"
    allowed_dimains=["douban.com"]
    start_urls=["https://www.douban.com"]
    def parse(self,response):
        filename="doubanresult"
        f=open(filename,'wb')
        f.write(response.body)
        # item=DoubanItem()
        # print response.css("head").extract()
        print "fffffffffffffffffffffffffffffffffffffffffff\n"

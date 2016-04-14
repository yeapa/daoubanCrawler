import scrapy
class DoubanSpider(scrapy.spider.Spider):
    """docstring for DoubanSpider"""
    name="doubanspider"
    allowed_dimains=["douban.com"]
    start_urls=["https://www.douban.com/tag/%E7%BC%96%E7%A8%8B/?focus=book"]
    def parse(self,response):
        filename="doubanresult"
        f=open(filename,'wb')
        f.write(response.body)
        print response.css("head").extract();

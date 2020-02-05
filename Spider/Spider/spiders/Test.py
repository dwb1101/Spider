# 导包
import scrapy


# 爬虫代码 爬取的是页面
class Test(scrapy.Spider):
    # 爬虫得唯一标识
    name = "Test"
    # 访问路径 地址后面要有个逗号
    start_urls = ("https://item.jd.com/59929124808.html",)

    # 回调函数
    def parse(self, response):
        print("回调函数")
        print(response.text)


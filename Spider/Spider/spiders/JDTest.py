import scrapy
import re
import json
import time

# 爬数据
class JDTest(scrapy.Spider):
    # 爬虫表示
    name = "JGTest"
    # 请求头信息(网页的数据都是以json进行传输)
    heads = {":authority": "sclub.jd.com",
             ":method": "GET",
             ":path": "/comment/productPageComments.action?callback=fetchJSON_comment98vv7&productId=59929124808&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1",
             ":scheme": "https",
             "accept": "*/*",
             "accept-encoding": "gzip, deflate, br",
             "accept-language": "zh-CN,zh;q=0.9",
             "cookie": "areaId=14; ipLoc-djd=14-1137-1138-0; PCSYCityID=CN_340000_340500_340521; unpl=V2_ZzNtbUIAFhNwXxQEchxbAmJTFlxKXxMWdAhBBCwcCwA0B0EJclRCFX0URldnGFgUZwYZXUtcRhZFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsZXgdhBRZcQlVzJXI4dmR%2fHl8GbgUiXHJWc1chVEJRcxxUSGcDEF9EUUcUdQp2VUsa; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_1fd74fca84664a5099a2016af4f4b5be|1575526720274; JSESSIONID=40EAE4E44166E3C4F27DC3C9E34A07F9.s1; __jda=122270672.1133775013.1563955369.1575465926.1575526720.5; __jdb=122270672.4.1133775013|5.1575526720; __jdc=122270672; shshshfp=79a7ff8fc033b076ccb950216d256b50; shshshfpa=27562aba-e49d-5c8e-63a8-461e0a5a835e-1563955375; shshshsID=b3ad090f1139fd60489fb426cda253f8_3_1575527028916; shshshfpb=tfvzQY8Cl7VI6M0lQ7OSGIg%3D%3D; 3AB9D23F7A4B3C9B=PQ3XSB2Q64KGP2XAD3QRT2JS2I5D5JUQTZYGSGY5YH2TWQ6VRQVIGINET5S5YW7OU54Q4W32E43AZOTRSYBWQ4O4OI; __jdu=1133775013",
             "referer": "https://item.jd.com/59929124808.html",
             "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3223.0 Safari/537.36"
             }
    # 请求地址的变量名可以随便给了
    urls = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv7&productId=59929124808&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1"

    # 请求数据
    def start_requests(self):
        for i in range(1,21):
            url=self.urls % i
            yield scrapy.Request(url=url,
                             headers=self.heads,
                             callback=self.parse)

    # 获取回到函数(获取返回结果)
    def parse(self, response):
        print("回调函数")
        print(response.text)
        # 正则表达式
        c = re.compile(r"[(](.*)[)]", re.S)
        # 匹配正则表达式
        # 返回的结果是list
        f = re.findall(c, response.text)
        print(f[0])
        jsonStr=json.loads(f[0])
        print(jsonStr)
        #获取评价信息
        comments=jsonStr["comments"]
        for i in comments:
           id=i["id"]
           #conten=i["content"]
           score=i["score"]
           #data=str(id)+","+conten+","+str(score)
           data=str(id)+","+str(score)
           #写入到文件
           print(data)
           with open("F:\IDER\dangtu\Spider\data\data.txt",
                     mode="a",encoding="utf-8") as f:
               f.write(data)
               f.write("\n")
        # 模拟延迟
        time.sleep(2)


# -*- coding: utf-8 -*-
import scrapy
from k17.items import K17Item
import json
class A17kSpider(scrapy.Spider):
    name = '17k'


#######################################################################
##############d第二种方法获取
#######################################################################
    allowed_domains = ['17k.com']
    start_urls = ['http://www.17k.com/chapter/271047/6336386.html']
    def parse(self, response):
        for i in range(6336386, 6336510 + 1):  ###拼接url
            new_url="http://www.17k.com/chapter/271047/"+str(i)+".html"
            #print(new_url)
            yield scrapy.Request(new_url, callback=self.next_parse) ##传入url

    def next_parse(self,response):
        for bb in response.xpath('//div[@class="readArea"]/div[@class="readAreaBox content"]'):
                item=K17Item()
                title=bb.xpath("h1/text()").extract()###得到每一章的标题
                new_title=(''.join(title).replace('\n','')).strip()
                item['title']=new_title
                #print(item['title'])
                dec= bb.xpath("div[@class='p']/text()").extract()###得到每一章的详细内容
               # print(type(dec))
                dec_new=((''.join(dec).replace('\n','')).replace('\u3000','')).strip() ###去除内容中的\n 和\u3000和空格的问题
                #print(type(dec_new))
                item['describe'] = dec_new

                yield item

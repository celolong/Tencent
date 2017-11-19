# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']

    def parse(self, response):
        # print (response.url)

        # 获取所有职位节点列表
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        # print (len(node_list))

        # 遍历节点列表
        for node in node_list:

            # 创建item实例
            item = TencentItem()
            # 抽取数据，赋值
            item['name'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['link'] = 'http://hr.tencent.com/' + node.xpath('./td[1]/a/@href').extract()[0]
            item['type'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract()[0]
            item['address'] = node.xpath('./td[4]/text()').extract()[0]
            item['pub_time'] = node.xpath('./td[5]/text()').extract()[0]
            # print (item)
            # 返回数据
            # yield item
            # 通过meta以字典形式往下一个函数传参数
            yield scrapy.Request(item['link'],callback=self.parse_detail,meta={'mymeta':item})


        # 获取下一页url
        try:
            next_url = 'http://hr.tencent.com/' + response.xpath('//*[@id="next"]/@href').extract()[0]
            yield scrapy.Request(next_url, callback=self.parse)

        except:
            pass


    def parse_detail(self,response):
        # print(response.meta)
        item = response.meta['mymeta']
        item['duty'] =''.join(response.xpath('//tr[3]/td/ul/li/text()').extract())
        item['request'] = ''.join(response.xpath('//tr[4]/td/ul/li/text()').extract())
        yield item


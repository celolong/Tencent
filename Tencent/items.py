# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名
    name = scrapy.Field()
    # 链接
    link = scrapy.Field()
    # 职位类别
    type = scrapy.Field()
    # 人数
    number = scrapy.Field()
    # 地点
    address = scrapy.Field()
    # 发布时间
    pub_time = scrapy.Field()
    # 工作职责
    duty = scrapy.Field()
    # 职位要求
    request = scrapy.Field()
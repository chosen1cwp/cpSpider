# Define here the models for your scraped items
#
# 保存所抓取的数据的容器，其存储方式类似于 Python 的字典 其使用方法和 Python 字典类似
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CpspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bule_ball = scrapy.Field();
    red_ball = scrapy.Field();
    cycle_No = scrapy.Field();
    pass

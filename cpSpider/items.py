# Define here the models for your scraped items
#
# 保存所抓取的数据的容器，其存储方式类似于 Python 的字典 其使用方法和 Python 字典类似
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CpspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bule_ball = scrapy.Field(); # 蓝球
    red_ball = scrapy.Field(); # 红球
    cycle_No = scrapy.Field(); # 期号
    winner_price_num = scrapy.Field(); # 中奖注数
    open_date = scrapy.Field(); # 开奖日期
    total_sale = scrapy.Field(); # 总销售额
    jackpot = scrapy.Field(); # 奖池金额
    pass

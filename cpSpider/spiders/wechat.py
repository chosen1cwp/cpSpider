import scrapy


class WechatSpider(scrapy.Spider):
    name = 'wechat'
    allowed_domains = ['mp.weixin.qq.com']
    start_urls = ['https://mp.weixin.qq.com/']

    def parse(self, response):
        pass

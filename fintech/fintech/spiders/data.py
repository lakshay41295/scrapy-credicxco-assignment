import json

import scrapy
from ..items import  FintechItem


class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['midsouthshooterssupply.com']
    start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1']

    def parse(self, response):

        items = FintechItem()

        title= response.xpath('//div[@class="product-description"]/a/text()').extract()


        stock1=[]
        stock = response.xpath('//span[@class="out-of-stock"]/text()').extract()

        for i in stock:
            if i =='Out of Stock':
                stock1.append('False')
            else:
                stock1.append('True')
        #print(len(stock1))

        manuf=response.xpath('//div[@class="catalog-item-brand-item-number"]/a/text()').extract()


        price =response.xpath('//span[@class="price"]/span/text()').extract()

        # print(price)
        for i in range(0,len(title)):
            items['title'] =title[i]
            items['stock'] = stock1[i]
            items['manuf']  = manuf[i]
            items['price'] = float(price[i].split('$')[1])

            yield items







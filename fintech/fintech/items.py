# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FintechItem(scrapy.Item):
    title = scrapy.Field()
    manuf=scrapy.Field()
    stock=scrapy.Field()
    price=scrapy.Field()

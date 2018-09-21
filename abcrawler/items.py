# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AbcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuoteItem(scrapy.Item):
    id = scrapy.Field()
    quote = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    created_date = scrapy.Field()

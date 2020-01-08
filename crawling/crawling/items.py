# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookCover(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    # in_stock = scrapy.Field()
    star = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()


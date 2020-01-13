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

"""
{'image_urls': ['http://books.toscrape.com/media/cache/0b/bc/0bbcd0a6f4bcd81ccb1049a52736406e.jpg'],
 'images': [{'checksum': '4b75678760ac88e4bca9c888da999d97',
             'path': 'full/27bfbda82c55c895ad6621816856c22b43fb2581.jpg',
             'url': 'http://books.toscrape.com/media/cache/0b/bc/0bbcd0a6f4bcd81ccb1049a52736406e.jpg'}],
 'title': 'Libertarianism for Beginners'}

"""

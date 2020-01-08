# -*- coding: utf-8 -*-
import scrapy
from ..items import BookCover


class ImageSpiderSpider(scrapy.Spider):
    name = 'image_spider'
    # allowed_domains = ['http://books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        books = response.css("ol.row article.product_pod")
        for book in books:
            image_relative_url = book.css("div.image_container>a::attr(href)").get()
            image_absolute_url = response.urljoin(image_relative_url)
            yield scrapy.Request(url=image_absolute_url, callback=self.parse_details)

        next_url = response.css("ul.pager>li.next>a::attr(href)").get()
        if next_url:
            next_url = response.urljoin(next_url)
            yield response.follow(next_url, callback=self.parse)


    def parse_details(self, response):
        data = response.css("article.product_page")
        title = data.css("h1::text").get()
        price = data.css("p.price_color::text").get()
        star = data.css("div.col-sm-6.product_main p::attr(class)").getall()[-1].split()[-1]
        image_relative_url = data.css("img::attr(src)").get()
        image_absolute_url = response.urljoin(image_relative_url)
        yield BookCover(title=title, price=price, star=star, file_urls=[image_absolute_url])


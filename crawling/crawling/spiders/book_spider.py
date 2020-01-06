# -*- coding: utf-8 -*-
import scrapy

star_mapper = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

pages = int(input("How many pages do you want to scrape:"))


class BookSpiderSpider(scrapy.Spider):
    name = 'book_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/page-{}.html'.format(i + 1) for i in range(pages)]

    def parse(self, response):
        data = {}
        books = response.css("ol.row article.product_pod")
        for book in books:
            data["title"] = book.css("h3 a::attr(title)").getall()
            data["price"] = book.css("div.product_price p.price_color::text").getall()
            data["availability"] = book.css("div.product_price p.instock.availability::text").getall()[1].strip()
            text_star = book.css("p::attr(class)").get().split()[-1]
            data["star"] = star_mapper[text_star]
            yield data

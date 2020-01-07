# -*- coding: utf-8 -*-
import scrapy

star_mapper = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


class BookSpiderSpider(scrapy.Spider):
    name = 'book_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        data = {}
        books = response.css("ol.row article.product_pod")
        for book in books:
            data["title"] = book.css("h3 a::attr(title)").get()
            data["price"] = book.css("div.product_price p.price_color::text").get()
            data["availability"] = book.css("div.product_price p.instock.availability::text").getall()[1].strip()
            text_star = book.css("p::attr(class)").get().split()[-1]
            data["star"] = star_mapper[text_star]
            yield data
        next_page = response.css("div>ul.pager>li.next>a::attr(href)").get()
        if next_page:
            next_url = response.urljoin(next_page)
            yield response.follow(next_url, callback=self.parse)

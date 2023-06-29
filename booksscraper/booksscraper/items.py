# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    name = scrapy.Field()
    on_sale = scrapy.Field()
    book_full_price = scrapy.Field()
    book_off_price = scrapy.Field()

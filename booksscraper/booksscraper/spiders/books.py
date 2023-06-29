import scrapy
from .config import BookXpath
from ..items import BooksItem


class Books(scrapy.Spider):
    name = "books"
    start_urls = [BookXpath.start_url]

    def parse(self, response):

        books_box = BookXpath.book_box
        book_name = BookXpath.book_name
        book_price = BookXpath.book_price
        on_sale = BookXpath.on_sale
        book_full_price = BookXpath.book_full_price
        book_off_price = BookXpath.book_off_price
        next_page = BookXpath.next_page

        for product in response.xpath(books_box):
            book_items = BooksItem()
            book_items['name'] = product.xpath(book_name).get()
            book_items['on_sale'] = product.xpath(on_sale).get()

            if on_sale is not None:
                book_items['book_full_price'] = response.xpath(book_full_price).get()
                book_items['book_off_price'] = response.xpath(book_off_price).get()
            else:
                book_items['book_full_price'] = response.xpath(book_price).get()

            yield book_items

        # next_page = response.xpath(next_page).get()
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)

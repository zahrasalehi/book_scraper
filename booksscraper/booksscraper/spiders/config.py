import os

from dotenv import load_dotenv

load_dotenv()


class BookXpath:
    start_url = os.getenv("BOOK_XPATH_START_URL",
                          "http://kadenbook.com/product-category/%d9%81%d8%b1%d9%88%d8%b4%da%af%d8%a7%d9%87-%da%a9%d8%aa%d8%a7%d8%a8-%d8%b2%d8%a8%d8%a7%d9%86/novels/literature-and-novels/")
    book_box = os.getenv("BOOK_XPATH_BOX",
                         "//div[@class='products elements-grid wd-products-holder  wd-spacing-30 grid-columns-6 pagination-pagination title-line-two align-items-start row']")
    book_name = os.getenv("BOOK_XPATH_NAME", "//h3[@class='wd-entities-title']/a/text()")
    on_sale = os.getenv("BOOK_ON_SALE_PERCENTAGE", "//span[@class='onsale product-label']/text()")
    book_price = os.getenv("BOOK_XPATH_PRICE", "//span[@class='price']//text()")
    book_full_price = os.getenv("BOOK_XPATH_FULL_PRICE", "//span[@class='price']/del//text()")
    book_off_price = os.getenv("BOOK_XPATH_OFF_PRICE", "//span[@class='price']/ins//text()")

    next_page = os.getenv("BOOK_XPATH_NEXT_PAGE", "response.xpath('//a[@class='next page-numbers']/@href').get()")

from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import now

from .models import *


class ScrapySpiderPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        books = BookTable()
        books.name = item["name"]
        books.on_sale = item["on_sale"]
        books.book_full_price = item["book_full_price"]
        books.book_off_price = item["book_off_price"]

        try:
            session.add(books)
            session.commit()
        except:
            session.rollback()
        finally:
            session.close()

        return item

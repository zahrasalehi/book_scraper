import pytz
from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Text, DateTime
from datetime import datetime
from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    conn_str = get_project_settings().get("CONNECTION_STRING")
    return create_engine(conn_str)


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class BookTable(DeclarativeBase):
    @staticmethod
    def now():
        return datetime.now(tz=pytz.timezone('Asia/Tehran'))

    __tablename__ = "data"
    id = Column(Integer, primary_key=True)
    name = Column('name', Text(), nullable=False)
    on_sale = Column('on_sale', Text(), nullable=False)
    book_full_price = Column('book_full_price', Text(), nullable=False)
    book_off_price = Column('book_off_price', Text(), nullable=False)
    date_time = Column('date_time', DateTime(timezone=True), nullable=False, default=now)

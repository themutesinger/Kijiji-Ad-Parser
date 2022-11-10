from sqlalchemy import Column, String, Integer, Date, DECIMAL

from .base import Base


class Ad(Base):
    __tablename__ = 'Ads'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    price = Column(Integer())
    currency = Column(String(20))
    date = Column(String(50))
    image = Column(String(350))
    pagination = Column(Integer())

    def __init__(self, title, price, date, image, pagination, currency):
        self.title = title
        self.price = price
        self.currency = currency
        self.date = date
        self.image = image
        self.pagination = pagination
        
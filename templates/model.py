from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Product(Base):
   __tablename__ = 'Product'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(Float)
   picture_link = Column(String)
   Description = Column(String)

def add_to_cart(productID)

class Cart(Base):
	__tablename__ = "Cart"
	id = Column(Integer, primary_key=True)
	productID = Column(String)
	
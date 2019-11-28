from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(Name, Price, Picture_link,Description):
    product_object = Product()
        Name=name,
        Price=price,
        Picture_link=Picture_link
        Description=Description
    session.add(product_object)
    session.commit()

def edit_product_status(name, edit_product):
	product_object = session.query(
       Product).filter_by(
       name=name).first()
   product_object.edit_product = edit_product
   session.commit()


def delete_product(product_name):
   session.query(Product).filter_by(
       name=product_name).delete()
   session.commit()

def query_all():
   Products = session.query(
      Product).all()
   return Products
print(query_all())

def query_by_name(product_name):
   Product = session.query(
       Product).filter_by(
       name=their_name).first()
   return product

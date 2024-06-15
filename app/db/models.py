from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from app.db.db import engine

Base = declarative_base()

# Category

class Category(Base):
    __tablename__ = "category"
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_name: str = Column(String, unique=True)
    description: str = Column(String)

# --------------------------

# Seller

class Seller(Base):
    __tablename__ = "seller"
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    seller_name: str = Column(String, unique=True)

# --------------------------

# Item

class Item(Base):
    __tablename__ = "item"
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_name: str = Column(String)
    color: str = Column(String)
    in_stock: bool = Column(Boolean)
    category_id: int = Column(Integer, ForeignKey("category.id"))
    seller_id: int = Column(Integer, ForeignKey("seller.id"))

# --------------------------

Base.metadata.create_all(bind=engine)
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# importing declarative base class from database.py
from .database import DeclBase


#  These model classes are used for creating the tables in the database.
class User(DeclBase):
    __tablename__ = "users"  # defines the name of table in the database

    # column names and their value types
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # indicates that the column items will be related to the Item table values. It will consist of all the primary key values of Item table as a list.
    items = relationship("Item", back_populates="owner")


class Item(DeclBase):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

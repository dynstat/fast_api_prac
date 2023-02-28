from sqlalchemy import Column, Integer, Text, Boolean
from .database import base

class Todo(base):
    __tablename__ = "ToDo"
    id = Column(Integer,primary_key = True)
    task = Column(Text)
    completed = Column(Boolean)
    
    def __repr__(self) -> str:
        return '<Todo %r>' % (self.id)
    
    


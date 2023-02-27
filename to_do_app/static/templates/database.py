from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "sqlite:///todo.sqlite3"

# creating engine 

engine = create_engine(DB_URL,connect_args = {'check_same_thread':False} )

# creating a session object
sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# creating a base class

base = declarative_base()

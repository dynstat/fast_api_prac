from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "sqlite:///./sql_app/sql_app_DB.sqlite3."

# Creating an engine to create and connect to the database provided.
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

# dB session can be created using sessionLocal class
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# to be used in model classes (for databases)
DeclBase = declarative_base()

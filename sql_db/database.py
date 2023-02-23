from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 


# create a sqlalchemy databaseurl

SQLALCGEMY_DATABASE_URL = "sqlite:///test.db"


'''By default SQLite will only allow one thread to communicate with it, assuming that each thread would handle an independent request.
This is to prevent accidentally sharing the same connection for different things (for different requests).
But in FastAPI, using normal functions (def) more than one thread could interact with the database for the same request, so we need to make SQLite know that it should allow that with connect_args={"check_same_thread": False}.
Also, we will make sure each request gets its own database connection session in a dependency, so there's no need for that default mechanism.
we are "connecting" to a SQLite database (opening a file with the SQLite database)
'''
engine = create_engine(SQLALCGEMY_DATABASE_URL,echo = True)


'''Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.
But once we create an instance of the SessionLocal class, this instance will be the actual database session.
We name it SessionLocal to distinguish it from the Session we are importing from SQLAlchemy.'''

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine,connect_args={"check_same_thread": False})

'''Now we will use the function declarative_base() that returns a class.
Later we will inherit from this class to create each of the database models or classes (the ORM models):'''
Base = declarative_base()




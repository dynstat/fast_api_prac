from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import Boolean, Column, Integer, String


SQLALCHEMY_DATABASE_URL = ("sqlite:///test.sqlite3")
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# The first step is to create a SQLAlchemy "engine".
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},echo = True)
'''
Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.

But once we create an instance of the SessionLocal class, this instance will be the actual database session.

We name it SessionLocal to distinguish it from the Session we are importing from SQLAlchemy.
'''

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

Base = declarative_base()




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    
#to migrate

Base.metadata.create_all(engine) 

# create data into table 
u1 =User(id=1,email="k@k.com",hashed_password="123abc@",is_active=True)
u2 =User(id=2,email="v@v.com",hashed_password="124abc@",is_active=True)
u3 =User(id=3,email="k@v.com",hashed_password="124abc@",is_active=True)
u4 =User(id=4,email="b@v.com",hashed_password="124abc@",is_active=True)
u5 =User(id=5,email="i@v.com",hashed_password="124abc@",is_active=True)
# session.add(u1)
session.add_all([u1,u2,u3,u4,u5])
session.commit()


# '''get all data'''
# user = session.query(User)

# for u in user:
#     print(u.email)


# '''get data in order'''
# user = session.query(User).order_by(User.email)

# for u in user:
#     print(u.email)

# '''get data by filtering'''
# user = session.query(User).filter(User.hashed_password=="123abc@").first()
# print(user.email)
# for u in user:
#     print(u.email)

# '''update data'''
# user=session.query(User).filter(User.email=="k@k.com").first()
# print(user.email)
# user.email = "kv@kv.com"
# session.commit()
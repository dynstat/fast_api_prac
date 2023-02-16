# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import Boolean, Column, Integer, String


# engine = create_engine("sqlite:///sqlite.db",echo = True,connect_args={"check_same_thread": False})

# session = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Base = declarative_base()


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)




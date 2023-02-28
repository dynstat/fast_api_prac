# from .models import User, Item
from . import models, schemas
from .schemas import *
from sqlalchemy.orm import Session


# Searches the dB with user_id and returns that user if found.
def get_user_by_id(db: Session, user_id: int):
    matched_user = db.query(models.User).filter(models.User.id == user_id).first()
    return matched_user


# Searches the dB with email and returns that user if found.
def get_user_by_email(db: Session, email: str):
    matched_user = db.query(models.User).filter(models.User.email == email).first()
    return matched_user


# create a user in dB
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = "hashed" + user.password
    new_user_obj = models.User(email=user.email, hashed_password=fake_hashed_password)

    # creates a new instance of model named User (not in dB)
    db.add(new_user_obj)

    # adds the above new instance to the dB session (still not visible in dB, need to commit )
    db.commit()  # creates a new row in users table in dB (VISIBLE NOW)

    # to update the new values (if any) in dB to the instance created in python code of fastAPI
    db.refresh(new_user_obj)
    return new_user_obj

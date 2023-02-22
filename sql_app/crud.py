# from .models import User, Item
from . import models, schemas
from .schemas import *
from sqlalchemy.orm import Session


# Searches the dB with user_id and returns that user if found.
def get_user_by_id(db: Session, user_id: int):
    matched_user = db.query(models.User).filter(models.User.id == user_id).first()
    return matched_user

from sqlalchemy.orm import Session
from .database import sessionLocal


# dB dependency
def get_db():
    db: Session = sessionLocal()
    try:
        yield db
    finally:
        db.close()

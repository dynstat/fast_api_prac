from sqlalchemy.orm import Session
from .database import sessionLocal


# dB dependency. This function creates a generator, the yield statement returns a value and haults..without exiting the function.
def get_db():
    db: Session = sessionLocal()
    try:
        yield db  # sends the created database session
    finally:
        db.close()  # this statemnt gets excuted only in the end of function body.

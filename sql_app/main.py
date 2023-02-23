from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import sessionLocal, engine

# importing dependencies
from .dependencies_ import get_db


models.DeclBase.metadata.create_all(bind=engine)  # Unsure: Migrations related maybe ??

# FastAPI app
app = FastAPI()


# get user by id
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    matched_user = crud.get_user_by_id(db=db, user_id=user_id)
    if not matched_user:
        raise HTTPException(status_code=404, detail="User Not Found in Database")
    return matched_user


# handling POST request from user front-end to create a new User in dB
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.get_user_by_email(db, email=user.email)
    if new_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

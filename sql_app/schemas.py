from pydantic import BaseModel


# Creating this class similar to SQLAlchemy's declarative_base() object, mainly for validation purposes
class User(BaseModel):
    id: int
    email: str

    # By defining the Config subclass, and setting the attribute "orm_mode" to True helps the response_model parameter to..
    # to validate the SqlAlchemy's return User object even if it is not in the form of dictionary.
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True

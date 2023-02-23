from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True

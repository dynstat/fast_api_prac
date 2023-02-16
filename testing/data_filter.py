'''But in most of the cases where we need to do something like this, we want the model 
just to filter/remove some of the data as in this example.And in those cases, we can 
use classes and inheritance to take advantage of function type annotations to get 
better support in the editor and tools, and still get the FastAPI data filtering'''



from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str
    last:str


@app.post("/user/")
async def create_user(user: BaseUser) -> BaseUser:
    return user
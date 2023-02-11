from enum import Enum
from typing import Union

from fastapi import FastAPI, Path, Query, status, Request, Body, Cookie, Header
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field


app = FastAPI()


# @app.exception_handler(422)
# async def error422(request: Request, exc: HTTPException):
#     return {"error422": "ye to bekar error hai"}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str = Field(example="Foo", title="ye hai name")
    description: str | None = Field(default=None, example="A very nice Item")
    price: float = Field(example=35.4)
    tax: float | None = Field(default=None, example=3.2)


class User(BaseModel):
    username: str = Field(example="username1234")
    full_name: str | None = Field(example="kanstat", default=None)


@app.get("/")
async def read_items(req: Request, ads_id: str | None = Cookie(default="h")):
    return {"ads_id": ads_id}


@app.get("/hitems/")
async def read_items(req: Request, x_token: list[str] | None = Header(default="abcd")):
    return {"X-Token values": x_token}


@app.get(
    "/items/{item_id}",
    responses={422: {"msg": "fix the data type of parameters"}},
)
async def read_items(
    req: Request,
    item_id: int = Path(title="The ID of the item to get", example=2023),
    q: str | None = Query(default=None),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.post("/items/{item_id}", status_code=status.HTTP_201_CREATED)
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


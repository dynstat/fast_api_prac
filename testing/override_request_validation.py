'''Override request validation exceptions¶
When a request contains invalid data, FastAPI internally raises a RequestValidationError.

And it also includes a default exception handler for it.

To override it, import the RequestValidationError and use it with @app.exception_handler(RequestValidationError) to decorate the exception handler.

The exception handler will receive a Request and the exception.'''


from enum import Enum
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"name":"kanchan"}


# tags
@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


# Tags, Enums
class Tags(Enum):
    items = "items"
    users = "users"


@app.get("/items/", tags=[Tags.items])
async def get_items():
    return ["Portal gun", "Plumbus"]


@app.get("/users/", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]
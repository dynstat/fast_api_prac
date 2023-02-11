from enum import Enum
from typing import Union
from base64 import b64encode
from fastapi import (
    FastAPI,
    Path,
    Query,
    status,
    Request,
    Body,
    Cookie,
    Header,
    File,
    UploadFile,
)
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError


async def http_exception(request: Request, exc: HTTPException):
    return JSONResponse(
        {"detail": "hehe"}, status_code=exc.status_code, headers=exc.headers
    )


# exc_handlers = {HTTPException: http_exception}
exc_handlers = {
    422: http_exception,
}

app = FastAPI(exception_handlers=exc_handlers)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    # if request.path_params
    # return PlainTextResponse(str(exc), status_code=422)
    return JSONResponse({"detail": "ye to galat h re"}, status_code=422)


# @app.exception_handler(422)
# async def error422(request: Request, exc: HTTPException):
#     return {"error422": "ye to bekar error hai"}


class Message(BaseModel):
    message: str


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


# @app.get("/")
# async def read_items(req: Request, ads_id: str | None = Cookie(default="h")):
#     return {"ads_id": ads_id}


@app.get("/hitems/")
async def read_items(req: Request, x_token: list[str] | None = Header(default="abcd")):
    return {"X-Token values": x_token}


@app.get("/items/{item_id}")
async def read_items(
    req: Request,
    item_id: int = Path(title="The ID of the item to get", example=2023),
    q: str | None = Query(default=None),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/test/{p1}")
async def read_items(p1: int):
    resp = {"p1": p1}
    return resp


@app.post("/items/{item_id}", status_code=status.HTTP_201_CREATED)
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


@app.post("/files/")
async def create_files(files: list[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/", include_in_schema=False)
async def main():
    content = """
<body>

kanchan
<h1>This is a heading</h1>
<p>This is a paragraph.</p>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

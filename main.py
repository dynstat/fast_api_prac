from enum import Enum
from typing import Union
from base64 import b64encode
from fastapi import (
    FastAPI,
    Path,
    Query,
    status,
    Request,
    Response,
    Body,
    Cookie,
    Header,
    File,
    UploadFile,
    Depends,
)
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError

# importing custom exception handling functions
from cust_exception import validation_exception_handler

# importing dependencies
import dependencies_

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def wrapper_validation_exception_handler(request, exc):
    return validation_exception_handler(request, exc)


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


@app.get("/hitems/")
async def read_items(req: Request, x_token: list[str] | None = Header(default="abcd")):
    return {"X-Token values": x_token}


@app.get("/items/{item_id}", tags=["basic"])
async def read_items(
    req: Request,
    item_id: int = Path(title="The ID of the item to get", example=2023),
    q: str | None = Query(default=None),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Endpoint for testing purposes
@app.get(
    "/test/{p1}/{p2}",
    tags=["testing"],
    dependencies=[
        Depends(dependencies_.verify_key),
        Depends(dependencies_.verify_token),
    ],
)
async def read_items(req: Request, p1: int, p2: int, q: int | None = None):
    resp = {"p1": p1, "p2": p2}
    if q:
        resp["q"] = q
    return resp


# Endpoint2 for testing purposes
@app.get("/test2", tags=["testing"])
async def read_items(req: Request, res: Response):
    res.set_cookie(key="my_cookie", value="test cookie value")
    return {"response_data": "test2 endpoint response"}


# Endpoint3 for testing purposes
@app.get("/test3", tags=["testing"])
async def read_items(
    req: Request, cuki: str | None = Cookie(default="something", title="cookie test")
):
    return {"response_data": "test2 endpoint response", "cuki": cuki}


@app.post("/items/{item_id}", status_code=status.HTTP_201_CREATED, tags=["basic"])
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

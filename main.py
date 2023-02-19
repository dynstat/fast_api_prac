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
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# importing dummy database
from dummy_db import dummy_DB


# importing custom exception handling functions
from cust_exception import validation_exception_handler

# importing dependencies
import dependencies_

# OAuth2PasswordBearer returns a class
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def wrapper_validation_exception_handler(request, exc):
    return validation_exception_handler(request, exc)


class Message(BaseModel):
    message: str


# not being used yet
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
async def hitems(req: Request, x_token: list[str] | None = Header(default="abcd")):
    return {"X-Token values": x_token}


@app.get("/items/{item_id}", tags=["basic"])
async def read_items_id(
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
async def read_items_2p(req: Request, p1: int, p2: int, q: int | None = None):
    resp = {"p1": p1, "p2": p2}
    if q:
        resp["q"] = q
    return resp


# Endpoint2 for testing purposes
@app.get("/test2", tags=["testing"])
async def read_items2(req: Request, res: Response):
    res.set_cookie(key="my_cookie", value="test cookie value")
    return {"response_data": "test2 endpoint response"}


# Endpoint3 for testing purposes
@app.get("/test3", tags=["testing"])
async def read_items3(
    req: Request,
    cuki: str
    | None = Cookie(
        default="something",
        title="cookie test",
    ),
    token: str = Depends(oauth2_scheme),  # token implementation is not done yet.
):
    return {"response_data": "test2 endpoint response", "cuki": cuki}


@app.post("/token", tags=["Authorization"])
async def authy(req: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    plain_password = form_data.password
    match_user_data = None
    # finding whether user exists or not
    for user_data in dummy_DB:
        if username in user_data["username"]:
            match_user_data = user_data
            break
    # imp: the response MUST have "access_token" and "token_type" as per the specs of OAuth2
    return {
        "access_token": "some_random_token_value_BlahBlah",
        "token_type": "bearer",
    }


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
Testing...
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

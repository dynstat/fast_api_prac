from fastapi import FastAPI,Body, Cookie,Header
from pydantic import BaseModel,Field

app = FastAPI()

class Image(BaseModel):
    url:str
    name:str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image:Image | None = None
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }



class Offer(BaseModel):
    name: str
    description: str 
    price: float 
    tax: float
    item: Item 
    


   
# @app.get("/items/")
# async def read_items(user_agent: str | None = Header(default=None)):
#     return {"User-Agent": user_agent}


   
@app.put("/items/{item_id}")
async def update_item(item_id: str):
        offer: Offer = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                    },
                },
            },
        )

  
        results = {"item_id": item_id, "item": offer}
        return results
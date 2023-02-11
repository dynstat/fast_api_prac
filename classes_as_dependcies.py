from fastapi import FastAPI,Depends,response



app = FastAPI()


fake_db = [{"item_name":"Foo","item_name":"Bar","item_name":"kanstat"}]

class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit
        


@app.get('/items/')
async def read_items(commons:CommonQueryParams=Depends(CommonQueryParams)):
    if commons.q:
        response.update({'q':commons.q})
    items = fake_db[commons.skip:commons.skip+commons.limit]
    response.update({"items":items})
    return response
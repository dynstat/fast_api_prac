from fastapi import FastAPI,Depends

app = FastAPI()


async def common_params(item_id:int, q:str | None = None,limit:int = 100):
    return {'item_id': item_id, 'q':q, 'limit':limit}


@app.get('/items/')
async def read_items(commans:dict = Depends(common_params)):
    return commans

@app.get('/users/')
async def read_users(comm:dict = Depends(common_params)):
    return comm

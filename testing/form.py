from fastapi import FastAPI,Form

app = FastAPI()

@app.post("/login/")

async def form_prac(item_id:int,username:str=Form(),password:str = Form()):
    return {"username":username}

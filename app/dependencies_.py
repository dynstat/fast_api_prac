from fastapi import HTTPException, Header


async def verify_token(x_token: str = Header(default="token1")):
    if x_token != "token1":
        raise HTTPException(status_code=400, detail="X-Token header is not token1")


async def verify_key(x_key: str = Header(default="key1")):
    if x_key != "key1":
        raise HTTPException(status_code=400, detail="X-Key header is not key1")
    return x_key

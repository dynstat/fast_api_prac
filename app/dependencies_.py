from fastapi import HTTPException, Header


# NOTE: The name of the parameter is x_token and x_key for the headers X-Token and X-Key respectively, since we can not put "-" in the python parameter variables.
# async function to verify the value of the header field named X-token is "token1" or not.
async def verify_token(x_token: str = Header(default="token1")):
    if x_token != "token1":
        raise HTTPException(status_code=400, detail="X-Token header is not token1")


# async function to verify the value of the header field named X-key is "token1" or not.
async def verify_key(x_key: str = Header(default="key1")):
    if x_key != "key1":
        raise HTTPException(status_code=400, detail="X-Key header is not key1")
    return x_key

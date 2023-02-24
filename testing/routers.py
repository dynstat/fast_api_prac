from fastapi import APIRouter

router = APIRouter()

@router.get("/users", tags=["users"])
async def read_users():
    return [{"username":"xs"},{"username":"xsvk"}] 

@router.get("/users/me/",tags=["users me"])
async def read_user_me():
    return {"username":"kanstat"}
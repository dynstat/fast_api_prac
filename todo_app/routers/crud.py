from fastapi import APIRouter,Request,Depends,Form,status
from ..database import sessionlocal, engine
from .. import models
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates




models.base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/tasks",
    tags=["Tasks"])

templates = Jinja2Templates(directory="todo_app/templates")

def get_db():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()
    



# to get all the task from the database
@router.get("/")
async def get_all_task(request:Request,db:Session=Depends(get_db) ):
    to_do = db.query(models.Todo).all()
    return templates.TemplateResponse("index.html",{"request":request,"to_do":to_do})
    

@router.post("/add_task")
async def create_task(request:Request, item:str=Form(...),db:Session=Depends(get_db)):
    add_task = models.Todo(task=item)
    db.add(add_task)
    db.commit()
    return RedirectResponse(url=router.url_path_for("get_all_task"),status_code=status.HTTP_303_SEE_OTHER)
    
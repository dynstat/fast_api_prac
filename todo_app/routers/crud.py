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
async def create_task(request:Request, task:str=Form(),db:Session=Depends(get_db)):
    add_task = models.Todo(task=task)
    db.add(add_task)
    db.commit()
    return RedirectResponse(url=router.url_path_for("get_all_task"),status_code=status.HTTP_303_SEE_OTHER)


@router.get("/edit_task/{task_id}")
async def get_edit_task_page(request:Request,task_id:int,db:Session=Depends(get_db)):
    task_tobe_edit = db.query(models.Todo).filter(models.Todo.id==task_id).first()
    return templates.TemplateResponse("edit.html",{"request":request,"task_tobe_edit":task_tobe_edit})


@router.post("/edit_task/{task_id}")
async def post_edit_task_page(request:Request,task_id:int,db:Session=Depends(get_db),task:str=Form(),):
    task_tobe_edit = db.query(models.Todo).filter(models.Todo.id==task_id).first()  
    task_tobe_edit.task  = task
    db.add(task_tobe_edit)
    db.commit()
    return RedirectResponse(url=router.url_path_for("get_all_task"),status_code=status.HTTP_303_SEE_OTHER)

@router.post("delete_task/{task_id}")
async def delete_task(request:Request,task_id:int,db:Session=Depends(get_db)):
    task_tobe_deleted = db.query(models.Todo).filter(models.Todo.id==task_id).first()
    db.delete(task_tobe_deleted)
    db.commit()
    return RedirectResponse(url=router.url_path_for("get_all_task"),status_code=status.HTTP_303_SEE_OTHER)
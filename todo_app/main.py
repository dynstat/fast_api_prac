from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
from . import models
from database import sessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

models.Base.metadata.createall(bind=engine)

templates = Jinja2Templates(directory='templates') 

app = FastAPI()

'''"Mounting" means adding a complete "independent" application in a specific path, that then takes care of handling all the sub-paths.'''
app.mount("/static", StaticFiles(directory="static"),name="static")


def get_db():
    db = sessionLocal()
    try:
        yield db 
    finally:
        db.close()
        

# to get items(tasks) from db 
@app.get("/")
async def get_task_list(req:Request, db:Session = Depends(get_db)):
    to_dos = db.query(models.Todo).order_by(models.Todo.id.desc()) 
    return templates.TemplateResponse("index.html",{"req":req,"to_dos":to_dos})
    
    
@app.post("/add_task")
async def create_tasks(req:Request, task:str=Form(), db:Session=Depends(get_db)):
    task_todo = models.Todo(task=task)  
    db.add(task_todo)
    db.commit()   
    return RedirectResponse(url=app.url_path_for("home"),status_code=status.HTTP_303_SEE_OTHER)


@app.get("/edit/{todo_id}")
async def add(req:Request, todo_id:int, db:Session=Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id==todo_id).first()
    return templates.TemplateResponse("edit.html",{"req":req,"todo":todo})
    

@app.post("/edit/{todo_id}")
async def edit_task(req:Request,todo_id:int,db:Session=Depends(get_db),task:str= Form(),completed:bool=Form(False)):
    todo= db.query(models.Todo).filter(models.Todo.id==todo_id).first()
    todo.task = task
    todo.completed = completed
    db.commit()
    return RedirectResponse(url = app.url_path_for("home"),status_code=status.HTTP_303_SEE_OTHER)

@app.get("/delete/{todo_id}")
async def delete_task(req:Request,todo_id:int, db:Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"),status_code=status.HTTP_303_SEE_OTHER)

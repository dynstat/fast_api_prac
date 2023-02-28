# from fastapi import FastAPI, Request, Depends, Form, status
# from fastapi.templating import Jinja2Templates
# from . import models
# from .database import sessionlocal, engine
# from sqlalchemy.orm import Session
# from fastapi.responses import RedirectResponse
# from fastapi.staticfiles import StaticFiles

# models.base.metadata.create_all(bind=engine)

# templates = Jinja2Templates(directory='todo_app/templates') 

# app = FastAPI()

# '''"Mounting" means adding a complete "independent" application in a specific path, that then takes care of handling all the sub-paths.'''
# app.mount("/static", StaticFiles(directory="todo_app/static/css"),name="static")


# def get_db():
#     db = sessionlocal()
#     try:
#         yield db 
#     finally:
#         db.close()
        

# # to get items(tasks) from db 
# @app.get("/")
# async def index(request:Request, db:Session = Depends(get_db)):
#     to_dos = db.query(models.Todo).order_by(models.Todo.id.desc()) 
#     return templates.TemplateResponse("index.html",{"request":request,"to_dos":to_dos})
    
    
# @app.post("/add_task")
# async def create_tasks(request:Request, task:str=Form(...), db:Session=Depends(get_db)):
#     task_todo = models.Todo(task=task)  
#     db.add(task_todo)
#     db.commit()   
#     return RedirectResponse(url=app.url_path_for("index"),status_code=status.HTTP_303_SEE_OTHER)


# @app.get("/edit/{todo_id}")
# async def add(request:Request, todo_id:int, db:Session=Depends(get_db)):
#     todo = db.query(models.Todo).filter(models.Todo.id==todo_id).first()
#     return templates.TemplateResponse("edit.html",{"request":request,"todo":todo})
    

# @app.post("/edit/{todo_id}")
# async def edit_task(request:Request,todo_id:int,db:Session=Depends(get_db),task:str= Form(),completed:bool=Form(False)):
#     todo= db.query(models.Todo).filter(models.Todo.id==todo_id).first()
#     todo.task = task
#     todo.completed = completed
#     db.commit()
#     return RedirectResponse(url = app.url_path_for("index"),status_code=status.HTTP_303_SEE_OTHER)

# @app.get("/delete/{todo_id}")
# async def delete_task(request:Request,todo_id:int, db:Session = Depends(get_db)):
#     todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
#     db.delete(todo)
#     db.commit()
#     return RedirectResponse(url=app.url_path_for("index"),status_code=status.HTTP_303_SEE_OTHER)


from fastapi import FastAPI
from .routers import crud


app = FastAPI()


app.include_router(crud.router)


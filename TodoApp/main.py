from fastapi import FastAPI, Depends, HTTPException, Path
import models
from models import Todos
from database import engine, Sessionlocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field 

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = Sessionlocal()

    try:
        yield db
    finally:
        db.close()

# muốn cho nó có mặt ở mọi điểm endpoint API tức là vầy thay vì m gọi lại db mỗi endpoint m chỉ cần 1 hàm xử lí 
db_dependency = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
    title : str = Field(min_length=3)
    description : str =Field(min_length=3, max_length=100)
    priority : int =Field(gt=0, lt=6)
    complete : bool


"""
Note:
- dependency injection thực chất có nghĩa là cần phải làm một việc gì đó trước khi thực thi những gì đang cố gắng thực thi
- clomn : cột
- row : hàng ngang

"""


@app.get("/",status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()  # add .all to fetch all data

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id : int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail='Todo not found.')

@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.dict()) #Unpack dict thành arguments

    db.add(todo_model) #-> đưa obj vào Session -> chưa save vào db nhé cưng
    db.commit() # EXECUTE SQL INSERT → LƯU vào database!
    # db.rollback()  # Xóa hàng chờ, không lưu gì cả! 

@app.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, 
                    todo_request: TodoRequest, 
                    todo_id : int = Path(gt=0)):
    #1. tìm todo
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    # 2. Không tìm thấy → 404
    if todo_model is None: 
        raise HTTPException(status_code=404, detail='Todo not found.')

    #3. Update từng field
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority 
    todo_model.complete = todo_request.complete

    # 4. Commit changes
    db.add(todo_model)
    db.commit()

@app.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, 
                    todo_id : int = Path(gt=0)):

    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None: 
        raise HTTPException(status_code=404, detail='Todo not found.')
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
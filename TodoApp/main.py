from fastapi import FastAPI, Depends
import models
from models import Todos
from database import engine, Sessionlocal
from typing import Annotated
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = Sessionlocal()
    # print('dauhbdjabn')
    try:
        yield db
    finally:
        db.close()

# muốn cho nó có mặt ở mọi điểm endpoint API 
db_dependency = Annotated[Session, Depends(get_db)]

"""
-dependency injection thực chất có nghĩa là cần phải làm một việc gì đó trước khi thực thi những gì đang cố gắng thực thi
"""


@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()  # ✅ Thêm .all() để lấy data!
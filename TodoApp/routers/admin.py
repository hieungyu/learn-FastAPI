from fastapi import FastAPI, Depends, HTTPException, Path,APIRouter
from models import Todos
from database import  Sessionlocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field 
from routers import auth
from .auth import get_current_user
from passlib.context import CryptContext


router = APIRouter(
    prefix= '/admin',
    tags=['admin']
)


def get_db():
    db = Sessionlocal()

    try:
        yield db
    finally:
        db.close()

# muốn cho nó có mặt ở mọi điểm endpoint API tức là vầy thay vì m gọi lại db mỗi endpoint m chỉ cần 1 hàm xử lí 
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/todo",status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(Todos).all()  

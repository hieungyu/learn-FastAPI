# model có thể được hiểu là cách để SQL alchemy có thể hiểu được loại bảng CSDL nào sẽ tạo trong CSDL của minh tương lai
from .database import Base
from sqlalchemy import Column, Integer,String, Boolean, ForeignKey


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True, index=True) 
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default= True)
    role = Column(String)
    phone_number = Column(String)



class Todos(Base):
    __tablename__ = "todos"

    """
    Mã định danh duy nhất cho bản ghi || index = True chỉ là cách đê có thể tăng hiệu suất bằng cách thông cho bảng \
    CSDL rằng dữ liệu nãy sẽ là duy nhất
    """
    id = Column(Integer, primary_key= True) 
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default= False) # 0 = False, 1 =True in a Db
    owner_id = Column(Integer, ForeignKey("users.id"))



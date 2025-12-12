from sqlalchemy import create_engine # tạo kết nối DB
from sqlalchemy.orm import sessionmaker # nhà máy sản xuất phiên làm việc
from sqlalchemy.ext.declarative import declarative_base # khuôn mẫu để tạo table


# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db' # 'sqlite' = loại database || "./todos.db" = File db trong thư mục hiện tại
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:123test@localhost/TodoApplicationDatabase' #POSTGRES
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:123test@127.0.0.1/TodoApplicationDatabase'

"""
# SQLite mặc định:
# - Chỉ cho 1 thread truy cập cùng lúc
# - FastAPI dùng nhiều threads (async)
# → Conflict! ❌

# Giải pháp:
{'check_same_thread': False}
# → Cho phép nhiều threads cùng truy cập ✅# SQLite mặc định:
# - Chỉ cho 1 thread truy cập cùng lúc
# - FastAPI dùng nhiều threads (async)
# → Conflict! ❌

# Giải pháp:
{'check_same_thread': False}
# → Cho phép nhiều threads cùng truy cập ✅

SQLite: chạy trong một file → kết nối phụ thuộc vào thread tạo ra → cần check_same_thread=False.

PostgreSQL: chạy dưới dạng server → mỗi kết nối độc lập → thread nào cũng dùng được → không cần flag đó.
"""
# engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread': False}) # tạo cái brige ==  engine
engine = create_engine(SQLALCHEMY_DATABASE_URL) 

"""
SessionLocal()  →  Tạo ra 1 session
    ↓
session.add()      ← Thêm data
session.query()    ← Đọc data
session.commit()   ← Lưu vào database
session.close()    ← Đóng kết nối
"""
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
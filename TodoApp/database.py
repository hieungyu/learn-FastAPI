from sqlalchemy import create_engine # tạo kết nối DB
from sqlalchemy.orm import sessionmaker # nhà máy sản xuất phiên làm việc
from sqlalchemy.ext.declarative import declarative_base # khuôn mẫu để tạo table


SQLAlCHEMY_DATABASE_URL = 'sqlite:///./todos.db' # 'sqlite' = loại database || "./todos.db" = File db trong thư mục hiện tại

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
"""
engine = create_engine(SQLAlCHEMY_DATABASE_URL,connect_args={'check_same_thread': False}) # tạo cái brige ==  engine


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
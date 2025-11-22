# DEMO BUG: BookRequest vs Book

from pydantic import BaseModel, Field

# 1. Class Book (class thường)
class Book:
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

# 2. BookRequest (Pydantic BaseModel)
class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(ge=1000, le=2030)

# ===== DEMO BUG =====

# List BOOKS chứa class Book
BOOKS = [
    Book(1, "Book One", "Author One", "Description", 5, 2024),
    Book(2, "Book Two", "Author Two", "Description", 4, 2025),
]

print("=== TRƯỚC KHI UPDATE ===")
print(f"BOOKS[0] type: {type(BOOKS[0])}")  # <class '__main__.Book'>
print(f"BOOKS[0].title: {BOOKS[0].title}")  # Book One
print()

# User gửi request update
new_book_data = BookRequest(
    id=1,
    title="Updated Title",
    author="Updated Author", 
    description="Updated Description",
    rating=5,
    published_date=2024
)

print("=== REQUEST DATA ===")
print(f"new_book_data type: {type(new_book_data)}")  # <class '__main__.BookRequest'>
print(f"new_book_data.title: {new_book_data.title}")  # Updated Title
print()

# ❌ CODE CŨ: Gán trực tiếp BookRequest vào Book[]
print("=== ❌ CODE CŨ (SAI) ===")
BOOKS[0] = new_book_data  # ❌ Gán BookRequest vào list Book[]
print(f"BOOKS[0] type: {type(BOOKS[0])}")  # <class '__main__.BookRequest'> ❌
print(f"BOOKS[1] type: {type(BOOKS[1])}")  # <class '__main__.Book'> ✅
print("⚠️ Bây giờ BOOKS[0] là BookRequest, BOOKS[1] là Book → KHÔNG NHẤT QUÁN!")
print()

# ✅ CODE MỚI: Convert BookRequest → Book
print("=== ✅ CODE MỚI (ĐÚNG) ===")
BOOKS = [
    Book(1, "Book One", "Author One", "Description", 5, 2024),
    Book(2, "Book Two", "Author Two", "Description", 4, 2025),
]

# Cách 1: Dùng **book.dict()
book_dict = new_book_data.dict()  # Convert BookRequest → dict
print(f"book_dict: {book_dict}")
BOOKS[0] = Book(**book_dict)  # Unpack dict → Book constructor
print(f"BOOKS[0] type: {type(BOOKS[0])}")  # <class '__main__.Book'> ✅
print(f"BOOKS[0].title: {BOOKS[0].title}")  # Updated Title
print()

# Cách 2: Dùng .model_dump() (Pydantic v2)
BOOKS[0] = Book(**new_book_data.model_dump())
print(f"BOOKS[0] type sau model_dump: {type(BOOKS[0])}")  # <class '__main__.Book'> ✅
print()

# ===== TẠI SAO PHẢI LÀM VẬY? =====
print("=== TẠI SAO PHẢI CONVERT? ===")
print("1. BOOKS[] chứa class Book (class thường)")
print("2. BookRequest là Pydantic BaseModel (có validation)")
print("3. Nếu gán trực tiếp → list không đồng nhất (Book + BookRequest)")
print("4. Có thể gây lỗi khi access attributes sau này")
print()

# ===== VÍ DỤ LỖI CÓ THỂ XẢY RA =====
print("=== VÍ DỤ LỖI ===")
BOOKS = [
    BookRequest(id=1, title="Book 1", author="A", description="D", rating=5, published_date=2024),  # BookRequest
    Book(2, "Book 2", "B", "D", 4, 2025),  # Book
]

# Code khác trong app cố access như class Book
try:
    for book in BOOKS:
        print(book.title)  # ✅ OK vì cả 2 đều có .title
except Exception as e:
    print(f"Error: {e}")

# Nhưng nếu check type:
print(f"All books same type? {all(type(b) == type(BOOKS[0]) for b in BOOKS)}")  # False ❌

# ========================================
# GIẢI THÍCH TOÁN TỬ ** (UNPACK)
# ========================================

# ===== VÍ DỤ 1: HÀM THƯỜNG =====
print("===== VÍ DỤ 1: HÀM THƯỜNG =====\n")

def say_hello(name, age, city):
    print(f"Xin chào {name}, {age} tuổi, sống ở {city}")

# Cách 1: Truyền argument bình thường
say_hello("Hieu", 22, "Vietnam")  # ✅ OK

# Cách 2: Dùng dict + ** (UNPACK)
person_dict = {
    "name": "Hieu",
    "age": 22,
    "city": "Vietnam"
}

# ❌ KHÔNG THỂ: say_hello(person_dict)  # Error! Hàm cần 3 args, bạn truyền 1 dict

# ✅ DÙNG ** ĐỂ UNPACK:
say_hello(**person_dict)  # ✅ OK! 
# **person_dict = name="Hieu", age=22, city="Vietnam"

print()

# ===== VÍ DỤ 2: CLASS BOOK =====
print("===== VÍ DỤ 2: CLASS BOOK =====\n")

class Book:
    def __init__(self, id, title, author, rating):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating
    
    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', rating={self.rating})"

# Cách 1: Tạo Book bình thường
book1 = Book(1, "FastAPI Guide", "Author A", 5)
print(f"Cách 1: {book1}")

# Cách 2: Có data dạng dict (từ API request chẳng hạn)
book_data = {
    "id": 2,
    "title": "Python Mastery",
    "author": "Author B",
    "rating": 4
}

# ❌ KHÔNG THỂ:
# book2 = Book(book_data)  # Error! __init__ cần 4 args, bạn truyền 1 dict

# ✅ DÙNG ** ĐỂ UNPACK:
book2 = Book(**book_data)  # ✅ OK!
# **book_data = id=2, title="Python Mastery", author="Author B", rating=4
print(f"Cách 2: {book2}")

print()

# ===== VÍ DỤ 3: TOÁN TỬ ** HOẠT ĐỘNG NHƯ THẾ NÀO? =====
print("===== VÍ DỤ 3: ** HOẠT ĐỘNG NHƯ THẾ NÀO? =====\n")

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

def test_function(a, b, c):
    print(f"a={a}, b={b}, c={c}")

print("Không dùng **:")
print(f"my_dict = {my_dict}")
print()

print("Dùng **:")
test_function(**my_dict)
# Tương đương với: test_function(a=1, b=2, c=3)

print()

# ===== VÍ DỤ 4: TƯƠNG ĐƯƠNG =====
print("===== VÍ DỤ 4: TƯƠNG ĐƯƠNG =====\n")

data = {"name": "Alice", "age": 25, "city": "Hanoi"}

# 3 cách này GIỐNG NHAU:
print("Cách 1: Truyền từng argument")
say_hello("Alice", 25, "Hanoi")

print("\nCách 2: Truyền bằng keyword arguments")
say_hello(name="Alice", age=25, city="Hanoi")

print("\nCách 3: Dùng ** unpack dict")
say_hello(**data)  # ← ** biến dict thành keyword arguments!

print()

# ===== VÍ DỤ 5: TẠI SAO CẦN ** TRONG UPDATE BOOK? =====
print("===== VÍ DỤ 5: TẠI SAO CẦN ** TRONG UPDATE? =====\n")

from pydantic import BaseModel

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    rating: int

# User gửi request:
request_data = BookRequest(id=1, title="New Book", author="New Author", rating=5)

print(f"request_data type: {type(request_data)}")  # BookRequest
print(f"request_data: {request_data}")

# Convert BookRequest → dict
book_dict = request_data.model_dump()  # hoặc .dict() (deprecated)
print(f"\nbook_dict: {book_dict}")
print(f"book_dict type: {type(book_dict)}")  # dict

# ❌ KHÔNG THỂ: Book(book_dict) → Error!
# ✅ PHẢI DÙNG: Book(**book_dict) → OK!

book_obj = Book(**book_dict)
print(f"\nbook_obj: {book_obj}")
print(f"book_obj type: {type(book_obj)}")  # Book

print()

# ===== BONUS: TOÁN TỬ * (CHỈ 1 DẤU SAO) =====
print("===== BONUS: * VS ** =====\n")

# * = unpack LIST/TUPLE thành positional arguments
numbers = [1, 2, 3]

def add(x, y, z):
    return x + y + z

print(f"numbers: {numbers}")
print(f"add(*numbers) = {add(*numbers)}")  # add(1, 2, 3)

# ** = unpack DICT thành keyword arguments
person = {"name": "Bob", "age": 30, "city": "Saigon"}
print(f"\nperson: {person}")
say_hello(**person)  # say_hello(name="Bob", age=30, city="Saigon")

print()

# ===== TÓM TẮT =====
print("=" * 50)
print("TÓM TẮT:")
print("=" * 50)
print("* (1 dấu sao)  → Unpack LIST/TUPLE")
print("               → Thành positional arguments")
print("               → Ví dụ: func(*[1,2,3]) = func(1,2,3)")
print()
print("** (2 dấu sao) → Unpack DICTIONARY")
print("               → Thành keyword arguments")
print("               → Ví dụ: func(**{'a':1,'b':2}) = func(a=1,b=2)")
print("=" * 50)

from fastapi import Body, FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field 
from typing import Optional 
from starlette import status

app = FastAPI()

class Book:
    id : int
    title : str
    author : str
    description : str
    rating : int
    published_date : int

    def __init__(self, id,title,author,description, rating,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id : Optional[int] = Field(description = 'ID is not needed on create', default = None)
    title : str = Field(min_length = 3)
    author : str = Field(min_length = 5)
    description : str = Field(min_length= 3, max_length = 100)
    rating : int = Field(gt=0, lt=6)  # Rating từ 1-5 ko dùng min-max vì thg khưa pydantic ko thích e nó
    # rating : int = Field(min_length= 3, max_length = 100)
    published_date : int = Field(ge=1000, le=2030)  # Năm từ 1000-2030

    model_config = {
        "json_schema_extra":{
            "example": {
                "title" : "A New book",
                "author" : "codingwithHieu",
                "description" : "A new description of a book",
                "rating" : 0,
                "published_date": 1999
            }
        }
    }


BOOKS = [
    Book(1, "My idol is S-MTP", "Gia Han", "Author is writting about favorite artist", 5,2024),
    Book(2, "Hieu Yeu Han", "Hieudepzai", "Technology book about modern programming", 4,2025),
    Book(3, "Computer Science Pro", "Author Three", "Deep dive into algorithms and data structures", 5,1990),
    Book(4, "Math for Everyone", "Author Four", "Mathematical concepts made simple", 3,2010),
    Book(5, "Science Fiction", "Author Five", "An exciting journey through space and time", 4,2020),
    Book(6, "History of Vietnam", "Author Six", "Complete history from ancient to modern times", 5,1999),
    Book(7, "History of Han", "Author Seven", "Han oiuii", 5,1999)
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books ():
    return BOOKS

"""
PATH vs QUERY PARAMETER:
- Path Parameter: Lấy 1 kết quả cụ thể -> trả về Object
- Query Parameter: Lọc nhiều kết quả -> trả về List
"""

# - get books with rating > 4
@app.get("/books/rating/" ,status_code=status.HTTP_200_OK)
async def get_books_by_rating(rating : int = Query(gt=0, lt=6)):
    book_to_return = [] 

    for book in BOOKS:
        if book.rating >= rating:
            book_to_return.append(book)
    
    return book_to_return

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id : int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    
    raise HTTPException(status_code=404, detail= 'Item not found')

# validation : xác thực
@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    
    # book.id = BOOKS[-1].id + 1 if len(BOOKS) > 0 else 1

    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    return book

# update book
@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False    
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

# delete book
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False  
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')   
# assignment
@app.get("/books/published_date/", status_code=status.HTTP_200_OK)
async def get_published_date(published_date: int = Query(gt=1000, lt=2030) ):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return
"""
Author: Hieu Nguyen
FastAPI Basics - Books API Example"""

from fastapi import Body,FastAPI

app = FastAPI() # use component 

@app.get("/") #decorator này dùng để đánh dấu hàm bên dưới là một API endpoint dạng GET.
async def first_api():
    return {'messlove': 'Han yeu Hieu!'}

BOOKS = [
    {'title': 'My idol is S MTP', 'author': 'Gia Han', 'category': 'storytelling'},
    {'title': 'Hieu Yeu Han', 'author': 'Hieudepzai', 'category': 'technology'},
    {'title': 'Han Khong Thich Hieu', 'author': 'Hieudepzai', 'category': 'sadstory'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five' ,'category': 'science'},
    {'title': 'Title Six', 'author': 'Author Six', 'category': 'math'}
]

@app.get("/books") #decorator này dùng để đánh dấu hàm bên dưới là một API endpoint dạng GET.
async def read_all_books():
    return BOOKS

# @app.get("/books/") 
# async def read_category_query_books(category : str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('category').casefold() == category.casefold():
#             books_to_return.append(book)
#     return books_to_return

# @app.get("/books/{book_author}/")
# async def read_author_category_by_query(book_author: str, category: str):
#     books_to_return = []
#     for book in BOOKS: 
#         if book.get('author').casefold() == book_author.casefold() \
#             and book.get('category').casefold() == category.casefold():
#             books_to_return.append(book)
    
#     return books_to_return

"""Assignment: 1.Create a new API Endpoint that can fetch all books from a specific author
 using either Path Parameters or Query Parameters.
 """
# Path Parameter
# @app.get("/books/by_author/{author_name}")
# async def read_author_by_path(author_name:str):
#     books_to_return =[]
#     for i in range(len(BOOKS)):
#         if BOOKS[i].get('author').casefold() == author_name.casefold():
#             books_to_return.append(BOOKS[i])
#     return books_to_return

# Query Parameter
@app.get("/books/author/")
async def read_author_by_query(author_name:str):
    books_to_return =[]
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold() == author_name.casefold():
            books_to_return.append(BOOKS[i])
    return books_to_return

@app.get("/books/{title_book}") 
async def read_books(title_book : str):
    for book in BOOKS:
        if book.get('title').casefold() == title_book.casefold():
            return book
    return {'message': 'Book not found'}

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    # print(BOOKS)
    return BOOKS

@app.put("/books/update_book/")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            return BOOKS[i]


@app.delete("/books/delete_book/{title_book}")
async def delete_book(title_book: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == title_book.casefold():
            deleted_book = BOOKS.pop(i)
            return {'message': 'Deleted book successfully!', 'book': deleted_book}
    return {'message': 'Book not found, cannot delete!'}


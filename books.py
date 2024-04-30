from fastapi import Body, FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    category: str


BOOKS = [
    {"title": "title one", "author": "author1", "category": "science"},
    {"title": "title two", "author": "author2", "category": "art"},
    {"title": "title three", "author": "author3", "category": "bio"},
    {"title": "title four", "author": "author4", "category": "science"},
    {"title": "title five", "author": "author5", "category": "art"},
]


@app.get("/books", response_model=List[Book], tags=["Books"])
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}", response_model=Book, tags=["Books"])
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books/", response_model=List[Book], tags=["Books"])
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.get("/books/by_author/", response_model=List[Book], tags=["Books"])
async def read_all_books_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return


@app.get("/books/{book_author}/", response_model=List[Book], tags=["Books"])
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
                book.get("author").casefold() == book_author.casefold()
                and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book", tags=["Books"])
async def create_book(book: Book = Body()):
    BOOKS.append(book.dict())


@app.put("/books/update_book", tags=["Books"])
async def update_book(book: Book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book.title.casefold():
            BOOKS[i].update(book.dict())


@app.delete("/books/delete_book/{book_title}", tags=["Books"])
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


@app.get("/books/by_author/{author}", response_model=List[Book], tags=["Books"])
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return

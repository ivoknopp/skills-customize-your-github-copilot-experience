"""Starter code for the FastAPI REST API assignment.

Run locally:
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookIn(BaseModel):
    title: str
    author: str
    published_year: int


books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "published_year": 1949},
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt and David Thomas",
        "published_year": 1999,
    },
]


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: BookIn):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "published_year": book.published_year,
    }
    books.append(new_book)
    return new_book


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookIn):
    for index, existing in enumerate(books):
        if existing["id"] == book_id:
            updated = {
                "id": book_id,
                "title": book.title,
                "author": book.author,
                "published_year": book.published_year,
            }
            books[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Book not found")

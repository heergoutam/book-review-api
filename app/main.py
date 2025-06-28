from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app import models
from app.schemas import book as book_schema, review as review_schema
from app.crud import book as book_crud, review as review_crud

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Review API!"}


@app.post("/books/", response_model=book_schema.Book)
def create_book(book: book_schema.BookCreate, db: Session = Depends(get_db)):
    return book_crud.create_book(db=db, book=book)


@app.get("/books/", response_model=list[book_schema.Book])
def get_books(db: Session = Depends(get_db)):
    return book_crud.get_books(db)


# ✅ POST review for a book
@app.post("/reviews/", response_model=review_schema.ReviewOut)
def create_review(review: review_schema.ReviewCreate, db: Session = Depends(get_db)):
    return review_crud.create_review(db=db, review=review)


# ✅ GET reviews for a specific book
@app.get("/books/{book_id}/reviews/", response_model=list[review_schema.ReviewOut])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return review_crud.get_reviews_for_book(db=db, book_id=book_id)

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine, get_db
from models import Book
from schemas import BookCreate, BookOut


Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS (so frontend can fetch)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/books", response_model=list[BookOut])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@app.get("/books/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(Book).filter(Book.id == book_id).first()

@app.post("/books", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    old_book = db.query(Book).filter(Book.id == book_id).first()
    old_book.title = book.title
    old_book.author = book.author
    old_book.copies = book.copies

    db.commit()
    db.refresh(old_book)
    return old_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}

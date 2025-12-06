from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas, database

router = APIRouter(prefix="/api/books", tags=["books"])

@router.get("/", response_model=List[schemas.BookResponse])
def read_books(
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = Query(None),
    db: Session = Depends(database.get_db)
):
    try:
        return crud.get_books(db, skip=skip, limit=limit, search=search)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(database.get_db)):
    try:
        db_book = crud.get_book(db, book_id=book_id)
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    try:
        return crud.create_book(db=db, book=book)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(
    book_id: int,
    book_update: schemas.BookUpdate,
    db: Session = Depends(database.get_db)
):
    try:
        db_book = crud.update_book(db, book_id=book_id, book_update=book_update)
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{book_id}/like", response_model=schemas.BookResponse)
def like_book(book_id: int, db: Session = Depends(database.get_db)):
    try:
        db_book = crud.like_book(db, book_id=book_id)
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{book_id}/rate/{rating}", response_model=schemas.BookResponse)
def rate_book(book_id: int, rating: float, db: Session = Depends(database.get_db)):
    try:
        if rating < 0 or rating > 5:
            raise HTTPException(status_code=400, detail="Rating must be between 0 and 5")
        db_book = crud.rate_book(db, book_id=book_id, rating=rating)
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{book_id}/favorite", response_model=schemas.BookResponse)
def toggle_favorite(book_id: int, db: Session = Depends(database.get_db)):
    try:
        db_book = crud.toggle_favorite(db, book_id=book_id)
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return db_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
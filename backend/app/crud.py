from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime, timedelta
from typing import List, Optional

# Book CRUD operations
def get_books(db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None):
    query = db.query(models.Book)
    if search:
        query = query.filter(
            models.Book.title.ilike(f"%{search}%") | 
            models.Book.author.ilike(f"%{search}%")
        )
    return query.offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        **book.dict(),
        available_copies=book.copies
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book_update: schemas.BookUpdate):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    
    update_data = book_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_book, field, value)
    
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

def like_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book:
        db_book.likes += 1
        db.commit()
        db.refresh(db_book)
    return db_book

def rate_book(db: Session, book_id: int, rating: float):
    db_book = get_book(db, book_id)
    if db_book:
        total_rating = db_book.rating * db_book.rating_count + rating
        db_book.rating_count += 1
        db_book.rating = total_rating / db_book.rating_count
        db.commit()
        db.refresh(db_book)
    return db_book

def toggle_favorite(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book:
        db_book.is_favorite = not db_book.is_favorite
        db.commit()
        db.refresh(db_book)
    return db_book

# Member CRUD operations
def get_members(db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None):
    query = db.query(models.Member)
    if search:
        query = query.filter(models.Member.name.ilike(f"%{search}%"))
    return query.offset(skip).limit(limit).all()

def get_member(db: Session, member_id: int):
    return db.query(models.Member).filter(models.Member.id == member_id).first()

def create_member(db: Session, member: schemas.MemberCreate):
    db_member = models.Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def update_member(db: Session, member_id: int, member_update: schemas.MemberUpdate):
    db_member = get_member(db, member_id)
    if not db_member:
        return None
    
    update_data = member_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_member, field, value)
    
    db.commit()
    db.refresh(db_member)
    return db_member

# Borrow CRUD operations
def get_borrows(db: Session, skip: int = 0, limit: int = 100, returned: Optional[bool] = None):
    query = db.query(models.Borrow)
    if returned is not None:
        query = query.filter(models.Borrow.returned == returned)
    return query.offset(skip).limit(limit).all()

def create_borrow(db: Session, borrow: schemas.BorrowCreate):
    # Check if book is available
    db_book = get_book(db, borrow.book_id)
    if not db_book or db_book.available_copies < 1:
        return None
    
    # Create borrow record
    db_borrow = models.Borrow(**borrow.dict())
    db.add(db_borrow)
    
    # Update available copies
    db_book.available_copies -= 1
    
    db.commit()
    db.refresh(db_borrow)
    return db_borrow

def return_book(db: Session, borrow_id: int):
    db_borrow = db.query(models.Borrow).filter(models.Borrow.id == borrow_id).first()
    if not db_borrow or db_borrow.returned:
        return None
    
    # Mark as returned
    db_borrow.returned = True
    db_borrow.return_date = datetime.utcnow()
    
    # Update book copies
    db_book = get_book(db, db_borrow.book_id)
    if db_book:
        db_book.available_copies += 1
    
    db.commit()
    db.refresh(db_borrow)
    return db_borrow

# Dashboard statistics
def get_dashboard_stats(db: Session):
    total_books = db.query(models.Book).count()
    total_members = db.query(models.Member).filter(models.Member.is_active == True).count()
    
    active_borrows = db.query(models.Borrow).filter(
        models.Borrow.returned == False
    ).count()
    
    overdue_borrows = db.query(models.Borrow).filter(
        models.Borrow.returned == False,
        models.Borrow.due_date < datetime.utcnow()
    ).count()
    
    available_books = db.query(models.Book).filter(
        models.Book.available_copies > 0
    ).count()
    
    return {
        "total_books": total_books,
        "total_members": total_members,
        "active_borrows": active_borrows,
        "overdue_borrows": overdue_borrows,
        "available_books": available_books
    }
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Book schemas
class BookBase(BaseModel):
    title: str
    author: str
    published_year: Optional[int] = None
    isbn: Optional[str] = None
    copies: int = 1
    cover_id: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None
    copies: Optional[int] = None
    is_favorite: Optional[bool] = None

class Book(BookBase):
    id: int
    available_copies: int
    likes: int
    rating: float
    rating_count: int
    is_favorite: bool
    
    class Config:
        from_attributes = True

# Member schemas
class MemberBase(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class MemberCreate(MemberBase):
    pass

class MemberUpdate(MemberBase):
    is_active: Optional[bool] = None

class Member(MemberBase):
    id: int
    join_date: datetime
    is_active: bool
    
    class Config:
        from_attributes = True

# Borrow schemas
class BorrowBase(BaseModel):
    book_id: int
    member_id: int

class BorrowCreate(BorrowBase):
    pass

class BorrowReturn(BaseModel):
    returned: bool = True

class Borrow(BorrowBase):
    id: int
    borrow_date: datetime
    return_date: Optional[datetime]
    due_date: datetime
    returned: bool
    
    class Config:
        from_attributes = True

class BorrowWithDetails(Borrow):
    book: Book
    member: Member

# Dashboard stats
class DashboardStats(BaseModel):
    total_books: int
    total_members: int
    active_borrows: int
    overdue_borrows: int
    available_books: int
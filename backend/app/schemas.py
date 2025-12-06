from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
import re

# Email validation pattern
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

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

# Member schemas with custom email validation
class MemberBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if v is None or v == "":
            return v
        if not EMAIL_REGEX.match(v):
            raise ValueError('Invalid email format')
        return v

class MemberCreate(MemberBase):
    pass

class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_active: Optional[bool] = None
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if v is None or v == "":
            return v
        if not EMAIL_REGEX.match(v):
            raise ValueError('Invalid email format')
        return v

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
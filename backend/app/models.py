from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_year = Column(Integer)
    isbn = Column(String, unique=True, nullable=True)
    copies = Column(Integer, default=1)
    available_copies = Column(Integer, default=1)
    likes = Column(Integer, default=0)
    rating = Column(Float, default=0.0)
    rating_count = Column(Integer, default=0)
    is_favorite = Column(Boolean, default=False)
    cover_id = Column(String, nullable=True)
    
    borrows = relationship("Borrow", back_populates="book")

class Member(Base):
    __tablename__ = "members"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)
    join_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    borrows = relationship("Borrow", back_populates="member")

class Borrow(Base):
    __tablename__ = "borrows"
    
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    member_id = Column(Integer, ForeignKey("members.id"))
    borrow_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)
    due_date = Column(DateTime, default=lambda: datetime.utcnow().replace(day=datetime.utcnow().day + 14))
    returned = Column(Boolean, default=False)
    
    book = relationship("Book", back_populates="borrows")
    member = relationship("Member", back_populates="borrows")
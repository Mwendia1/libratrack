from pydantic import BaseModel
from typing import Optional

# BOOK SCHEMAS
class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass  # inherits title and author

class BookOut(BookBase):
    id: int
    available: bool

    class Config:
        orm_mode = True

# MEMBER SCHEMAS
class MemberBase(BaseModel):
    name: str
    email: str

class MemberCreate(MemberBase):
    pass

class MemberOut(MemberBase):
    id: int

    class Config:
        orm_mode = True

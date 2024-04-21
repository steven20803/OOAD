from sqlmodel import SQLModel, Field, Column, Integer, ForeignKey
from .user import User
from typing import Optional
from datetime import datetime

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    book_name: str = Field(...)
    author: str = Field(...)
    borrowed: bool = Field(default=False)
    borrower_id: int = Column(Integer, ForeignKey('user.id'))
    last_borrowed: Optional[datetime] = Field(default=None)
    status: bool = Field(default=True)
    comments: str = Field(default="")
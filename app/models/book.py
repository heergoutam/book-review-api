# app/models/book.py

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base_class import Base  # ✅ fixed import

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_at = Column(DateTime(timezone=True), server_default=func.now())
    reviews = relationship("Review", back_populates="book", cascade="all, delete")


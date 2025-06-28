from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    book_id = Column(Integer, ForeignKey("books.id"))

    book = relationship("Book", back_populates="reviews")

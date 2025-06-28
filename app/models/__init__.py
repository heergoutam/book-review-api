from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_at = Column(DateTime(timezone=True), server_default=func.now())

    reviews = relationship("Review", back_populates="book", cascade="all, delete")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    reviewer_name = Column(String, nullable=False)
    review_text = Column(String)
    rating = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    book = relationship("Book", back_populates="reviews")

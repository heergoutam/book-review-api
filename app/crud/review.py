from sqlalchemy.orm import Session
from app.models import review as models
from app.schemas import review as schemas


def create_review(db: Session, review: schemas.ReviewCreate):
    db_review = models.Review(**review.model_dump())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_reviews_for_book(db: Session, book_id: int):
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()

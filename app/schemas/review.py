from pydantic import BaseModel
from datetime import datetime

class ReviewBase(BaseModel):
    content: str
    rating: int

class ReviewCreate(ReviewBase):
    book_id: int

class ReviewOut(ReviewBase):
    id: int
    book_id: int
    created_at: datetime

    class Config:
        from_attributes = True  # or orm_mode = True for Pydantic v1

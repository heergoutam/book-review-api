import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add this line (make sure it matches your environment variable setup)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./db.sqlite3")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

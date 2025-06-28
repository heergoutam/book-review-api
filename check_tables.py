# check_tables.py

from sqlalchemy import create_engine, inspect
from app.db.session import DATABASE_URL

engine = create_engine(DATABASE_URL)
inspector = inspect(engine)

tables = inspector.get_table_names()

print("✅ Tables found in the database:")
for table in tables:
    print(f"  - {table}")

if "books" in tables and "reviews" in tables:
    print("\n🎉 All required tables are present!")
else:
    print("\n❌ Missing required tables. Did you run `alembic upgrade head`?")

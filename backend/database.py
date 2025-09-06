from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from typing import Generator

from config import settings

from models import Base


# PostgreSQL doesn't need check_same_thread, that's SQLite specific
if "sqlite" in settings.database_url:
    engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})
else:
    engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db_and_tables():
    Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

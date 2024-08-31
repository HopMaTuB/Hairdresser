from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo = True)

SessionLocal = sessionmaker(
    autocommit = False, 
    autoflush = False, 
    bind = engine
    )

# create a new session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
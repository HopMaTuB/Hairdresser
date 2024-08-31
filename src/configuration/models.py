from sqlalchemy import (
    Column,Integer,String,Date,Boolean,DateTime,func
    )
from sqlalchemy.orm import declarative_base
from src.configuration.database import engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, nullable=False)
    first_name = Column(String(20), unique=False, index=True, nullable=False)
    last_name = Column(String(30), unique=False, index=True, nullable=True)
    email = Column(String(250), unique=True, index=True,nullable=False)
    password = Column(String(250), unique=False, index=False,nullable=False)
    phone_number = Column(String, unique=False, index=False,nullable=False)
    date_of_birth = Column(Date, unique=False, index=False, nullable=True)
    refresh_token = Column(String,nullable=True)
    confirmed = Column(Boolean,default=False)
    created_at = Column('created_at',DateTime,default=func.now())
    update_at = Column('update_at',)


Base.metadata.create_all(bind=engine)
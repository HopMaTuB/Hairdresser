import os
from fastapi_mail import ConnectionConfig
from pathlib import Path
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from slowapi.util import get_remote_address
from slowapi import Limiter

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
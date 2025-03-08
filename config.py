import os

class Config: 
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey123")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "postgresql://postgres:1234@localhost/authentication_db")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

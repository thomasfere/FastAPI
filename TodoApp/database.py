import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

SQL_ALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if SQL_ALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQL_ALCHEMY_DATABASE_URL = SQL_ALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)


engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URI', 'postgresql://jlgndebprlyugb:3b66cd2e28f6946b3b7d8d29e1db5c74f391999b0fd2f719b85d4880f6434a5d@ec2-3-211-37-117.compute-1.amazonaws.com:5432/dbo1gur14bbdom')


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
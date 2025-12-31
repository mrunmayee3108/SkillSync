from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = "sqlite:///./test.db"

engine = create_engine(
    database_url, 
    connect_args = {"check_same_thread": False}     # needed when handling multiple user requests simultaneously
)

SessionLocal = sessionmaker(bind = engine, autocommit = False)

Base = declarative_base()
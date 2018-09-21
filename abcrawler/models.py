from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import sys
import abcrawler.settings
from datetime import datetime,date

DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(URL(**abcrawler.settings.DATABASE))

def create_quotes_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class QuoteItem(DeclarativeBase):
    __tablename__ = "quotes"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    quote=Column('quote',String(1000))
    author=Column('author',String(255))
    tag=Column('tag',String(500),nullable=True)
    created_date =Column('created_date',DateTime,nullable=True)

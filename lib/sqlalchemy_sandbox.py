#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
   # pass
   __tablename__ = 'students'
   
   id = Column(Integer, primary_key=True)
   name = Column(String())

if __name__ == '__main__':
    #pass
    engine = create_engine('sqite:///students.db')
    Base.metadate.create_all(engine)
    
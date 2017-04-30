import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Beer(Base):
    __tablename__ = 'beer'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class BeerName(Base):
    __tablename__ = 'beer_name'

    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    beer_id = Column(Integer,ForeignKey('beer.id'))
    beer = relationship(Beer) 
 

engine = create_engine('sqlite:///beer.db')
Base.metadata.create_all(engine)

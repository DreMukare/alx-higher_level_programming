#!/usr/bin/python3
'''
contains class definition of a state and an instance
Base = declarative_base()
'''

from sys import argv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    maps to table states
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

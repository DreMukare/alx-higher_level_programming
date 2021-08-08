#!/usr/bin/python3
'''
contains class definition of a state and an instance
Base = declarative_base()
'''

from sys import argv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine,
    Column,
    Integer,
    String)

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3],)
        pool_pre_ping=True)
    Base = declarative_base()

    class State(Base):
        '''
        maps to table states
        '''
        __tablename__ = 'states'
        id = Column(Integer,
                    autoincrement=True,
                    unique=True,
                    nullable=False,
                    primary_key=True)
        name = Column(String(128), nullable=False)
    Base.metadata.create_all(bind=engine)

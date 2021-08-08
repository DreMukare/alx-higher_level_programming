#!/usr/bin/python3
'''
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)
    session.commit()
    session.close()

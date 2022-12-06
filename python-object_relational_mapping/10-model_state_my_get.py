#!/usr/bin/python3
""" Lists State objects passed on param from the database
    using SQLAlchemy
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'\
             .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    s = Session()
    flag = 0

    for state in s.query(State).all():
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            flag = 0
            break
        else:
            flag = 1
    if flag:
        print('Not found')

    s.close()

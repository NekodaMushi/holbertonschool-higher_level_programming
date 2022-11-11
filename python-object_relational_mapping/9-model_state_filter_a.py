
#!/usr/bin/python3
""" Lists all State objects containing 'a'  from the database
    using SQLAlchemy
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'\
             .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    s = Session()

    req = s.query(State).order_by(State.id).all()
    for state in req:
        if 'a' in state.name:
            print('{}: {}'.format(state.id, state.name))

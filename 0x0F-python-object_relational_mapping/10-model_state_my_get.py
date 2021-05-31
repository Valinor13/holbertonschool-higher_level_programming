#!/usr/bin/python3

"""Create a session for database access"""


import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State)

    try:
        for state in states:
            if len(state.name) == 0:
                sig = 1
                break
            elif state.name == sys.argv[4]:
                print(state.id)
                sig = 0
                break
            else:
                sig = 1
    except:
        sig = 1
    if sig == 1:
        print("Not found")

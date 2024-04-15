#!/usr/bin/python3
"""Gets the first state from database"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    sql_user = argv[1]
    sql_pass = argv[2]
    sql_db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sql_user, sql_pass, sql_db))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()

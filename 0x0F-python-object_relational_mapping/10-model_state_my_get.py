#!/usr/bin/python3
"""Prinst the id of the state passed as argument"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 5:
        print(
            "Usage: {} username password database_name state_name"
            .format(argv[0]))
        exit(1)
    sql_username = argv[1]
    sql_password = argv[2]
    sql_db = argv[3]
    state_name = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sql_username, sql_password, sql_db),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()

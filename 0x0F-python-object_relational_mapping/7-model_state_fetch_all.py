#!/usr/bin/python3
"""List all states from the database"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    sql_username = argv[1]
    sql_password = argv[2]
    sql_db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sql_username, sql_password, sql_db),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).all()

    for state in result:
        print("{}: {}".format(state.id, state.name))

    session.close()

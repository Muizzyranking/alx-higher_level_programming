#!/usr/bin/python3
"""List states with 'a' in the name"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    sql_user = argv[1]
    sql_pass = argv[2]
    sql_db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sql_user, sql_pass, sql_db),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    for state in result:
        print("{}: {}".format(state.id, state.name))
    session.close()

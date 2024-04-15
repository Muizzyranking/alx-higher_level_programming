#!/usr/bin/python3

"""Changes the name of an object"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    update_state = session.query(State).filter_by(id=2).first()
    update_state.name = "New Mexico"
    session.commit()
    session.close()

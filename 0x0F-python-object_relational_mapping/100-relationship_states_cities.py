#!/usr/bin/python3
"""Creates a state with a city"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    sql_user = argv[1]
    sql_pass = argv[2]
    sql_db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sql_user, sql_pass, sql_db),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()

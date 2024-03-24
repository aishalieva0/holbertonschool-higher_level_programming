#!/usr/bin/python3
"""
lists all State objects
corresponding City objects
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    usr = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pswd, db))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print("{}: {}"
              .format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))


if __name__ == "__main__":
    main()

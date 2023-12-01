from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Airport" table
class Airport(base):
    __tablename__ = "Airport"
    id = Column(Integer, primary_key=True)
    code = Column(String)
    airport = Column(String)
    city = Column(String)
    country = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass deinfed above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# delete all records
# airports = session.query(Airport)
# for airport in airports:
#     session.delete(airport)

# create records for the Airport table
# lhr = Airport(
#     code="LHR",
#     airport="London Heathrow",
#     city="London",
#     country="UK"
# )

# lgw = Airport(
#     code="LGW",
#     airport="London Gatwick",
#     city="London",
#     country="UK"
# )

# brs = Airport(
#     code="BRS",
#     airport="Bristol",
#     city="Bristol",
#     country="UK"
# )

# jfk = Airport(
#     code="JFK",
#     airport="New York JFK",
#     city="New York",
#     country="USA"
# )

# add records to the table
# session.add(lhr)
# session.add(lgw)
# session.add(brs)
# session.add(jfk)


# create record function
def create_record():
    airport_code = input("Airport code: ")
    airport_name = input("Airport name: ")
    airport_city = input("City: ")
    airport_country = input("Country: ")
    airport = Airport(
        code=airport_code,
        airport=airport_name,
        city=airport_city,
        country=airport_country
    )
    print("Airport created")
    session.add(airport)
    session.commit()


# read airport function
def read_record():
    airports = session.query(Airport)
    for airport in airports:
        print(
            airport.id,
            airport.code,
            airport.airport,
            airport.city,
            airport.country,
            sep=" | "
        )


# update airport function
def update_record():
    airport_code = input("Enter airport code: ")
    airport = session.query(Airport).filter_by(code=airport_code).first()
    if airport is not None:
        print("Updating the following record:")
        print(
            airport.id,
            airport.code,
            airport.airport,
            airport.city,
            airport.country,
            sep=" | "
        )
        code = input("Airport code: ")
        name = input("Airport name: ")
        city = input("City: ")
        country = input("Country: ")
        print("Airport updated")
        airport.code = code
        airport.airport = name
        airport.city = city
        airport.country = country
        session.commit()
    else:
        print("Airport not found")


# function to delete record
def delete_record():
    airport_code = input("Enter airport code: ")
    airport = session.query(Airport).filter_by(code=airport_code).first()
    if airport is not None:
        print("About to delete the following record:")
        print(
            airport.code,
            airport.airport,
            airport.city,
            airport.country,
            sep=" | "
        )
        option = input("Delete record? (y/n): ")
        if option.lower() == "y":
            session.delete(airport)
            session.commit()
        else:
            print("Airport NOT deleted")
    else:
        print("Airport not found")


# options to CRUD table
while True:
    option = input(
        "Would you like to (c)reate,(r)ead,(u)pdate or (d)elete a record? ")
    if option.lower() == "c":
        create_record()
    elif option.lower() == "r":
        read_record()
    elif option.lower() == "u":
        update_record()
    elif option.lower() == "d":
        delete_record()
    else:
        print(option)


# commit the updates
# session.commit()

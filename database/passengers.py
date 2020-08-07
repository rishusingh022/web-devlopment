import os#operating system libraries

from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:1234@localhost/postgres")
#engine is object which is used 
#here to make connection with database
db = scoped_session(sessionmaker(bind=engine))
#keppind different session for different person

flight = db.execute("SELECT id, origin, destination, duration FROM flight").fetchall()

for obj in flight:
    print(f"Flight {obj.id}: {obj.origin} to {obj.destination}, {obj.duration} minutes.")
    #that was selecting
    #data from the data abs
    #prompt the useer for input to choose the flight

flight_id=int(input("\n Flight_id: "))

flight=db.execute("SELECT origin,destination,duration FROM flight where id=:id",{"id": flight_id}).fetchone()#fetching only one thing

if obj is None:
	print("Error: no such flight")
	 #list passengers
passengers=db.execute("SELECT name FROM passengers where flight_id=:flight_id",{"flight_id":flight_id}).fetchall()
print("\nPAassengers")
for passenger in passengers:
	print(passenger.name)

if len(passengers)==0:
	print("no passengers")
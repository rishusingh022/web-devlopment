import os#operating system libraries

from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:1234@localhost/postgres")
#engine is object which is used 
#here to make connection with database
db = scoped_session(sessionmaker(bind=engine))
#keppind different session for different person


flight = db.execute("SELECT * FROM flight").fetchall()
for obj in flight:
      print(f"{obj.origin} to {obj.destination}, {obj.duration} minutes.")
      #that was selecting
      #data from the data abse
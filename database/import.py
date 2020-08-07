import csv#comma seperated values
import os#operating system libraries

from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:1234@localhost/postgres")
#engine is object which is used 
#here to make connection with database
db = scoped_session(sessionmaker(bind=engine))
#keppind different session for different person

def main():
	f=open("flight.csv")#BUILD IN file specifically for reading csv file from the computer
	reader=csv.reader(f)#i want to read f as a csv file
	for origin,destination,duration in reader:#looping
		db.execute("INSERT INTO flight (origin,destination,duration) VALUES(:origin,:destination,:duration)",
			        {"origin":origin,"destination":destination,"duration":duration})
		print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
	db.commit()#sqlalchemy running and making changes throgh db.commit otherwise we 
	#have to run actual queries

if __name__=="__main__":
	main()

        
       
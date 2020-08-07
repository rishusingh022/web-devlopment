import csv#comma seperated values
import os#operating system libraries

from flask import Flask,render_template,request
from models import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:1234@localhost/rishu"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)

def main():
	f=open("flight.csv")#BUILD IN file specifically for reading csv file from the computer
	reader=csv.reader(f)#i want to read f as a csv file
	for origin,destination,duration in reader:
		flight=Flight(origin=origin,destination=destination,duration=duration)#yaha per  class ka object banaya hai
		db.session.add(flight)#this add the data obtained to our database
		print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
	db.session.commit()#sqlalchemy running and making changes throgh db.commit otherwise we 
	#have to run actual queries

if __name__=="__main__":
	with app.app_context():
		main()
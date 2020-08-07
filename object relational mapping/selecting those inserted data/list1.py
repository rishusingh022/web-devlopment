import os#operating system libraries

from flask import Flask,render_template,request
from models import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:1234@localhost/rishu"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)

def main():
    flights = Flight.query.all()
    for f in flights:
        print(f"{f.origin} to {f.destination}, {f.duration} minutes.") 

if __name__=="__main__":
	with app.app_context():
		main()
#slect ki jagah ye use kiya hai orm me yahii karte hai 
    #object ke sath relate karke querry insert sab karskate hai jo ham normal scoped session
    #valee ke sath kar rahe the		
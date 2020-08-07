from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Flight(db.Model):

	__tablename__="flights"
	id=db.Column(db.Integer, primary_key=True)
	origin=db.Column(db.String,nullable=False)
	destination=db.Column(db.String,nullable=False)
	duration=db.Column(db.Integer,nullable=False)


class passenger(db.Model):
	__tablename__="passengers"
	id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String,nullable=False)
	flight_id=db.Column(db.Integer,db.ForeignKey("flights.id"),nullable=False)
	#we have just write now created two classes and connected them eith the help
	#foreignkey just like we have done through postgres this time using python 
	#class to do so

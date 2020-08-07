from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Flight(db.Model):

	__tablename__="flights"
	id=db.Column(db.Integer, primary_key=True)
	origin=db.Column(db.String,nullable=False)
	destination=db.Column(db.String,nullable=False)
	duration=db.Column(db.Integer,nullable=False)
	passenger=db.relationship("passenger",backref="flight",lazy=True)
	#agar hamre pass flight object hoga toh ham uske thorugh passengers ko bhi access kar skate hai
	#lazy 
	def add_passenger(self,name):
		p=passenger(name=name,flight_id=self.id)
		db.session.add(p)
		db.session.commit()


class passenger(db.Model):
	__tablename__="passengers"
	id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String,nullable=False)
	flight_id=db.Column(db.Integer,db.ForeignKey("flights.id"),nullable=False)
	#we have just write now created two classes and connected them eith the help
	#foreignkey just like we have done through postgres this time using python 
	#class to do so

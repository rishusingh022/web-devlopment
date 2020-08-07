import os

from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

app=Flask(__name__)

engine=create_engine("postgresql://postgres:1234@localhost/postgres")
db=scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
	flight=db.execute("SELECT * FROM flight").fetchall()
	return render_template("index.html",flight=flight)

@app.route("/book", methods=["POST"])
def book():
	"""book a flight."""
	#get the infomation from user
	name=request.form.get("name")
	try:
		flight_id=int(request.form.get("flight_id"))
	except ValueError:
		return render_template("error.html",message="Invalid flight number.")
	# Make sure the flight exists.
	if db.execute("SELECT * FROM flight WHERE id = :id", {"id": flight_id}).rowcount== 0:
		return render_template("error.html", message="No such flight with that id.")
	db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
	        {"name": name, "flight_id": flight_id})
	db.commit()
	return render_template("success.html")

@app.route("/flight")
def flight():
	"""list of all the flight."""
	flight=db.execute("SELECT * FROM flight").fetchall()
	return render_template("flights.html",flight=flight)

@app.route("/flight/<int:flight_id>")
def flights(flight_id):
	"""list details of a particular flight"""
	#make sure flight exits

	flight = db.execute("SELECT * FROM flight WHERE id = :id", {"id": flight_id}).fetchone()
	if flight is None:
		return render_template("error.html", message="No such flight.")

	# Get all passengers.
	passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
		                    {"flight_id": flight_id} ).fetchall()
	return render_template("flight.html", flight=flight, passengers=passengers)

if __name__ =="__main__":
	main()
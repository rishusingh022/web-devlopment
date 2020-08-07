from time import sleep
from flask import jsonify # <- `jsonify` instead of `json`
from flask import Flask,render_template,request
from models import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:1234@localhost/rishu"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)


@app.route("/")
def index():
	flight=Flight.query.all()
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
	flight=Flight.query.get(flight_id)
	if flight is None:
		return render_template("error.html", message="No such flight with that id.")
	#add passengers
	flight.add_passenger(name)
	return render_template("success.html")

@app.route("/flight")
def flight():
	"""list of all the flight."""
	flight=Flight.query.all()
	return render_template("flights.html",flight=flight)

@app.route("/flight/<int:flight_id>")
def flights(flight_id):
	"""list details of a particular flight"""
	#make sure flight exits

	flight = Flight.query.get(flight_id)
	if flight is None:
		return render_template("error.html", message="No such flight.")

	# Get all passengers.
	passengers = flight.passenger
	return render_template("flight.html", flight=flight, passengers=passengers)



@app.route("/api/flight/<int:flight_id>")

def flight_api(flight_id):
	"""Return details about a single flight."""
	# Make sure flight exists.
	flight = Flight.query.get(flight_id)
	if flight is None:
		return jsonify({"error": "Invalid flight_id"}), 422

	# Get all passengers.
	passengers = flight.passenger
	names = []
	for passenger in passengers:
		names.append(passenger.name)
	return jsonify({
		"origin": flight.origin,
		"destination": flight.destination,
		"duration": flight.duration,
		"passengers": names
		})	



if __name__ =="__main__":
	main()
from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
	return "hello world"

@app.route("/<string:name>")
def hello(name):
	name = name.capitalize()
	return f"hello, {name}!"
from flask import Flask

app=Flask(__name__)#create a flask application
@app.route("/")#part of url
def index():
	return"hello world!"
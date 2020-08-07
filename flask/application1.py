from flask import Flask

app=Flask(__name__)#create a flask application
@app.route("/")#part of url
def index():
	return"hello world!"
@app.route("/swapnil")
def swapnil():
	return"15 rupyee swapnil bhai sexy!"

@app.route("/devansh")
def devansh():
	return"bha keh de riya de apne dil ki baat!"
@app.route("/archit")
def archit():
	return"padhna start karde bsdk"
@app.route("/arpit")
def arpit():
	return"bhai ek bhabhi set karle apne liye"			


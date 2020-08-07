from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/hello" ,methods=["GET","post"])
def hello():
	if request.method=="GET":
		return"plz fill the form instead"
	else:	
		name=request.form.get("name")
		return render_template("hello.html",name=name)
		#pahle jitte bhi appllication banaye the usme ham get kar rahe the kyuki 
	#kyuki usme information chahiye thi
	#per isme post kar rahee hai kyuki isme informtion bhej rahe hai

if __name__=="__main__":	
    app.run()
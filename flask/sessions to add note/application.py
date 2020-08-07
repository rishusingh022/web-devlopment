from flask import Flask, render_template, request, session
from flask_session import Session

app=Flask(__name__)

app.config["SESSION_PERMANENT"]= False
app.config["SESSION_TYPE"]= "filesystem"
Session(app)

notes=[]

@app.route("/" ,methods=["GET","POST"])
def index():
	if request.method=="POST":
	    note=request.form.get("note")
	    notes.append(note)

	return render_template("index.html",notes=notes)
		#pahle jitte bhi appllication banaye the usme ham get kar rahe the kyuki 
	#kyuki usme information chahiye thi
	#per isme post kar rahee hai kyuki isme informtion bhej rahe hai

if __name__=="__main__":	
    app.run()
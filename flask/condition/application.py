import datetime

from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
	now=datetime.datetime.now()
	new_year= now.month ==1 and now.day ==1
	new_year= True
	return render_template("index.html",new_year=new_year) 
#JINGA 2 WAY OF USING CONDITIOM
#no trace of the date and time in the page source means what are actual code are is still hidden



if __name__=="__main__":	
    app.run()
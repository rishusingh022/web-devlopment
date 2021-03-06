from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
	headline="hello,world!"
	return render_template("index.html",headline=headline)
	#headline will be enclosed in double curly braces and value that will be suubstituted from here only
	#jinja 2 way of putting values 

@app.route("/bye")
def bye():
	headline="goodbye!"
	return render_template("index.html",headline=headline)

if __name__=="__main__":	
    app.run()
from flask import Flask, request, render_template, redirect
import pickle
import csv

app = Flask(__name__)
students = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/auth', methods=['POST','GET'])
def hello_world():
    return render_template("auth.html")

database={'khushal': '1234' , 'khush' :'1234' , 'Khushal' : '1234' }

with open("registered.csv", "r") as file :
        reader = csv.reader(file)
        students = list(reader)


@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('auth.html',info='Invalid Username')
    else:
        if database[name1]!=pwd:
            return render_template('auth.html',info='Invalid Username or Password')
        else:
	        return render_template("registered.html", students = students ,name=name1)

@app.route("/registered")
def registered():
    if not request.form.get("username") or not request.form.get("password"):
        return render_template("auth.html")
    else:
        return render_template("registered.html", students = students)

@app.route("/register" , methods = ["POST"])
def register():

    if not request.form.get("name") or not request.form.get("Course"):
        return "failure"

    with open("registered.csv", "a") as file :
        writer = csv.writer(file)
        writer.writerow((request.form.get("name"), request.form.get("email"), request.form.get("Course")))
    return redirect("/registered")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, redirect, url_for, request 
import mysql.connector 
import os 
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('Apple.csv')

plt.title("Electricity consumption and total CO2 emission over 5 years for each product")
plt.xlabel("Year5_kWh")
plt.ylabel("Year5_CO2e")
plt.show()

db = mysql.connector(
    user="localhost",
    password="root",
)

database = os.path.dirname(os.path.abspath(__file__))

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method=="POST":
        name = request.form["name"]
        lastname = request.form["lastname"]
        password = request.form["password"]

    return render_template("register.html")

cur=mysql.connector("/data.sql")
cur=mysql.commit()
cur=mysql.close()

@app.route("/login", methods=["GET", "POST"])   
def login():
    if request.method=="POST":
        name = request.form["name"]
        lastname = request.form["lastname"]
        password = request.form["password"]   

    return render_template("login.html")
cur=mysql.connector("/data.sql")
cur=mysql.commit()
cur=mysql.close()
cur=mysql.fetchall()


if __name__=='__main__':
    app.run(debug=True)    




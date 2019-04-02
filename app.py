from flask import Flask, request, render_template, redirect, url_for
import requests
import json
import pyrebase

config = {
    "apiKey": "AIzaSyD90J2SBHbXM1w475rrET4zi_uCQQt0osE",
    "authDomain": "python-72493.firebaseapp.com",
    "databaseURL": "https://python-72493.firebaseio.com",
    "projectId": "python-72493",
    "storageBucket": "python-72493.appspot.com",
    "messagingSenderId": "984337128335"
};

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/form", methods=['POST'])
def sendtodb():
    email = request.form['email']
    phone = request.form['phone']
    survey = request.form['survey']
    data = {"email": email, "phone": phone, "survey": survey}
    db.child("surveys").push(json.dumps(data))
    return redirect(url_for('hello'))

@app.route("/surveys")
def surveys():
    return render_template('survey.html')

@app.route("/about")
def about():
    return render_template('about.html')
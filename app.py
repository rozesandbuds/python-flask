from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/form", methods=['POST'])
def sendtodb():
    db = 'https://python-72493.firebaseio.com'
    email = request.form['email']
    phone = request.form['phone']
    survey = request.form['survey']
    data = {email: email, phone: phone, survey: survey}
    r = requests.post('https://python-72493.firebaseio.com/surveys', data=data)
    return render_template('index.html')

@app.route("/surveys")
def surveys():
    return render_template('survey.html')

@app.route("/about")
def about():
    return render_template('about.html')
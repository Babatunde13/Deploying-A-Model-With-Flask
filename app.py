from flask import Flask, render_template, request
from model import model

# print(model)

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/prediction', methods='POST')
def prediction():
    rm = request.form['RM']
    lstat = request.form['LSTAT']
    predict = model.predict([rm, lstat])
    return render_template('predicted.html', rm=rm, lstat=lstat, predict=predict)

from flask import Flask, render_template, request, url_for
from model import model

# print(model)

app = Flask(__name__)

@app.route('/prediction')
def prediction():
    
    return render_template('predicted.html')


@app.route('/')
@app.route('/home/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        rm = request.form['RM']
        lstat = request.form['LSTAT']
        predict = model.predict([rm, lstat])
        return url_for('prediction', rm=rm, lstat=lstat, predict=predict)
        # return render_template('predicted.html', rm=rm, lstat=lstat, predict=predict)

    return render_template('home.html')

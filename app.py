from flask import Flask, render_template, request, url_for
from model import model

# print(model)

app = Flask(__name__)

@app.route('/prediction')
def prediction():
    # rm, lstat, predict = (1, 1, 1)
    return render_template('predicted.html', rm=1, lstat=1, predict=1)


@app.route('/')
@app.route('/home/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        print(1)
        # rm = request.form['RM']
        # lstat = request.form['LSTAT']
        # predict = model.predict([rm, lstat])
        # print(predict)
        # return render_template(url_for('prediction', rm=rm, lstat=lstat, predict=predict))
        return render_template('predicted.html', rm=1, lstat=2, predict=3)

    return render_template('home.html')

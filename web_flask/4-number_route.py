#!/usr/bin/python3
'''starting a flask web app'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''display Hello HBNB'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    '''display HBNB'''
    return 'HBNB'


@app.route('/c/<text>')
def cisfun(text):
    ''' display text'''
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    '''display text'''
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def find_int(n):
    """display “n is a number”"""
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def templateifint(n):
    '''display template if n is int'''
    return render_template('5-number.html', N=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

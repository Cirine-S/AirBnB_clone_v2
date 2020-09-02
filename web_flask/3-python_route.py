#!/usr/bin/python3
'''starting a flask web app'''
from flask import Flask
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


@app.route('/python', strict_slashes)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    '''display text'''
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

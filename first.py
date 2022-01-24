from distutils.log import debug
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Wrld!'

@app.route('/second')
def second():
    return 'second'

@app.route('/third')
def third():
    return 'third'

app.run(debug=True)
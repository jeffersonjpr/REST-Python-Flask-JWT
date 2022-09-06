from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/greet')
def greet():
    return 'Hello there!'
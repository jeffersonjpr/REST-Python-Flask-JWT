from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/hello')
def greet():
    return 'Hello, good morning!'


#variables
@app.route('/user/<username>')
def show_username(username):
    #return 'User %s' % username
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #return 'Post %d' % post_id
    return 'Post {}'.format(post_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'
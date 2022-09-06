from flask import Flask, request
app = Flask(__name__)

@app.route('/user', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    print(username, password)
    return 'username: '
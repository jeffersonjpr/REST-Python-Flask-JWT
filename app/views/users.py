from werkzeug.security import generate_password_hash
from app import db
from flask import jsonify, request
from ..models.users import Users, user_schema, users_schema


def post_user():
    # get the post data
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    # instantiate the user model
    hashed_password = generate_password_hash(password)
    user = Users(username, hashed_password, name, email)

    try:
        # insert the user in the database
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'New user created!', 'data': result}), 201

    except Exception as e:
        return jsonify({'message': 'Something went wrong', "error": str(e)}), 500

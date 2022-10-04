import datetime
from app import db, ma


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    birth = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self,birth = birth
        self.email = email


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'name', 'birth', 'email', 'created_on')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

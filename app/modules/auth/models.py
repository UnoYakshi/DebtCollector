from flask_sqlalchemy import SQLAlchemy
import json
from app import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('uid', db.Integer, primary_key=True)
    login = db.Column('login', db.String(32), unique=True, index=True)
    first_name = db.Column('first_name', db.String(128))
    last_name = db.Column('last_name', db.String(128))
    email = db.Column('email', db.String(128), unique=True, index=True)
    password = db.Column('password', db.String(128))
    birthday = db.Column('birthday', db.Date())

    def __init__(self, login, first_name, last_name, email, password, birthday):
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.birthday = birthday

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.login)

    def to_json(self):
        res = conn.execute(select([self]))
        return json.dumps([dict(r) for r in res])

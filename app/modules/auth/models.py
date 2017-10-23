#! ~DebtCollector/app/modules/auth/models.py

from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
import json

import app


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('uid', db.Integer, primary_key=True, autoincrement=True)
    login = db.Column('login', db.String(32), unique=True, index=True)
    first_name = db.Column('first_name', db.String(128))
    last_name = db.Column('last_name', db.String(128))
    email = db.Column('email', db.String(128), unique=True, index=True)
    pwdhash = db.Column('password', db.String(128), unique=True)
    birthdate = db.Column('birthdate', db.Date())

    def __init__(self, login, first_name, last_name, email, password, birthdate):
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)
        self.birthdate = birthdate

    # TODO: make authentication...
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

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    def to_json(self):
        res = conn.execute(select([self]))
        return json.dumps([dict(r) for r in res])

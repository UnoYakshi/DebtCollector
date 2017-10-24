#! ~DebtCollector/app/modules/auth/models.py

#from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
import json
from datetime import datetime, date

from app import db, bcrypt

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    login = db.Column('login', db.String(32), unique=True, index=True)
    first_name = db.Column('first_name', db.String(128))
    last_name = db.Column('last_name', db.String(128))
    email = db.Column('email', db.String(128), unique=True, index=True)
    pwdhash = db.Column('pwdhash', db.String(128), unique=True)
    birthdate = db.Column('birthdate', db.Date())

    def __init__(self, login, first_name, last_name, email, password, birthdate):
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pwdhash = bcrypt.generate_password_hash(password)
        self.birthdate = birthdate

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.login)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    # TODO :: Make to_json/as_dict automated, but considering datetime and hash...
    def to_json(self):
        return {
            'id': self.id,
            'login': self.login,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'birthdate': self.birthdate
        }

    def as_dict(self):
        return json.dumps({c.name: (c.name.isoformat()) if (type(c) in (datetime, date)) else (getattr(self, c.name)) for c in self.__table__.columns})

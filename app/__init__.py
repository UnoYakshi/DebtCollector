#! ~DebtCollector/app/__init__.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app.modules.auth.views import auth_bp
from app.modules.auth.models import Users
app.register_blueprint(auth_bp)

db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<username>')
def show_user(username):
    user = Users.query.filter_by(login=username).first_or_404()
    return render_template('user.html', user=user)


@app.route('/users?page=<int:count>')
def show_users(count):
    users = Users.query.filter_by(login='Anas').first()
    return render_template('user.html', user=users)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


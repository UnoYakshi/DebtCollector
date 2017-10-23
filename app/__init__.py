#! ~DebtCollector/app/__init__.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app.modules.auth.views import auth_bp
from app.modules.users.views import users_bp
from app.modules.auth.models import Users
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
db.create_all()


@app.route('/')
def index():
    return render_template('index.html')




@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


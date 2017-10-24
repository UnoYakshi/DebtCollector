#! ~DebtCollector/app/__init__.py

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)


from app.modules.auth.views import auth_bp
from app.modules.users.views import users_bp
from app.rest import rest_bp
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
app.register_blueprint(rest_bp, url_prefix='/api')
db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

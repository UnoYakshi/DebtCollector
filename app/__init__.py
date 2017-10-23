#! app/__init__.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
#app.config['SECRET_KEY'] = 'ss'

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<username>')
def show_user():
    user = Users.query.filter_by(login=username).first_or_404()
    return render_template('user.html', user=user)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from .modules.auth.views import auth_bp
app.register_blueprint(auth_bp)

db.create_all()

#! ~DebtCollector/app/__init__.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.modules.auth.models import Users


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
print('12')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<username>')
def show_user(username):
    user = Users.query.filter_by(login=username).first_or_404()
    return render_template('user.html', user=user)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.modules.auth.views import auth_bp
app.register_blueprint(auth_bp)

db.create_all()

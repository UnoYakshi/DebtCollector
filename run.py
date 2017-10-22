from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from database import db
#import json

from modules.auth.views import auth_bp
from modules.users.views import users_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SECRET_KEY'] = 'ss'


db = SQLAlchemy(app)
#db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user():
    user = Users.query.filter_by(login=username).first_or_404()
    return render_template('user.html', user=user)


if __name__ == '__main__':
    app.register_blueprint(auth_bp)
    #app.register_blueprint(users_bp)

    db.create_all()

    app.run(debug=True, port=80)

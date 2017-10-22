from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
import json

from modules.auth.views import auth_bp
from modules.users.views import users_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SECRET_KEY'] = 'ss'

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column('uid', db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    #date = db.Column(db.Date())
    def to_json(self):
        res = conn.execute(select([self]))
        return json.dumps([dict(r) for r in res])

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    db.create_all()
    app.register_blueprint(auth_bp)
    #app.register_blueprint(users_bp)
    app.run(debug=True, port=80)

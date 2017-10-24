#! ~DebtCollector/app/__init__.py

from flask import Flask, render_template, request, jsonify
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


@app.route('/api/users')
def api_users(page=1, per_page=3):
    if request.method == 'POST':
        user = request.get_json()

        new_user = Users(login=form.login.data,
                         first_name=form.first_name.data,
                         last_name=form.last_name.data,
                         email=form.email.data,
                         password=form.password.data,
                         birthdate=form.birthdate.data)
        db.session.add(new_user)
        db.session.commit()
        form = SignUpForm()
        # Validate the input data...

        # Pass through the signup()...

        return "The user's login is {}!".format(user['login'])

    else:
        all_users = {}

        users = db.session.query(Users).paginate(page, per_page, False).items
        for user in users:
            all_users[user.login] = db.session.query(Users).filter_by(login=user.login).first_or_404().to_json()

        return jsonify(all_users)


@app.route('/api/user/<int:id>')
def api_user(id):
    return jsonify(db.session.query(Users).get(id).to_json())


@app.route('/api/user/<string:login>')
def api_user_login(login):
    return jsonify(db.session.query(Users).filter_by(login=login).first_or_404().to_json())


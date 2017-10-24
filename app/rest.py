#! ~DebtCollector/app/rest.py

from flask import Blueprint, render_template, request, jsonify
from app import app, db
from app.modules.auth.models import Users


rest_bp = Blueprint('rest', __name__,
                 template_folder='templates',
                 static_folder='static')


@rest_bp.route('/users')
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
        #form = SignUpForm()
        # Validate the input data...

        # Pass through the signup()...

        return "The user's login is {}!".format(user['login'])

    else:
        all_users = {}

        users = db.session.query(Users).paginate(page, per_page, False).items
        for user in users:
            all_users[user.login] = db.session.query(Users).filter_by(login=user.login).first_or_404().to_json()

        return jsonify(all_users)


@rest_bp.route('/user/<int:id>')
def api_user(id):
    return jsonify(db.session.query(Users).get(id).to_json())


@rest_bp.route('/user/<string:login>')
def api_user_login(login):
    return jsonify(db.session.query(Users).filter_by(login=login).first_or_404().to_json())


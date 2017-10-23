#! ~DebtCollector/app/modules/auth/views.py

from flask import Blueprint, render_template, redirect, url_for, request, session, current_app, g

from .forms import LoginForm, SignUpForm
from .models import Users
from app import db, bcrypt

auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')


@auth_bp.route('/signup', methods=['GET'])
def signup_get():
    form = SignUpForm()
    return render_template('signup.html', form=form)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    form = SignUpForm()
    if form.validate() and form.validate_on_submit():
        # Add new user to db...
        new_user = Users(login=form.login.data,
                         first_name=form.first_name.data,
                         last_name=form.last_name.data,
                         email=form.email.data,
                         password=form.password.data,
                         birthdate=form.birthdate.data)
        db.session.add(new_user)
        db.session.commit()

        # Auto log-in with the provided data... or even auto-log a user in...
        #login_user(new_user)
        login_form = LoginForm()
        login_form.login = form.login
        return render_template('login.html', form=login_form, method='POST')
    return render_template('signup.html', form=form)


@auth_bp.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(login=form.login.data).first()
        if not user:
            return redirect(url_for('index'))

        if bcrypt.check_password_hash(user.pwdhash, form.password.data):
            #login_user(user)
            session['logged_in'] = True
            #identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))

            return redirect(request.args.get('next') or '/')
        #return redirect(url_for('auth.AuthView:index'))
    return redirect(url_for('index'))


@auth_bp.route('/login', methods=['GET'])
def index():
    form = LoginForm()
    return render_template('login.html', form=form)


@auth_bp.route('/logout', methods=['POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))
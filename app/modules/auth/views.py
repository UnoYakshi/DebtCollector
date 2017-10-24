#! ~DebtCollector/app/modules/auth/views.py

from flask import Blueprint, render_template, redirect, url_for, request, session, current_app, g, abort
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlparse, urljoin

from app import db, bcrypt, login_manager
from .models import Users
from .forms import LoginForm, SignUpForm

auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


@login_manager.user_loader
def load_user(uid):
    return db.session.query(Users).get(uid)



@auth_bp.route('/signup', methods=['GET', 'POST'])
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
        form.populate_obj(new_user)
        db.session.add(new_user)
        db.session.commit()

        # Auto log-in with the provided data... or even auto-log a user in...
        login_user(new_user)
        login_form = LoginForm()
        login_form.login = form.login
        return render_template('login.html', form=login_form, method='POST')
    return render_template('signup.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(Users).filter_by(login=form.login.data).first()
        if not user:
            return render_template('login.html', form=form)

        if bcrypt.check_password_hash(user.pwdhash, form.password.data):
            login_user(user)

            next = request.args.get('next')
            if not is_safe_url(next):
                return abort(400)

            return redirect(next or '/')
    return render_template('login.html', form=form)


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@auth_bp.route('/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete_post(id):
    id = int(id)
    user = current_user
    if user.is_authenticated():
        if id == -1:
            instances = user.Compute.delete()
        else:
            try:
                instance = user.Compute.filter_by(id=id).first()
                db.session.delete(instance)
            except:
                pass

        db.session.commit()
    return redirect(url_for('users.edit', username=user.login))

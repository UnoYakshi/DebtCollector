#!/modules/auth/views.py

from flask import Blueprint, render_template, redirect, url_for, request, session, current_app, g
from .forms import LoginForm, SignUpForm

from app import db
#from database import db

auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

#current_app.config['DATABASE']

@auth_bp.route('/signup', methods=['GET'])
def signup_get():
    form = SignUpForm()
    return render_template('signup.html', form=form)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Add new user to db...
        user = Users(login=request.form['login'], first_name=request.form['first_name'], last_name=request.form['last_name'],
                     email=request.form['email'], password=request.form['password'], birthday=request.form['birthday'])
        db.session.add(user)
        db.session.commit()

        # Auto log-in with the provided data... or even auto-log a user in...
        #login_user(new_user)
        return render_template('login.html', form=form, method='POST')
    return render_template('signup.html', form=form)


@auth_bp.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #user = User.getBy(login=form.login.data)
        #if not user:
        #    return redirect(url_for('auth.AuthView:index'))

        if form.password.data == '123': #user.password:
            #login_user(user)
            session['logged_in'] = True
            #identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))

            return redirect(request.args.get('next') or '/')
        #return redirect(url_for('auth.AuthView:index'))
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
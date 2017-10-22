#!/modules/auth/views.py

from flask import Blueprint, render_template, session

from .forms import LoginForm
#from ..users.forms import NewUserForm, SignupForm


auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auth_bp.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    return form.login.data + form.password.data


@auth_bp.route('/login', methods=['GET'])
def index():
    form = LoginForm()
    return render_template('login.html', form=form)

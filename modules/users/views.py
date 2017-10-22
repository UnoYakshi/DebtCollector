#!/modules/users/views.py

from flask import Blueprint, render_template

from .forms import NewUserForm, EditUserForm


users_bp = Blueprint('users', __name__, template_folder='templates', static_folder='static')


#@users_bp.route('/login', methods=['POST'])
#def login():
#    form = LoginForm
#    return render_template('login.html')

@users_bp.route('/signup', methods=['POST'])
def sign_up():
    form = NewUserForm()
    return render_template('signup.html')

@users_bp.route('/edit', methods=['POST'])
def edit():
    form = EditUserForm()
    return render_template('edit.html')

@users_bp.route('/logout', methods=['POST'])
def index():
    return render_template('index.html')


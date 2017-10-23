#!/modules/users/views.py

from flask import Blueprint, render_template

from .forms import NewUserForm, EditUserForm
from database import db

users_bp = Blueprint('users', __name__, template_folder='templates', static_folder='static')




@users_bp.route('/edit', methods=['POST'])
def edit():
    form = EditUserForm()
    return render_template('edit.html')

@users_bp.route('/logout', methods=['POST'])
def index():
    return render_template('index.html')


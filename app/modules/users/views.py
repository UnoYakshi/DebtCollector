#!/modules/users/views.py

from flask import Blueprint, render_template

from .forms import EditUserForm
from app import db
from app.modules.auth.models import Users


users_bp = Blueprint('users', __name__,
                     template_folder='templates',
                     static_folder='static')


@users_bp.route('/user/<username>', methods=['GET'])
def show_user(username):
    user = Users.query.filter_by(login=username).first_or_404()
    return render_template('user.html', user=user)


@users_bp.route('/users/<int:per_page>/<int:page_num>', methods=['GET'])
def show_users(page_num=1, per_page=3):
    return render_template('users.html', users_pg=Users.query.paginate(page_num, per_page, False))



@users_bp.route('/user/<username>/edit', methods=['GET'])
def edit(username):
    form = EditUserForm()
    user = Users.query.filter_by(login=username).first_or_404()
    return render_template('edit.html', user=username, form=form)


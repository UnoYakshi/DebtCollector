#!/modules/users/views.py
from config import MAX_UNITS_PER_PAGE
from flask import Blueprint, render_template
from flask_login import current_user, login_required

from .forms import EditUserForm
from app import db
from app.modules.auth.models import Users


users_bp = Blueprint('users', __name__,
                     template_folder='templates',
                     static_folder='static')


@users_bp.route('/user/<username>', methods=['GET'])
def show_user(username):
    user = db.session.query(Users).filter_by(login=username).first_or_404()
    return render_template('user.html', user=user)


@users_bp.route('/users/<int:per_page>/<int:page_num>', methods=['GET'])
def show_users(page_num=1, per_page=3):
    # Clamp for the sake of bd safety...
    pp = per_page
    if pp > MAX_UNITS_PER_PAGE:
        pp = MAX_UNITS_PER_PAGE
    users = db.session.query(Users).paginate(page_num, per_page, False)
    return render_template('users.html', users_pg=users, pp=pp)


@users_bp.route('/user/<username>/edit', methods=['GET'])
@login_required
def edit(username):
    form = EditUserForm()
    user = db.session.query(Users).filter_by(login=username).first_or_404()
    return render_template('edit.html', user=username, form=form)

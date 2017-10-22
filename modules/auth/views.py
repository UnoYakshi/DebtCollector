#!/modules/auth/views.py

from flask import Blueprint, render_template, redirect, url_for, request, session


from .forms import LoginForm


auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')



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
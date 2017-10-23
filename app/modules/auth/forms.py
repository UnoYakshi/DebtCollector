#! ~DebtCollector/app/modules/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import date

from .models import Users

class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignUpForm(LoginForm):
    login = StringField('Login')
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=25)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match!')])
    confirm = PasswordField('Confirm')
    birthdate = DateField('Birthdate', format='%d/%m/%Y', validators=[DataRequired()]) #, DateRange(max=datetime.now())])

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        user = Users.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken.")
            return False
        else:
            return True
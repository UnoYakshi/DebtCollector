#! ~DebtCollector/app/modules/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateField


from .models import Users

class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignUpForm(LoginForm):
    login = StringField('Login',
                        validators=[DataRequired(), Length(max=32)],
                        render_kw={"placeholder": "JoDo_316"})
    first_name = StringField('First Name',
                             validators=[DataRequired(), Length(min=2, max=32)],
                             render_kw={"placeholder": "John"})
    last_name = StringField('Last Name',
                            validators=[DataRequired(), Length(min=2, max=32)],
                            render_kw={"placeholder": "Doe"})
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=3, max=40)],
                        render_kw={"placeholder": "user.example@mail.com"})
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('confirm', message='Passwords must match!')])
    confirm = PasswordField('Confirm')
    birthdate = DateField('Birthdate',
                          format='%d.%m.%Y',
                          validators=[DataRequired()
    #, DateRange(min=date.today() - timedelta(years=18),max=date.today())
                                      ],
                          render_kw = {"placeholder": "14.02.1990"})

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        user = Users.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken.")
            return False
        else:
            return True
#! ~DebtCollector/app/modules/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from wtforms.fields.html5 import DateField

from .models import Users
from app import db


# Validator that checks if the field is not in the model yet...
class Unique(object):
    def __init__(self, model, field, message='Is taken already.'):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def get_user(self):
        return db.session.query(Users).filter_by(login=self.login.data).first()


class SignUpForm(LoginForm):
    login = StringField('Login',
                        validators=[DataRequired(),
                                    Unique(Users, Users.login),
                                    Length(max=32)],
                        render_kw={"placeholder": "JoDo316"})
    first_name = StringField('First Name',
                             validators=[DataRequired(),
                                         Regexp('((^[A-Z][a-z]+$)|(^[А-Я][а-я]+$))',
                                                message='Either cyrrilic, or latin. Start with the capital.'),
                                         Length(min=2, max=32)],
                             render_kw={"placeholder": "John"})
    last_name = StringField('Last Name',
                            validators=[DataRequired(),
                                        Regexp('((^[A-Z][a-z]+$)|(^[А-Я][а-я]+$))',
                                               message='Either cyrrilic, or latin. Start with the capital.'),
                                        Length(min=2, max=32)],
                            render_kw={"placeholder": "Doe"})
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email(),
                                    Unique(Users, Users.email),
                                    Length(min=3, max=40)],
                        render_kw={"placeholder": "user.example@mail.com"})
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Regexp('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{8,32})',
                                                message='Use at least once: a-z, A-Z, 0-9, [@#$%]'),
                                         EqualTo('confirm', message='Passwords must match!')])
    confirm = PasswordField('Confirm')
    birthdate = DateField('Birthdate',
                          format='%d.%m.%Y',
                          validators=[DataRequired()
    #, DateRange(min=date.today() - timedelta(years=18),max=date.today())
                                      ],
                          render_kw={"placeholder": "14.02.1990"})

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        # Check for email...
        user = db.session.query(Users).filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append('That email is already taken.')
            return False

        # Check for login/username...
        user = db.session.query(Users).filter_by(email=self.login.data).first()
        if user:
            self.login.errors.append('That login/username is already taken.')
            return False

        return True

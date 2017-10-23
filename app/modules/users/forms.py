from wtforms import Form, StringField, PasswordField, SelectMultipleField, BooleanField, SelectField, validators


class NewUserForm(Form):

    first_name = StringField('first_name', validators=[validators.Length(min=1, max=30)])
    last_name = StringField('last_name', validators=[validators.Length(min=1, max=30), validators.DataRequired])
    login = StringField('login', validators=[validators.Length(min=1, max=30)])
    password = PasswordField('password', validators=[validators.Length(min=1), validators.EqualTo('confirm', message='Passwords must match!')])
    confirm = PasswordField('confirm', validators=[validators.DataRequired()])


class EditUserForm(Form):

    first_name = StringField('first_name', validators=[validators.Length(min=1, max=30)])
    last_name = StringField('last_name', validators=[validators.Length(min=1, max=30)])
    login = StringField('login', validators=[validators.Length(min=1, max=30)])
#    password = PasswordField('password', validators=[validators.Length(min=1), validators.EqualTo('confirm', message='Passwords must match!')])
#    confirm = PasswordField('confirm', validators=[validators.DataRequired()])


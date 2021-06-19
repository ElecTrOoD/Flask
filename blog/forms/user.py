from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserRegisterForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.length(3, 25)])
    first_name = StringField('First name', [validators.DataRequired(), validators.length(2, 25)])
    last_name = StringField('Last name', [validators.DataRequired(), validators.length(2, 25)])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.length(8, 25),
                                          validators.EqualTo('password_confirm',
                                                             message='Field must be equal to password')])
    password_confirm = PasswordField('Confirm password', [validators.DataRequired(), validators.length(8, 25)])
    submit = SubmitField('Register')


class UserLoginForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.length(8, 25)])
    submit = SubmitField('Login')

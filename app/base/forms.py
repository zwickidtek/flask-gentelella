from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

## login and registration


class LoginForm(FlaskForm):
    username = StringField('Name', id='username_login')
    password = PasswordField('Password', id='pwd_login')


class CreateAccountForm(FlaskForm):
    username = StringField('Name', id='username_create')
    email = StringField('Email')
    password = PasswordField('Password', id='pwd_create')

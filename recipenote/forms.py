"""This module will contain all the forms for the application"""
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class RegisterationForm(FlaskForm):
    "Controls the signup form"
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('password2', validators=[DataRequired()])
    submit = SubmitField('register')


class LoginForm(FlaskForm):
    "Controls the Login form"
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('login')

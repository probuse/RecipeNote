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


class RecipesForm(FlaskForm):
    "Form to help manipulate recipes"
    name = StringField('name', validators=[DataRequired()])
    ingredients = TextAreaField('ingredients', validators=[DataRequired()])
    prep_method = TextAreaField('method', validators=[DataRequired()])
    prep_time = StringField('time', validators=[DataRequired()])


class DeleteRecipesForm(FlaskForm):
    "Form to help us delete a recipe"
    id = StringField('id', validators=[DataRequired()])


class CategoryForm(FlaskForm):
    "Form to help manipulate categories"
    name = StringField('name', validators=[DataRequired()]) 


class DeleteCategoryForm(FlaskForm):
    "Form to help us delete a category"
    id = StringField('id', validators=[DataRequired()])

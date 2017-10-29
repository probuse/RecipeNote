""" 
contains all the logic for RecipeNote app RecipeNote app is a 
web application that lets users create, edit, delete and even share 
their favourite recipes with their friends and family.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    "Renders the landing page"
    return render_template('base.html')

@app.route('/register')
def register():
    "Renders the index page"
    return render_template('register.html')

@app.route('/login')
def login():
    "Renders login page"
    return render_template('login.html')

@app.route('/forgot-password')
def forgot_password():
    "Renders forgot-password page"
    return render_template('forgot-password.html')

@app.route('/recipes')
def recipes():
    "Renders the recipes page"
    return render_template('recipes.html')

@app.route('/recipe_detail')
def recipe_detail():
    "Renders the recipes detail page"
    return render_template('recipe_detail.html')

@app.route('/recipes_add')
def recipes_add():
    "Renders the create page for recipes"
    return render_template('recipes_add.html')

@app.route('/recipe_edit')
def recipe_edit():
    "Renders the edit page for recipes"
    return render_template('recipe_edit.html')

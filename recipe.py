""" 
contains all the logic for RecipeNote app RecipeNote app is a 
web application that lets users create, edit, delete and even share 
their favourite recipes with their friends and family.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    "Renders the landing page"
    return render_template('index.html')

@app.route('/register')
def register():
    "Renders the index page"
    return render_template('register1.html')

@app.route('/login')
def login():
    "Renders login page"
    return render_template('login_.html')

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

@app.route('/category')
def category():
    "Renders the category page"
    return render_template('category.html')

@app.route('/category_create')
def category_create():
    "Renders the page to create a new category"
    return render_template('category_create.html')

@app.route('/category_edit')
def category_edit():
    "Renders the page for editing and deleting a category"
    return render_template('category_edit.html')

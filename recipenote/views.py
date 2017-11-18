"""contains all the logic for RecipeNote app RecipeNote app is a 
web application that lets users create, edit, delete and even share 
their favourite recipes with their friends and family.
"""
import os

from flask import render_template, flash, session, redirect, url_for, request
from functools import wraps

from . import app
from .forms import LoginForm, RegisterationForm, RecipesForm, CategoryForm
from recipenote.models.user import Category, Recipe, User
from recipenote.sessions.sessions import SessionUser

app.secret_key = "StumblingFromRightQuestionsToWrongAnswers"

logged_in_users = {}

def create_appplication_session_keys():
    "creates application session for different keys"
    if "users" not in session:
        session["users"] = {}
    if "logged_in" not in session:
        session["logged_in"] = None


def login_required(f):
    "Allows only logged in users to view content"
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'users' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for("login"))
    return wrap

@app.route('/')
def index():    
    "Renders the landing page"
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    "Renders the register page"
    create_appplication_session_keys()
    form = RegisterationForm()
   
    if form.validate_on_submit():
        # Check for password mismatch
        if form.password.data != form.password2.data:
            message = "Your passwords do not match"
            flash(message)
            return render_template(
                'register.html', 
                title="Create Profile", 
                form=form
            )

        new_user = SessionUser(
            form.username.data,
            form.email.data,
            form.password.data
        )
        user_object = User(
            form.username.data, 
            form.email.data, 
            form.password.data
        )
        logged_in_users['user'] = user_object

        session["users"][new_user.id] = vars(new_user)
        session['logged_in'] = vars(new_user)
        flash("Your account has been created, Login to continue")
        return redirect(url_for("login"))
    return render_template("register.html", title="Create Profile", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    "Renders login page"
    create_appplication_session_keys()
    form = LoginForm()

    if form.validate_on_submit():
        users = session["users"]
        for key in users:
            user = users[key]
            username = form.username.data.strip()
            password = form.password.data.strip()
        
            if user["username"] == username and user["password"] == password:
                flash("You are now logged in")
                return redirect(url_for("recipes"))
            else:
                message = "Wrong username or password, Please Try Again"
                flash(message)
    return render_template('login.html', title='Login', form=form)


@app.route('/recipes')
@login_required
def recipes():
    "Renders the recipes page"
    user = logged_in_users['user']
    # for category in user.user_categories:
    user_categories = user.user_categories
    print(user_categories)
    return render_template('recipes.html', user_categories=user_categories)

@app.route('/recipe_detail/<recipe_name>')
@login_required
def recipe_detail(recipe_name):
    "Renders the recipes detail page"
    user = logged_in_users['user']

    for category in user.user_categories:
        for recipe in user.user_categories[category]:
            if recipe == recipe_name:
                prep_method = user.user_categories[category][recipe]
                print(recipe, "=>", prep_method)
    return render_template('recipe_detail.html', 
                            recipe_name=recipe_name,
                            prep_method=prep_method)

@app.route('/recipes_add', methods=["GET", "POST"])
@login_required
def recipes_add():
    "Renders the create page for recipes"
    create_appplication_session_keys()
    user = logged_in_users['user']
    form_recipe = RecipesForm()
    form_categories = CategoryForm()
    categories = user.user_categories.keys()

    if request.method == 'POST':
        selected_category = request.form['selectedCategory']

    if form_recipe.validate_on_submit():
        new_recipe = user.create_recipes(
            form_recipe.name.data, 
            selected_category, 
            form_recipe.prep_method.data)
        print(new_recipe.name)
        flash("Your recipe has been successfully added")
        return redirect(url_for("recipes"))
    return render_template(
            'recipes_add.html', 
            form_recipe=form_recipe, 
            categories=categories
        )

@app.route('/recipe_edit/<recipe_name>', methods=['POST', 'GET'])
@login_required
def recipe_edit(recipe_name):
    "Renders the edit page for recipes"
    user = logged_in_users['user']

    for category in user.user_categories:
        for recipe in user.user_categories[category]:
            if recipe == recipe_name:
                recipe = Recipe(recipe, user.user_categories[category][recipe])
    categories = user.user_categories.keys()
    form_recipe = RecipesForm(obj=recipe)   

    print(user.user_categories, "<<<<<<<<<<<<<<<<<<<<<<<<<<")
    if form_recipe.validate_on_submit():
        if request.method == 'POST':    
            edited_name_category = request.form['selectedCategory']
        edited_new_name = form_recipe.name.data
        edited_prep_method = form_recipe.prep_method.data
        user.delete_recipe(recipe_name)
        print(user.user_categories, ">>>>>>>>>>>>>>>>>>>>>>>>>")
        user.create_recipes(
            edited_new_name, 
            edited_name_category, 
            edited_prep_method)
        flash("Your recipe has been successfully Updated")
        print("++++", edited_new_name, edited_name_category, edited_prep_method, "++++")
        return redirect(url_for('recipes'))
    
    return render_template('recipe_edit.html',
                            categories=categories,
                            form_recipe=form_recipe,
                            recipe_name=recipe_name)

@app.route('/delete_recipe/<recipe_name>')
def delete_recipe(recipe_name):
    "Deletes selected recipe"
    user = logged_in_users['user']

    for category in user.user_categories:
        for recipe in user.user_categories[category]:
            if recipe == recipe_name:
                user.delete_recipe(recipe)
                return redirect(url_for('recipes'))


@app.route('/category_add', methods=["GET", "POST"])
@login_required
def category_add():
    "Renders the page to create a new category"
    create_appplication_session_keys()
    form_categories = CategoryForm()
    user = logged_in_users['user']
    
    if form_categories.validate_on_submit():
        user.create_category(form_categories.name.data)
        flash("Category has been successfully added")
        return redirect(url_for("category"))
    return render_template('category_create.html',
                            form_categories=form_categories)

@app.route('/category')
@login_required
def category():
    "Renders the category page"
    create_appplication_session_keys()
    user = logged_in_users['user']
    categories = user.user_categories.keys()

    return render_template('category.html', 
                            categories=categories   )

@app.route('/category_edit/<name>', methods=['POST', 'GET'])
@login_required
def category_edit(name):
    "Renders the page for editing and deleting a category"
    user = logged_in_users['user']
    category = Category(name)
    form = CategoryForm(obj=category)
    if form.validate_on_submit():
        user.edit_category_name(name, form.name.data)
        print(form.name.data, "-----------")
        flash("Your category has been successfully Updated")
        return redirect(url_for('category'))
    return render_template(
            'category_edit.html', 
            form=form,
            name=name)

@app.route('/delete_category/<category_name>', methods=['POST', 'GET'])
@login_required
def delete_category(category_name):
    "Deletes category name"
    user = logged_in_users['user']
    user.delete_category(category_name)
    flash("Category {} has been successfully been deleted".format(category_name))
    return redirect(url_for('category'))

@app.route('/logout')
@login_required
def logout():
    "Renders the logout page"
    session.pop('users', None)
    del logged_in_users['user']
    flash("You are now logged out")
    return redirect(url_for("index"))

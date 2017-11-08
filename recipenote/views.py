"""contains all the logic for RecipeNote app RecipeNote app is a 
web application that lets users create, edit, delete and even share 
their favourite recipes with their friends and family.
"""
import os

from flask import render_template, flash, session, redirect, url_for, request
from functools import wraps

from . import app
from .forms import LoginForm, RegisterationForm, RecipesForm, CategoryForm
from recipenote.models.user import User

app.secret_key = "StumblingFromRightQuestionsToWrongAnswers"

logged_in_users = {}

class Base:
    "Used to generate session_id"

    def generate_session_id(self, session_key):
        """returns a randomly generated session_id if not in session already
        Random no one guesses it :-)"""
        session_id = str(os.urandom(10))
        while session_id in session[session_key]:
            session_id = str(os.urandom(10))

        return session_id

class SessionUser(Base):
    "Stores the user object during a session"
   
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.id = self.generate_session_id("users")


class Recipe(Base):
    "Stores the recipe object during a session"

    def __init__(self, name, category, ingredients, prep_method, prep_time):
        self.name = str(name).title()
        self.category = str(category).title()
        self.ingredients = ingredients
        self.prep_method = prep_method
        self.user_id = session["logged_in"]["id"]
        self.prep_time = prep_time
        self.id = self.generate_session_id("recipe")


class Category(Base):
    "Stores the category object during a session"

    def __init__(self, name):
        self.name = name
        self.user_id = session["logged_in"]["id"]
        self.id = self.generate_session_id("category")



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
        flash({"message": "Your account has been created, Login to continue"})
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
                return redirect(url_for("recipes"))
            message = "Wrong username or password, Please Try Again"
            flash(message)
    return render_template('login.html', title='Login', form=form)


@app.route('/recipes')
@login_required
def recipes():
    "Renders the recipes page"
    user = logged_in_users['user']
    user_recipes = user.user_recipes
    print(user_recipes)
    return render_template('recipes.html', user_recipes=user_recipes)

@app.route('/recipe_detail/<recipe_name>')
@login_required
def recipe_detail(recipe_name):
    "Renders the recipes detail page"
    user = logged_in_users['user']

    for recipe in user.user_recipes.keys():
        if recipe == recipe_name:
            prep_method = user.user_recipes[recipe]
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
        flash({"message": "Your recipe has been successfully added"})
        return redirect(url_for("recipes"))
    return render_template(
            'recipes_add.html', 
            form_recipe=form_recipe, 
            categories=categories
        )

@app.route('/recipe_edit', methods=['POST', 'GET'])
@app.route('/recipe_edit/<recipe_name>', methods=['POST', 'GET'])
@login_required
def recipe_edit(recipe_name=None):
    "Renders the edit page for recipes"
    user = logged_in_users['user']
    # recipe = user.
    form_recipe = RecipesForm()

    if recipe_name is not None:

        if request.method == 'POST':
            new_name_category = request.form['selectedCategory']

        
        if form_recipe.validate_on_submit():
            new_name = form_recipe.name.data
            edited_prep_method = form_recipe.prep_method.data
            # edited_category_name = user.edit_recipe_name(old_name, new_name)
            user.create_recipes(
                new_name, 
                new_name_category, 
                edited_prep_method)
            print("++++", new_name, new_name_category, edited_prep_method, "++++")
            return redirect(url_for('recipes'))
    
    return render_template('recipe_edit.html', 
                            form_recipe=form_recipe,
                            recipe_name=recipe_name)

@app.route('/category_add', methods=["GET", "POST"])
@login_required
def category_add():
    "Renders the page to create a new category"
    create_appplication_session_keys()
    form_categories = CategoryForm()
    user = logged_in_users['user']
    
    if form_categories.validate_on_submit():
        user.create_category(form_categories.name.data)
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

@app.route('/category_edit/<name>')
@login_required
def category_edit(name):
    "Renders the page for editing and deleting a category"
    category = Category()
    form = CategoryForm(obj=category)
    user = logged_in_users['user']

    if form.validate_on_submit():
        user.edit_category_name(form.name.data)
        print(category.name)
    return render_template(
            'category_edit.html', 
            form=form,
            name=name)

@app.route('/logout')
@login_required
def logout():
    "Renders the logout page"
    session.pop('users', None)
    del logged_in_users['user']
    flash("You are now logged out")
    return redirect(url_for("index"))

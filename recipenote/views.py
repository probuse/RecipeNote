"""contains all the logic for RecipeNote app RecipeNote app is a 
web application that lets users create, edit, delete and even share 
their favourite recipes with their friends and family.
"""
import os

from flask import render_template, flash, session, redirect, url_for, request
from functools import wraps

from . import app
from .forms import LoginForm, RegisterationForm

app.secret_key = "StumblingFromRightQuestionsToWrongAnswers"

class Base:
    "Used to generate session_id"

    def generate_session_id(self, session_key):
        """returns a randomly generated session_id if not in session already
        Random no one guesses it :-)"""
        session_id = str(os.urandom(10))
        while session_id in session[session_key]:
            session_id = str(os.urandom(10))

        return session_id

class User(Base):
    "Stores the user object during a session"
   
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.id = self.generate_session_id("users")


def create_appplication_session_keys():
    "creates application session for different keys"
    if "users" not in session:
        session["users"] = {}
    if "recipe" not in session:
        session["recipe"] = {}


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
    session.pop("users", None)
    create_appplication_session_keys()
    form = RegisterationForm()
   
    if form.validate_on_submit():
        # Check for password mismatch
        if form.password.data != form.password2.data:
            message = "Your passwords do not match"
            print(message)
            flash(message)
            return render_template(
                'register.html', 
                title="Create Profile", 
                form=form
            )

        new_user = User(
            form.username.data,
            form.email.data,
            form.password.data
        )

        session["users"][new_user.id] = vars(new_user)
        flash({"message": "Your account has been created, Login to continue"})
        return redirect(url_for("login"))
    return render_template("register.html", title="Create Profile", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    "Renders login page"
    create_appplication_session_keys()
    form = LoginForm()

    if form.validate_on_submit():
        print("hello")
        users = session["users"]
        for key in users:
            user = users[key]
            username = form.username.data.strip()
            password = form.password.data.strip()
            print(username, password)
            print("form => {} {}".format(user["username"], user["password"]))
            if user["username"] == username and user["password"] == password:
                return redirect(url_for("recipes"))
            message = "Wrong username or password, Please Try Again"
            flash(message)
            return redirect(url_for("login"))
    
    return render_template('login.html', title='Login', form=form)

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

@app.route('/logout')
def logout():
    "Renders the logout page"
    return render_template('logout.html')

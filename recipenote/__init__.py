""" Module to help us set up the Flask"""
from flask import Flask
from flask_bootstrap import Bootstrap

# initialize the flask application
app = Flask(__name__)
Bootstrap(app)

# After initialization, import views
from . import views

""" Module to help us set up the Flask"""
from flask import Flask

# initialize the flask application
app = Flask(__name__)

# After initialization, import views
from . import views

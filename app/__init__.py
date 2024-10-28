from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)

# Ensure the `mongo` instance is available globally if you're accessing it in other modules.
from app import routes

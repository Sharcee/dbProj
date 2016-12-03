# @Tech: Flask
from flask import Flask

# Create a Flask app object @db_app
db_app = Flask(__name__)

# Fancy dictionary function object; holds flask config settings
db_app.config.from_object('config')

# Import views from app package
from app import views

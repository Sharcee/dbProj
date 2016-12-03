from flask import Flask

db_app = Flask(__name__)  # Create a Flask app object @db_app
from app import views     # Import views from app package

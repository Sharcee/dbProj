from app import db_app
from flask import render_template

@db_app.route('/')		# Home Route
@db_app.route('/index')	# Index
def index():
	return render_template('index.html')

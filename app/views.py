from app import db_app
@db_app.route('/')	# Home Route
@db_app.route('/index')	# Index
def index():
	return "Welcome to db_proj!"

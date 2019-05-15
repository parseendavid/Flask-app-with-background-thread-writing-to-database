from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object('config')

# Initialize the db
db = SQLAlchemy(app)

#Initialize migrate
migrate = Migrate(app, db)

# Load the views
from app import routes
from app.models import Joke
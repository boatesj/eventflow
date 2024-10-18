import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

if os.path.exists("env.py"):
    import env  # noqa

# Initialize the app
app = Flask(__name__)

# Set the secret key and database URI from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress the warning

# Initialize the database and migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes and models
from eventflow import routes  # noqa
from eventflow import models  # noqa

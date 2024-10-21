import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Check if env.py exists and load it for environment variables
if os.path.exists("env.py"):
    import env  # noqa

# Initialize the Flask app
app = Flask(__name__)

# Set the secret key from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Database configuration: handle development vs production and PostgreSQL URI replacement
if os.environ.get("DEVELOPMENT") == "True":
    # Use the development database URL
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    # Use the production database URL and handle PostgreSQL URI fix for Heroku
    uri = os.environ.get("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Suppress the SQLAlchemy modification tracking warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration modules
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Print the database URI to verify
print("Using database:", app.config["SQLALCHEMY_DATABASE_URI"])

# Custom filter to format datetime to 'dd-mm-yyyy' (U.K. format)
@app.template_filter('dateformat')
def dateformat(value, format='%d-%m-%Y'):
    if value is None:
        return ""
    
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return value

    return value.strftime(format)

# Import routes and models after app initialization to avoid circular imports
from eventflow import routes  # noqa
from eventflow import models  # noqa

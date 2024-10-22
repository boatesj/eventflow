import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Load environment variables if env.py exists
if os.path.exists("env.py"):
    import env  # noqa

# Initialize the Flask app
app = Flask(__name__)

# Set the secret key from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "your_default_secret_key")

# Set the database URI based on environment
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Initialize the database
db = SQLAlchemy(app)

# Initialize migration support
migrate = Migrate(app, db)

# Register custom 'dateformat' filter
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

# Import routes after app and db initialization to avoid circular imports
from eventflow import routes  # noqa

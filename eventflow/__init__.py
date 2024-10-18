import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

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

# Import routes and models
from eventflow import routes  # noqa
from eventflow import models  # noqa

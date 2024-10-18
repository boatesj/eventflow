import sys
import os
from flask import request, redirect, url_for, flash, render_template, jsonify
from werkzeug.utils import secure_filename
from eventify import app, db
from eventify.models import Event, Category
from datetime import datetime
from eventify.models import RSVP  # Import the RSVP model
from eventify.email_utils import send_rsvp_confirmation
from flask_mail import Message
from eventify import mail
from datetime import datetime, timedelta
from flask_login import current_user
import json




# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Home page showing list of all upcoming and past events
@app.route("/")
def home():
    sort_by = request.args.get("sort_by", "date")  # Default sort by date
    order = request.args.get("order", "asc")  # Default order ascending

    now = datetime.now()

    featured_events = Event.query.filter_by(featured=True).order_by(Event.date.asc()).all()
    
    if sort_by == "date":
        if order == "asc":
            upcoming_events = Event.query.filter(Event.date >= now).order_by(Event.date.asc()).all()
            past_events = Event.query.filter(Event.date < now).order_by(Event.date.asc()).all()
        else:
            upcoming_events = Event.query.filter(Event.date >= now).order_by(Event.date.desc()).all()
            past_events = Event.query.filter(Event.date < now).order_by(Event.date.desc()).all()

  
    return render_template("events.html", upcoming_events=upcoming_events, past_events=past_events, featured_events=featured_events, user=current_user)
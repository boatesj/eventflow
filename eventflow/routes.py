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


    # Add event details
@app.route("/event/<int:event_id>", methods=["GET", "POST"])
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    rsvps = RSVP.query.filter_by(event_id=event_id).all()  # Fetch RSVPs for this event

    
    if request.method == "POST":
        try:
            # Debugging: Log the form data
            print(f"Form Submitted: {request.form}")

            # Handle RSVP form submission
            name = request.form.get("name")
            email = request.form.get("email")
            attending = request.form.get("attending") == "1" if request.form.get("attending") else False

            # Debugging: Log the RSVP details
            print(f"RSVP Details - Name: {name}, Email: {email}, Attending: {attending}")

            # Check if an RSVP for this event and email already exists
            existing_rsvp = RSVP.query.filter_by(event_id=event_id, email=email).first()

            if existing_rsvp:
                # Debugging: Log existing RSVP update
                print(f"Updating existing RSVP for {email}")

                # If RSVP exists, update it
                existing_rsvp.attending = attending
                existing_rsvp.name = name  # Update name in case the user changes it
                db.session.commit()
                flash(f"RSVP updated successfully for {email}!", "success")
            else:
                # Debugging: Log new RSVP creation
                print(f"Creating new RSVP for {email}")

                # Create a new RSVP entry
                rsvp_entry = RSVP(event_id=event_id, name=name, email=email, attending=attending)
                db.session.add(rsvp_entry)
                db.session.commit()
                flash(f"RSVP submitted successfully for {email}!", "success")

            # Redirect to avoid form re-submission on refresh
            return redirect(url_for("event_detail", event_id=event_id))

        except Exception as e:
            db.session.rollback()  # Roll back any changes in case of an error
            flash(f"Error submitting RSVP: {str(e)}", "error")
            return redirect(url_for("event_detail", event_id=event_id))

    # Pass the RSVPs to the template for display
    return render_template("event_detail.html", event=event, rsvps=rsvps)



# Create a new event
@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    categories = Category.query.all()  # Fetch all categories
    if request.method == "POST":
        try:
            # Extract event details from the form
            title = request.form.get("title")
            description = request.form.get("description")
            event_date_raw = request.form.get("date")  # Expecting 'dd-mm-yyyy'
            event_time_raw = request.form.get("time")  # Expecting 'HH:MM'
            location = request.form.get("location")
            category_id = request.form.get("category_id")
            featured = request.form.get("featured") == "1"  # Store as boolean

            # Debugging: Log form data for troubleshooting
            print("Form Data:", request.form)
            print("Selected Date:", event_date_raw)
            print("Selected Time:", event_time_raw)

            # Parse the date and time strings using dd-mm-yyyy format for date and HH:MM for time
            day, month, year = map(int, event_date_raw.split('-'))
            hour, minute = map(int, event_time_raw.split(':'))

            # Create a datetime object for the event date and time
            event_date = datetime(year, month, day, hour, minute)

            # Handle file upload
            file = request.files.get('image')
            filename = None
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.static_folder, 'images', filename)
                print(f"File path: {file_path}")  # Log the file path
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                file.save(file_path)
                print(f"File {filename} saved successfully.")
            else:
                print("File upload failed or invalid file type.")

            # Create the event and save it to the database
            event = Event(
                title=title,
                description=description,
                date=event_date,  # Store date as datetime object
                time=event_time_raw,  # Store time as string (make sure it's passed here)
                location=location,
                category_id=category_id,
                featured=featured,
                image_file=filename  # Store the filename in the database
            )

            db.session.add(event)
            db.session.commit()
            flash('Event added successfully!', 'success')
            return redirect(url_for('home'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error adding event: {str(e)}', 'error')
            return redirect(url_for('add_event'))

    return render_template("add_event.html", categories=categories)